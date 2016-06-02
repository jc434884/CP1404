"""
Author: Jenishkumar Dhirajlal Rank (13186622)

Note: My previous assignment1 code was done in hurry. It had some faults. So I had to create this code to use it for assignment 2.

git hub repository: https://github.com/rankjenish/JenishkumarRankA1

"""

__Author__ = "Jenishkumar Dhirajlal Rank"
FILE_NAME = "items.csv"


def main(file_name):

    print('Items for Hire - by:{}\n'.format(__Author__))

    import_file = open("{}".format(file_name), mode='r')
    items_lists = format_csv_file_data_for_use(import_file)
    import_file.close()

    items_loaded = len(items_lists)
    print("{} items loaded from {}".format(items_loaded, file_name))

    main_menu = "Menu:\n(L)ist all items \n(H)ire an Item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"

    print(main_menu)

    chosen_menu_option = input('Input your selection: ')
    chosen_menu_option = chosen_menu_option.upper()

    while chosen_menu_option != 'Q':
        if chosen_menu_option == 'L':
            print("All items on file (* indicates item is currently out):")
            print_items_list_all(items_lists, 1)

        elif chosen_menu_option == 'H':
            print('Hire Item')
            check_status_list = check_item_status(items_lists,"in")

            if check_status_list == 0:

                print("No items available for hire")
            else:
                print_items_list_all(items_lists, 3)
                items_lists = hire_item(items_lists)

        elif chosen_menu_option == 'R':
            print('Return Item')
            check_status_list = check_item_status(items_lists,"out")

            if check_status_list == 0:

                print("No items are currently on hire")
            else:
                print_items_list_all(items_lists, 2)
                items_lists = return_item(items_lists)
        elif chosen_menu_option == 'A':
            print('Add Item')
            items_lists = add_new_item(items_lists)
        else:
            print("Invalid choice")

        print(main_menu)
        chosen_menu_option = input('Input your selection: ')
        chosen_menu_option = chosen_menu_option.upper()

    save_file_data = format_csv_file_data_to_save(items_lists)
    import_file = open("{}".format(FILE_NAME), mode='w')
    import_file.write(save_file_data)
    import_file.close()
    final_item_count = len(items_lists)
    print("{} items saved to {}\nHave a nice day :)".format(final_item_count, file_name))


def format_csv_file_data_for_use(imported_file):

    whole_file_string = imported_file.read()
    list_of_strings = whole_file_string.strip()
    list_of_strings = list_of_strings.split('\n')

    counter_strip = 0
    for n in list_of_strings:
        list_of_strings[counter_strip] = list_of_strings[counter_strip].strip()
        counter_strip += 1

    counter_split = 0
    for i in list_of_strings:
        list_of_strings[counter_split] = list_of_strings[counter_split].split(',')
        counter_split += 1
    return list_of_strings


def format_csv_file_data_to_save(finalized_list):

    string_to_save_to_file = ""
    first_loop_counter = 0
    for list in finalized_list:
        finalized_list[first_loop_counter] = ("{},{},{},{}\n".format(list[0], list[1], list[2], list[3]))
        first_loop_counter += 1

    second_loop_counter = 0
    for i in finalized_list:
        string_to_save_to_file = string_to_save_to_file + finalized_list[second_loop_counter]
        second_loop_counter += 1
    return string_to_save_to_file


def print_items_list_all(printable_list, print_option):

    counter_main = 0
    blank_string = ''

    ##print all items
    if print_option == 1:
        for i in printable_list:
            working_list = printable_list[counter_main]
            spacing_length = 40 - (len(working_list[0] + working_list[1]))

            for i in range(1, spacing_length, 1):
                blank_string += ' '

            if working_list[3] == 'in':
                print("{} - {} ({}){}\t\t\t= ${:.2f}".format(counter_main, working_list[0], working_list[1], blank_string, float(working_list[2])))

            elif working_list[3] == 'out':
                print("{} - {} ({}){}\t\t\t= ${:.2f}{}".format(counter_main, working_list[0], working_list[1], blank_string, float(working_list[2]), '*'))

            counter_main += 1
            blank_string = ' '
    ##print only unavailable items
    elif print_option == 2:
        for i in printable_list:
            working_list = printable_list[counter_main]
            spacing_length = 40 - (len(working_list[0] + working_list[1]))

            for i in range(1, spacing_length, 1):
                blank_string += ' '

            if working_list[3] == 'out':
                print("{} - {} ({}){}\t\t\t= ${:.2f}".format(counter_main, working_list[0], working_list[1], blank_string, float(working_list[2])))

            counter_main += 1
            blank_string = ' '
    ##print only available Items
    elif print_option == 3:
        for i in printable_list:
            working_list = printable_list[counter_main]
            spacing_length = 40 - (len(working_list[0] + working_list[1]))

            for i in range(1, spacing_length, 1):
                blank_string += ' '

            if working_list[3] == 'in':
                print("{} - {} ({}){}\t\t\t= ${:.2f}".format(counter_main, working_list[0], working_list[1], blank_string, float(working_list[2])))

            counter_main += 1
            blank_string = ' '


