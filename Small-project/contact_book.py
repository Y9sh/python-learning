#Mini Contact Book 
#Recap 2/7/2025
#self make
contact = []
def title():
    banner= '''Contact  Book'''
    print(banner)
    

def add_contact(name, phone,email):
    
    contact.append(
        {"name":name, 
         "phone": phone, 
         "email" : email}
        )
    return contact

def display_contact():
    for display in contact:
        print(f"Name: {display["name"]}\nPhone: {display["phone"]}\nEmail: {display["email"]}")
        if len(contact) >1 :
            print("--------")
    

def main_menu():
     
    while True: 
        print("1.Add contact")
        print("2.See all contact")
        print("3.Exit")
        
        choose = int(input("Choose your path: "))
        if choose == 1 :
            print("--------")
            add_contact(name=input("Input name contact: "), phone=int(input("Input number phone: ")), email=input("Input email contact: "))
        elif choose ==2 : 
            print("--------")
            display_contact()
            print("--------")
        elif choose == 3 :
            print("--------")
            print("Goodbye See You Again~~~")
            break
        else: 
            print("--------")
            print(f"Invalid path {choose}. Try again and refer the main menu.")
            print("--------")
title()
main_menu()
#(add_contact("nyra","0112300533","nyra@gmail.com"))
#display_contact()

'''
Futher improvement or suggestions: 

🔧 1. Convert phone input to string.
--
phone=input("Input number phone: ")
---
Because phone numbers may start with zero and aren’t used for calculation.

'''

# ai refine 
# Define a global list to store all contacts
contacts = []

def add_contact(name, phone, email):
    # Return a contact dictionary
    return {"name": name, "phone": phone, "email": email}

def store_contact(contact, contact_list):
    # Append contact into the given contact_list (here: contacts)
    contact_list.append(contact)

def display_contact(contact_list):
    # Loop through each contact in contact_list
    for display in contact_list:
        print(f"Name: {display['name']}\nPhone: {display['phone']}\nEmail: {display['email']}")
        print("--------")

def main_menu():
    while True:
        print("1. Add contact")
        print("2. See all contacts")
        print("3. Exit")
        
        choose = int(input("Choose your path: "))
        if choose == 1:
            name = input("Input name: ")
            phone = input("Input phone: ")
            email = input("Input email: ")
            
            # Create new contact dict using add_contact()
            new_contact = add_contact(name, phone, email)
            
            # Store contact into global contacts list using store_contact()
            store_contact(new_contact, contacts)
        
        elif choose == 2:
            display_contact(contacts)
        
        elif choose == 3:
            print("Goodbye See You Again~~~")
            break
        else:
            print(f"Invalid choice {choose}. Try again.")

# Pipeline to start the program
main_menu()


