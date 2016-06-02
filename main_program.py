"""
Manojkumar Sadhasivam (13355060)
2 june 2016
This has been created by python and kivy as GUI.
"""

from Item import *
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from Items_in_shop import format_csv_file_data_for_use
from Items_in_shop import format_csv_file_data_to_save


__Author__ = "Manojkumar Sadhasivam"
FILE_NAME = "items.csv"

Imported_Files = open("{}".format(FILE_NAME), mode='r')
Items_To_List = format_csv_file_data_for_use(Imported_Files)
Imported_Files.close()

"""
making a list of Item objects which were not used in this program
"""
List_Of_Item= []
Count = 0
for item in Items_To_List:
    Name= item[0]
    Description  = item[1]
    Prize= item[2]
    Availability = item[3]
    current_item_in_the_cart = Item(Name, Description , Prize, Availability)
    List_Of_Item.append(current_item_in_the_cart)
    Count += 1


def List_Dictionary(list_of_items):

    Items_In_Dicctionary= {}
    for items in list_of_items:
        Name_Of_Items= items[0]
        Details_About_An_Items  = [items[1], items[2], items[3]]
        Items_In_Dicctionary[Name_Of_Items] = Details_About_An_Items

    return Items_In_Dicctionary


def convert_item_dictionary_to_list(item_dictionary):

    list_of_an_items = []
    name_of_an_item= item_dictionary.keys()
    for each_item in name_of_an_item:
        Name_Of_Items= [each_item]
        item_description = item_dictionary[each_item]
        working_item = [Name_Of_Items+ item_description]
        list_of_an_items = list_of_an_items + working_item

    return list_of_an_items