def hire_item(list_of_items):

    new_list_of_items = list_of_items
    length_of_list = len(list_of_items)
    error_marker = 0
    while error_marker == 0:
        try:
            choice = int(input("Enter the number of an item to hire "))
            error_marker = 1
        except ValueError:
            print("Invalid input, enter a valid number")
            error_marker = 0

    while (choice > length_of_list) or (choice < 0):
        error_marker3 = 0
        while error_marker3 == 0:
            try:
                choice = int(input("Enter the number of an item to hire: "))
                error_marker3 = 1
            except ValueError:
                print("Invalid input, enter a number")
                error_marker3 = 0

    checked_item = list_of_items[choice]
    while (checked_item[3]) != 'in':
        print("That item is not available for hire")
        error_marker2 = 0
        while error_marker2 == 0:
            try:
                choice = int(input("Enter a valid number: "))
                error_marker2 = 1
            except ValueError:
                choice = input("Invalid input, enter a number")
                error_marker2 = 0

        while (choice > length_of_list) or (choice < 0):
            print("Invalid item number: ")
            error_marker4 = 0
            while error_marker4 == 0:
                try:
                    choice = int(input("Enter a valid number: "))
                    error_marker4 = 1
                except ValueError:
                    choice = input("Invalid input, enter a number")
                    error_marker4 = 0

        checked_item = list_of_items[choice]

    print("{} hired for ${}".format(checked_item[0], checked_item[2]))

    checked_item[3] = "out"

    new_list_of_items[choice] = checked_item
    return new_list_of_items


def return_item(list_of_items):
    c
    new_list_of_items = list_of_items
    length_of_list = len(list_of_items)
    error_marker = 0
    while error_marker == 0:
        try:
            choice = int(input("Enter the number of an item to return: "))
            error_marker = 1
        except ValueError:
            print("Invalid input, enter a number")
            error_marker = 0

    while (choice > length_of_list) or (choice < 0):
        error_marker3 = 0
        while error_marker3 == 0:
            try:
                choice = int(input("Invalid item number: "))
                error_marker3 = 1
            except ValueError:
                print("Invalid input, enter a valid number")
                error_marker3 = 0

    checked_item = list_of_items[choice]
    while (checked_item[3]) != 'out':
        print("That item is not on hire")
        error_marker2 = 0
        while error_marker2 == 0:
            try:
                choice = int(input("Enter a valid number: "))
                error_marker2 = 1
            except ValueError:
                choice = input("Invalid input, enter a number")
                error_marker2 = 0

        while (choice > length_of_list) or (choice < 0):
            print("Invalid item number: ")
            error_marker4 = 0
            while error_marker4 == 0:
                try:
                    choice = int(input("Enter a valid number: "))
                    error_marker4 = 1
                except ValueError:
                    choice = input("Invalid input, enter a number")
                    error_marker4 = 0

        checked_item = list_of_items[choice]

    print("{} returned".format(checked_item[0]))

    checked_item[3] = "in"

    new_list_of_items[choice] = checked_item
    return new_list_of_items


def add_new_item(list_of_items):

    amended_list_of_items = list_of_items

    new_item_name = input("Item name ")
    while new_item_name == "":
        new_item_name = input("Input cannot be blank.")

    new_item_description = input("Description ")
    while new_item_description == "":
        new_item_description = input("Input cannot be blank.")

    error_marker = 0
    while error_marker == 0:
        try:
            new_item_price = float(input("Price per day "))
            error_marker = 1
        except ValueError:
            print("Invalid input, enter a valid number")
            error_marker = 0

        if new_item_price < 0:
            print("Price must be >= $0")
            error_marker = 0

    new_item_availability = "in"

    new_item_list = []
    new_item_list.append(new_item_name)
    new_item_list.append(new_item_description)
    new_item_list.append(new_item_price)
    new_item_list.append(new_item_availability)

    amended_list_of_items.append(new_item_list)
    print("{} {}, {:.2f} now available for hire".format(new_item_name, new_item_description, new_item_price))
    return amended_list_of_items


def check_item_status(items_list_to_check_availability, in_or_out_string):

    counter = 0
    list_check_boolean = 0
    for i in items_list_to_check_availability:
        working_list = items_list_to_check_availability[counter]
        if working_list[3] == in_or_out_string:
            list_check_boolean = 1

        counter += 1

    return(list_check_boolean)


#main(FILE_NAME)