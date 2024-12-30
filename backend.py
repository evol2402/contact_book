import csv
from email_validator import validate_email, EmailNotValidError

# File to store contacts
CONTACTS_FILE = 'contacts.csv'

# Load contacts from the CSV file
def load_contacts():
    contacts = []
    try:
        with open(CONTACTS_FILE, mode='r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass
    return contacts

# Save contacts to the CSV file
def save_contacts(contacts):
    with open(CONTACTS_FILE, mode='w', newline='') as f:
        fieldnames = ['name', 'phone', 'email', 'address']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

# Function to validate email
def is_valid_email(email):
    try:
        # This will check if the email is valid
        validate_email(email)
        return True
    except EmailNotValidError as e:
        print(f"Invalid email: {e}")
        return False

# Add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    # Validate email
    email = input("Enter email: ")
    while not is_valid_email(email):  # Keep asking until a valid email is provided
        email = input("Enter a valid email: ")

    address = input("Enter address: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")


# View all contacts
def view_contacts():
    contacts = load_contacts()
    if contacts:
        print("\nContact List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts found.")

# Search contacts by name or phone
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    contacts = load_contacts()
    found_contacts = [contact for contact in contacts if
                      search_term in contact['name'] or search_term in contact['phone']]

    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No matching contacts found.")

# Update an existing contact
def update_contact():
    name_to_update = input("Enter the name of the contact to update: ")
    contacts = load_contacts()

    for contact in contacts:
        if contact['name'].lower() == name_to_update.lower():
            print("Contact found!")
            contact['phone'] = input(f"Enter new phone number (current: {contact['phone']}): ")
            contact['email'] = input(f"Enter new email (current: {contact['email']}): ")
            contact['address'] = input(f"Enter new address (current: {contact['address']}): ")
            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found.")

# Delete a contact
def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()

    contacts = [contact for contact in contacts if contact['name'].lower() != name_to_delete.lower()]
    save_contacts(contacts)
    print("Contact deleted successfully.")
