golf=7
thermo=6
def add():     #this is the add function created over here
    name = input("Item name          : ")    #getting the name
    description = input("description        : ")   #getting the description
    prize=input("prize              : ")    #getting the prize
    while len(name) <=0:
     print("Item name cannot be null")

    items = open("test3.csv","a")    #opening the scv file
    x=(name,description,prize)

    print(x, file=items)    #saving the input value into the csv file
    print("Your Items are Added")
    count=1
    items.close()

def list():

 f = open("test3.csv", "r")   #displaying the content from the  csv file

# Loop over each line in the file.
 for line in f.readlines():   #adding loop over here to read all lines in the csv file

    # Strip the line to remove whitespace.
    lines = line.strip()
    # Display the line.
    print(lines)

def hire():

        list()     #displaying the content in the define function
        select=input("Select an item:")  #getting the input over here



        if select =='0': #if the input value is 0  the whole code will run
                     rusty=5
                     rusty=rusty-1

                     print("Rusty bucket is selected (40L bucket - quite rusty)    = $   0.00 ")
                     print("The Remaining Rusty Bucket In The Cart Is ",rusty)
                     while rusty!=0:  # if there is no item in the cart it will break the functiom
                      print("There Is No More Rusty Buckets In The Cart" )
                      break




        elif select == '1':
            print("Golf is selected (Tesla powered 250 turbo)             = $ 195.00 ")
        elif select == '2':
            print("Thermomix is selected (TM-31)                          = $  25.50 ")


        else:
            print("invalid input")

def ret():   #creating the function for returning the item
    list()   # displaying the content in the list
    print ("from this which you want to return:")
    return_product=input("enter an item which you want to return : ")
    if return_product =="0": # if this statement is 0 which execute the below string
        print("rusty bucket is returned")
    elif return_product =="1":   # if this statement is 1 which execute the below string
        print("Golf is selected (Tesla powered 250 turbo) is returned")
    elif return_product =="2":   # if this statement is 2 which execute the below string
        print("Thermomix is selected (TM-31) is returned")   # if this statement is 0 which execute the below string
    elif return_product =="3":    # if this statement is 3 which execute the below string
        print("AeroPress (The great coffee maker) is returned")

def main(): # this is the main function
    print("Items for Hire -By Manoj Kumar")
    print("""Menu:
    (L)List An Item
    (H)Hire An Item
    (R)Return An Item
    (A)Add New Item
    (Q)Quit""")
    choice=str(input("Select your choice: ")) #getting the input value from the user to ask their option
    if choice=='l': # if the option is l it will go to the function called list()
            list()
    elif choice=='h':# if the option is h it will go to the function called hire()

          hire()
    elif choice=='a':# if the option is a it will go to the function called add()
        add()
    elif choice=='r':# if the option is r it will go to the function called ret()
        ret()
    elif choice=='q':# if the suer selected the quit option the whole process will stop by a break statement
        print("Thank you...")
        print("please visit again...")

    while choice!='q':

     print("Items for Hire -By Manoj Kumar")
     print("""Menu:
    (L)List An Item
    (H)Hire An Item
    (R)Return An Item
    (A)Add New Item
    (Q)Quit""")
     choice=str(input("Select your choice: ")) #getting the input value from the user to ask their option
     if choice=='l': # if the option is l it will go to the function called list()
            list()
     elif choice=='h':# if the option is h it will go to the function called hire()

          hire()
     elif choice=='a':# if the option is a it will go to the function called add()
        add()
     elif choice=='r':# if the option is r it will go to the function called ret()
        ret()
     elif choice=='q':# if the suer selected the quit option the whole process will stop by a break statement
        print("Thank you...")
        print("please visit again...")

main()