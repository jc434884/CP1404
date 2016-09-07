count=0

def add():     #this is the add function created over here


    items = open("ass1.csv","a")
    read_items = open("ass1.csv", "r")

    name = str(input("Item name : "))    #getting the name
    price = float(input("prize : "))   #getting the description
    priority=int(input("priority : "))    #getting the prize
    count=0           #opening the scv file
    for every_line in read_items:

             count=count+1

                    # delete the space
             every_line = every_line.strip()

                    # Split the data by "," then store into the dictionary
             eachItem = every_line.split(",")
             x=(count)

    print(x)

    print(("{},{},{},{}".format(x,name,price,priority)), file=items)    #saving the input value into the csv file
    print("Your Items are Added")

    items.close()

def required():#This function is used for display required items

 file_reader = open("ass1.csv", "r")


 for every_line in file_reader:




         every_line = every_line.strip()
                  #which delete the space between the text inside the csv file

         eachItem = every_line.split(",")
                  # which Split the data by "," then store into the dictionary from there we can use by slicing in the list

         product_count=(int(eachItem[0]))
         product_name=(str(eachItem[1]))
         product_price=(float(eachItem[2]))
         product_priority=(str(eachItem[3]))

         csv_to_display="{}-{} ${:.2f}  ({}) added to shopping list".format(product_count,product_name, product_price, product_priority)
         print(csv_to_display)



def compleated():#this function is used to mark an item as compleated
 try:
      file_reader = open("ass1.csv", "r")
      for every_line in file_reader:



                #which delete the space between the text inside the csv file
       every_line = every_line.strip()

                # which Split the data by "," then store into the dictionary from there we can use by slicing in the list
       eachItem = every_line.split(",")


       product_count=(int(eachItem[0]))
       product_name=(str(eachItem[1]))
       product_price=(float(eachItem[2]))
       product_priority=(str(eachItem[3]))

       if eachItem[4]=="c":

         csv_to_display="{}-{} ${:.2f}  ({}) added to shopping list".format(product_count,product_name, product_price, product_priority)

         print(csv_to_display)

 except IndexError:
       print()




def mark():   #this function used to mark an items

#****************************************************************************************************************************
    flagMarked = True  # Label for judge entering
    file_reader = open("ass1.csv", "r")

    count=0

    for every_line in file_reader:

         count=count+1

                #which delete the space between the text inside the csv file
         every_line = every_line.strip()

                # which Split the data by "," then store into the dictionary from there we can use by slicing in the list
         eachItem = every_line.split(",")


         product_count=(int(eachItem[0]))
         product_name=(str(eachItem[1]))
         product_price=(float(eachItem[2]))
         product_priority=(str(eachItem[3]))

         csv_to_display="{}-{} ${:.2f}  ({}) added to shopping list".format(product_count,product_name, product_price, product_priority)

    if len(csv_to_display) == 0:

        print("No required items")
#Till here from the above line which is used to check the length of the list

    # if len(csv_to_display)!=0
    #         it will execute further
    #             else
    #which break the command and shows error message
    else:



      file_reader = open("ass1.csv", "r")



      for every_line in file_reader:



                #which delete the space between the text inside the csv file
         every_line = every_line.strip()

                # which Split the data by "," then store into the dictionary from there we can use by slicing in the list
         eachItem = every_line.split(",")


         product_count=(int(eachItem[0]))
         product_name=(str(eachItem[1]))
         product_price=(float(eachItem[2]))
         product_priority=(str(eachItem[3]))

         csv_to_display="{}-{} ${:.2f}  ({}) added to shopping list".format(product_count,product_name, product_price, product_priority)
         print(csv_to_display)


      while True:

              try:
                 chooseItem = int(input("Enter the number of an item to mark as completed : "))

                 # the index is starts from 0 thats why we use the below statement to check the input value is valid or not
                 if chooseItem < 0 or chooseItem > len(csv_to_display) - 1:
                     print("Invalid item number", end="\n\n")

                 elif product_count==chooseItem:
                     print(chooseItem(product_name))




                     # which ensure an item is marked as compleated
                 print("{} marked as completed".format(product_name))



              except ValueError:
                 print("Invalid input; enter a valid number",end="\n\n")






def main(): # this is the main function

    print("Items for Hire -By Manoj Kumar")
    print("""Menu:
    R - List Required Item
    C - List Compleated Item
    A - Add New Item
    M - Mark An Item As Completed
    Q - Quit""")
    choice=str(input("Select your choice: ")) #getting the input value from the user to ask their option
    if choice=='r': # if the option is l it will go to the function called list()
            required()
    elif choice=='c':# if the option is h it will go to the function called hire()

          compleated()
    elif choice=='a':# if the option is a it will go to the function called add()
        add()
    elif choice=='m':# if the option is r it will go to the function called ret()
        mark()
    elif choice=='q':# if the suer selected the quit option the whole process will stop by a break statement
        print("Thank you...")
        print("please visit again...")
    else:
        print("You have selected a wrong option \n""select correct option once again")
    while choice!='q':

     print("Items for Hire -By Manoj Kumar")
     print("""Menu:
    R - List Required Item
    C - List Compleated Item
    A - Add New Item
    M - Mark An Item As Completed
    Q - Quit""")
     choice=str(input("Select your choice: ")) #getting the input value from the user to ask their option
     if choice=='r': # if the option is l it will go to the function called list()
            required()
     elif choice=='c':# if the option is h it will go to the function called hire()

          compleated()
     elif choice=='a':# if the option is a it will go to the function called add()
        add()
     elif choice=='m':# if the option is r it will go to the function called ret()
        mark()
     elif choice=='q':# if the suer selected the quit option the whole process will stop by a break statement
        print("Thank you...")
        print("please visit again...")
     else:
      print(".......You have selected a wrong option select correct option once again.......")
main()