# task_4_4.py
# A simple command-line assistant bot to manage contacts.
def parse_input(user_input): # Parses user input into command and arguments.
    cmd, *args = user_input.split() # Split input into command and arguments
    cmd = cmd.strip().lower() # Normalize command to lowercase
    return cmd, *args # Return command and arguments

# Command functions
def add_contact(args, contacts): # Adds a new contact
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts): # Changes an existing contact's phone number
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found." # Error message if contact doesn't exist

def show_phone(args, contacts): # Shows the phone number of a contact
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts): # Shows all contacts
    if contacts:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "No contacts saved."

def main(): # Main function to run the assistant bot
    contacts = {} # Dictionary to store contacts
    print("Welcome to the assistant bot!")
    while True: # Main loop
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input) # Parse user input

        if command in ["close", "exit"]: # Exit commands
            print("Good bye!")
            break
        elif command == "hello": # Greeting command
            print("How can I help you?")
        elif command == "add": # Add contact command
            print(add_contact(args, contacts)) 
        elif command == "change": # Change contact command
            print(change_contact(args, contacts))
        elif command == "phone": # Show phone command
            print(show_phone(args, contacts))
        elif command == "all": # Show all contacts command
            print(show_all(contacts))
        else: # Invalid command
            print("Invalid command.")

if __name__ == "__main__": # Run the main function
    main() 
