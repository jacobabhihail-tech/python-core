#project : Mini Address-Book Program 

address_book = {}

#Function to Add Contact


def add_contact(book, contact_id, name, phone, city=""):
    book[contact_id] = {
        "name": name,
        "phone": phone,
        "city": city
    }

def show_contact(book, contact_id):
    if contact_id in book:
        print(book[contact_id])
    else:
        print("Contact not found")

def delete_contact(book, contact_id):
    if contact_id in book:
        del book[contact_id]
        print("Contact has been deleted.")
    else:
        print("Contact not found")

def update_contact(book, contact_id, key, value):
    if contact_id in book:
        book[contact_id][key] = value
        print("Contact updated successfully")
    else:
        print("contact not found")

#Functions create entering data into address book

print("\n*********Welcome to python address book*************\n")

# adding data to the address book
add_contact(address_book, "c1", "Ashu", "888888", "Dubai")
add_contact(address_book, "c2", "Ravi", "999999", "Bangalore")

#showing contact
show_contact(address_book, "c1")

#If contact does not exist
show_contact(address_book, "c3")

#Update a contact
show_contact(address_book, "c2")
update_contact(address_book,"c2", "city", "Mumbai")
show_contact(address_book, "c2")

#Delete a contact
print(address_book)

show_contact(address_book, "c1")
delete_contact(address_book,"c1")

print(address_book)