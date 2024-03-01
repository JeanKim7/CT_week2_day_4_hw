#Exercise 1

def address_bk():
    address_book = {}
    while True:
        user_response = input("Chooose one of the following options for how you would like to change your digital address book!\n(Add/Remove/Check/Quit): ")
        
        #quit function for the program
        if user_response.lower() == "quit":
            #print the address book if they entered some names and addresses
            if address_book:
                print("\nHere are the addresses you entered:\n")
                for name1, address1 in address_book.items():
                    print(f"Name: {name1}\naddress: {address1}\n\n====================================\n")
                print("Thanks for using our service! Hope to see you again!")
                break
            #print message if address book is empty
            else:
                print("\nYour address book is empty. Try adding some addresses next time! Thanks for using our service.\n")
                break

        #adding an address to the address book
        elif user_response.lower() == "add":
            address_name = input("Please enter a name for the address: ")
            #give options if name already exists in address book
            if address_book.get(address_name):
                user_response_override=input("That name already exists!\nIf you would like to override and enter a new address, enter \"Override\".\nIf you would like to enter another name enter \"New Name\" ")
                #override existing address with new address
                if user_response_override.lower() == "override":
                    address = input("Please enter the address: ")
                    address_book[address_name]= address
                    print(f"{address_name}'s address has been changed!\n")
                    continue
                #enter a new name to create a new address
                elif user_response_override.lower() == "new name":
                    address_name = input("Please enter a name for the address: ")
                    #go back to start if they entered existing name
                    if address_book.get(address_name):
                        print("That's not a new name! Please enter a new name next time")
                        continue
                    #enter new address for existing name
                    else:
                        address = input("Please enter the address: ")
                        address_book[address_name]= address
                        print(f"{address_name}'s address has been added!\n")
                        continue
                #go back to start if they didn't enter correct response
                else:
                    print('Please enter "Override" or "New Name" next time!')
                    continue
            #add new address if name doesn't exist
            else:
                address = input("Please enter the address: ")
                address_book[address_name]= address
                print(f"{address_name}'s address has been added!\n")
            continue
        
        #remove an address from the address book
        elif user_response.lower()== "remove":
            address_name_remove = input("Please enter the name for the address you want to remove: ")
            #remove the address if name exists
            if address_book.get(address_name_remove):
                address_book.pop(address_name_remove)
                print (f"{address_name_remove}'s address has been removed!\n")
            #go back to start if name doesn't exist
            else:
                print(f"{address_name_remove} is not in the address book! Please enter an existing name next time.")
                continue
        
        #check to see what names and addresses are in the address book
        elif user_response.lower() == "check":
            #print address book if it's not empty
            if address_book:
                print("Here's what you've entered so far:\n")
                for name1, address1 in address_book.items():
                        print(f"Name: {name1}\naddress: {address1}\n\n====================================\n")
                continue
            #message if address book is empty
            else:
                print("\nThe address book is empty!\n")
                continue
        
        #go back to start if they didn't enter correct response
        else:
            print ("Please type a response of \"Add\", \"Remove\" or \"Quit\".")
            continue

address_bk()



#Exercise 2

person1 = {'09:00', '10:30', '11:30', '12:00', '13:00', '14:30'}
person2 = {'09:30', '10:00', '10:30', '12:00', '14:30', '16:00'}
person3 = {'09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00'}
person4 = {'11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00'}
# Available Times: '12:00' and '14:30'

def available_times(*times):
        list_of_sets = []
        for time in times:
            list_of_sets.append(time)
        available_times_set=list_of_sets[0]
        for i in range(len(list_of_sets)):
            available_times_set = available_times_set.intersection(list_of_sets[i])
        return available_times_set

print(available_times(person1, person2, person3, person4))
