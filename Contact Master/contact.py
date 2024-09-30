import csv 
import os

# function for adding a contact
def add(contacts):
    saveed_numbers=contacts
    name = input("Enter Contact Name: ") # input takes input values through run time
    phone = int(input("Enter Phone Number: ")) # int(input) case conversion
    email = input("Enter Email Address: ")
    place= input("Enter place if any: ")
    contacts.append({'name': name, 'phone': phone, 'email': email,'place':place})

#function for saveing contacts
def save(fname, contacts):
    with open(fname, mode='w', newline='') as file: # filehandling using write operation
        fields = ['name', 'phone', 'email','place']
        writer = csv.DictWriter(file, fields=fields)
        writer.writeheader()
        writer.writerows(contacts)
#function for delete contacts
def delete(contacts):
    name= input("Enter name to delete: ")
    contacts[::] = [contact for contact in contacts if contact['name'] != name] # List comphrension
    
def search(contacts):
    query = input("Enter name to search for: ")
    results = [contact for contact in contacts if query.upper() in contact['name'].upper()]
    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Place: {contact['place']}")  
    else:
        print("No contacts found.")

def load_contacts(fname):
    contacts = []
    if os.path.exists(fname):# it checks the file is present or not
        with open(fname, mode='r', newline='') as file:# using filehandling method read operation
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    return contacts # return bring control flow from functional space to main space
# function for adding a contact

def main():
    fname = 'contacts.csv'
    contacts = load_contacts(fname)

    while True:
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contacts")
        print("4. Exit")
        enter_choice = input("Enter your choice: ") #user can enter there choice which action should be done

        if enter_choice == '1':
            add(contacts)
            print("Contact Added")
        elif enter_choice == '2':
            delete(contacts)
            print("Contact Deleted")
        elif enter_choice == '3':
            search(contacts)
        elif enter_choice == '4':
            save(filename, contacts)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