class ItemsForHireApp(App):

    status_text = StringProperty()

    def __init__(self, **kwargs):

        super(ItemsForHireApp, self).__init__(**kwargs)
        self.items_dict = List_Dictionary(Items_To_List)
        self.mode = 0
        self.hiring_list = []
        self.total_hiring_price = 0
        self.items_to_display_string = ""
        self.returning_list = []

    def build(self):
        """
        Which builds the Kivy GUI
        """
        self.title = "Items For Hire"
        self.root = Builder.load_file('user_interface.kv')
        self.create_entry_buttons()
        return self.root

    def create_entry_buttons(self):
        """
        This function is used to create the entry buttons and add them into the GUI

        """
        """
        for each name in items_dict
            create Button with text(current_name)
            set Button to run press_entry function on release
            set Button to run clear_all on press
            generate a widget for the Button
            find the current items data from items_dict
            if working_item(availability) = 'in'
                make Button colour Green
            else if working_item(availability) = 'out'
                make Button colour Red

            make sure that the buttons separate into columns of maximum 5
        """
        for name in self.items_dict:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            temp_button.bind(on_press=self.clear_all)
            self.root.ids.entriesBox.add_widget(temp_button)
            working_item = self.items_dict[name]
            if working_item[2] == 'in':
                temp_button.background_color = (0, 1, 0, 1)
            elif working_item[2] == 'out':
                temp_button.background_color = (1, 0, 0, 1)
            self.root.ids.entriesBox.cols = len(self.items_dict) // 5 + 1

    def press_entry(self, instance):
        """
        This function is used to display the currently stored item buttons
         For instance: color changing while pressing the button
         which denotes where the current action is
        """
        """
        get all details about the current buttons item from items_dict

        if current program Mode = 0 (listing Items)
            display only Items name and details to the status bar

        else if current program Mode = 1 (Hiring Items)
            if current item is available for hire
                if current item has not already been selected
                    add item to the list of items to hire
                    add items price to the total current hire price

                reset the display string
                re-make the display string to include all items currently in the list of items to hire

                print the new formatted list of Items selected for hire to the status bar

        else if current program Mode = 2 (Return Items)
            if current item is out on hire
                if current item has not already been selected
                    add item to the list of items to return

                reset the display string
                re-make the display string to include all items currently in the list of items to return

                print the new formatted list of Items selected for return to the status bar
        """
        name = instance.text
        details = self.items_dict[name]
        description = details[0]
        price = details[1]
        availability = details[2]

        if self.mode == 0:
            self.status_text = "'{}': {} \nPrice: ${}\nAvailability: {}".format(name, description, price, availability)

        elif self.mode == 1:
            if availability == 'in':
                if name not in self.hiring_list:
                    self.hiring_list.append(name)
                    self.total_hiring_price += float(price)
                self.items_to_display_string = ""
                for items in self.hiring_list:
                    self.items_to_display_string += "{}, ".format(items)

                self.status_text = ""
                self.status_text = "Items To Hire\n{}\nPrice: {}".format(self.items_to_display_string,
                                                                         str(self.total_hiring_price))

        elif self.mode == 2:
            if availability == 'out':
                if name not in self.returning_list:
                    self.returning_list.append(name)

                self.items_to_display_string = ""
                for items in self.returning_list:
                    self.items_to_display_string += "{}, ".format(items)

                self.status_text = ""
                self.status_text = "Items To Return\n{}".format(self.items_to_display_string)

        instance.state = 'down'

    def press_clear(self):
        """
        This function executes while pressing the Clear Button
        which clear the content in lable
        """
        """
        reset all buttons in main widget to normal
        status_text = blank string
        hiring_list = blank list
        hiring_price = 0
        items_to_display_string = blank string
        returning_list = blank list
        """
        for instance in self.root.ids.entriesBox.children:
            instance.state = 'normal'
        self.status_text = ""
        self.hiring_list = []
        self.total_hiring_price = 0
        self.items_to_display_string = ""
        self.returning_list = []


    def clear_all(self, instance):
        """
        Function to reset only the Buttons on the widget to their normal states but not reset the data stored.
        This allows us to have only one button selected at a time.
            return None
        """
        for instance in self.root.ids.entriesBox.children:
            if instance.state == 'down':
                instance.state = 'normal'

    def press_list_items(self):
        """
        This function executes while pressing the list_items button
        which show all the data in the csv file
        """
        self.press_clear()
        self.mode = 0

    def press_hire_item(self):
        """
        This function executes while pressing the hire_item button
        which is used to display an items which in the hire category
        """
        self.status_text = "Select Items to Hire Above\nPress 'Confirm' when ready to hire\n" \
                           "Press 'Clear' to restart your selection"
        self.mode = 1

    def press_return_item(self):
        """
        This function is executes while pressing the return_item button
        this function is used for return the item
        """
        self.status_text = "Select Items to Return Above\nPress 'Confirm' when ready to Return\n" \
                           "Press 'Clear' to restart your selection"
        self.mode = 2

    def press_new_item(self):
        """
        This handler is used for add new item while pressing the add_new_item button ID
        """
        self.status_text = "Enter details for the new Item"
        self.root.ids.popup_for_new_item.open()

    def press_save_new_item(self, new_item_name, new_item_description, new_item_price):
        """
        This function will execute while pressing the save button in which it will add entry popup
        """
        """
        Error Check new_item_name for blank string
        Error Check new_item_description for blank string
        Error check new_item_price for numerical float type input
        Error check new_item_price for positive number (input > = 0) input

        create Button with text(new_item_name)
        set Button to run press_entry function on release
        set Button to run clear_all on press
        generate a widget for the Button
        new_item(availability = 'in')
        make Button colour Green
        make sure that the buttons separate into columns of maximum 5

        clear popup entry data
        close popup
        """
        error_marker = 0
        try:
            new_item_price = new_item_price.strip('$')
            check_price = float(new_item_price)

            if check_price < 0:
                error_marker = 1
                new_item_price = "error"
                check_price = float(new_item_price)

            if new_item_name == "":
                error_marker = 2
                new_item_price = "error"
                check_price = float(new_item_price)

            if new_item_description == "":
                error_marker = 3
                new_item_price = "error"
                check_price = float(new_item_price)

            self.items_dict[new_item_name] = [new_item_description, new_item_price, "in"]
            self.root.ids.entriesBox.cols = len(self.items_dict) // 5 + 1
            temp_button = Button(text=new_item_name)
            temp_button.bind(on_release=self.press_entry)
            temp_button.bind(on_press=self.clear_all)
            self.root.ids.entriesBox.add_widget(temp_button)
            temp_button.background_color = (0, 1, 0, 1)
            self.root.ids.popup_for_new_item.dismiss()
            self.clear_fields()
            self.status_text = ""

        except ValueError:
            if error_marker == 0:
                self.status_text = "Incorrect Input: Please Enter a Number"
                self.root.ids.new_item_price.value = ""
                self.root.ids.new_item_price.text = ""
            elif error_marker == 1:
                self.status_text = "Incorrect Input: Price must not be Negative"
                self.root.ids.new_item_price.value = ""
                self.root.ids.new_item_price.text = ""
            elif error_marker == 2:
                self.status_text = "Incorrect Input: Name Cannot Be Blank"

            elif error_marker == 3:
                self.status_text = "Incorrect Input: Description Cannot Be Blank"

            error_marker = 0

    def press_confirm_item(self):
        """
        This function is execute while clicking on confirm button
        which confirms that the user will Hire/Return the currently selected Items
        """
        """
        if current program Mode = 0
            do nothing

        else if current program Mode = 1 (hire Items)
            for each item in hiring_list
                update items_dict availability = 'out'

            for each Button name in hiring_list
                change button colour to Red

            final_price = total_hiring_price
            generate final message to display all items just hired

        else if current program Mode = 2 (return Items)
            for each item in returning_list
                update items_dict availability = 'in'

            for each Button name in hiring_list
                change button colour to Green

            generate final message to display all items just Returned

        change current program Mode to 0 (list items)
        run press_clear()
        display final_message to status bar

        """
        final_message = ""
        if self.mode == 1:
            for i in self.items_dict:
                check_current_item = self.items_dict[i]
                if i in self.hiring_list:
                    check_current_item[2] = 'out'
                    self.items_dict[i] = check_current_item

            for instance in self.root.ids.entriesBox.children:
                print(instance.text)
                if instance.text in self.hiring_list:
                    instance.background_color = (1, 0, 0, 1)

            final_price = float(self.total_hiring_price)
            final_message = "{}\n Hired for: ${}".format(self.items_to_display_string, final_price)

        elif self.mode == 2:
            for i in self.items_dict:
                check_current_item = self.items_dict[i]
                if i in self.returning_list:
                    check_current_item[2] = 'in'
                    self.items_dict[i] = check_current_item

            for instance in self.root.ids.entriesBox.children:
                print(instance.text)
                if instance.text in self.returning_list:
                    instance.background_color = (0, 1, 0, 1)
            final_message = "{}\n returned".format(self.items_to_display_string)

        self.mode = 0
        self.press_clear()
        self.status_text = "{}".format(final_message)

    def press_save(self):
        """
        This function will execute while pressing the save button
         to format the date and saves it to file

        """
        final_list = convert_item_dictionary_to_list(self.items_dict)
        save_file_data = format_csv_file_data_to_save(final_list)
        save_file = open("{}".format(FILE_NAME), mode='w')
        save_file.write(save_file_data)
        save_file.close()
        final_item_count = len(final_list)
        self.status_text = "{} items saved to {}".format(final_item_count, FILE_NAME)

    def clear_fields(self):
        """
        This function is used to Clear the text input fields from the add entry popup
        Clears the fields in the popup window entries

        """
        self.root.ids.new_item_name.text = ""
        self.root.ids.new_item_description.text = ""
        self.root.ids.new_item_price.text = ""

    def press_cancel(self):
        """
        This function is execute while pressing the cancel in the add entry popup
        clears the popup fields and closes the popup

        """
        self.root.ids.popup_for_new_item.dismiss()
        self.clear_fields()
        self.status_text = ""

    def on_stop(self):
        """
        This function is used to save data to file and
        calls the functions which needed to format the date and saves it into the file

        """
        final_list = convert_item_dictionary_to_list(self.items_dict)
        save_file_data = format_csv_file_data_to_save(final_list)
        save_file = open("{}".format(FILE_NAME), mode='w')
        save_file.write(save_file_data)
        save_file.close()
        final_item_count = len(final_list)
        self.status_text = "{} items saved to {}\nHave a nice day :)".format(final_item_count, FILE_NAME)

ItemsForHireApp().run()

