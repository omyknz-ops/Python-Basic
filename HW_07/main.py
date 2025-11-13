# Create a bot working together with Address Book file
from address_book import AddressBook, Record


def input_error(func):
    """Error handling decorator."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AttributeError:
            return "Contact not found."
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
    return wrapper


def parse_input(user_input):
    """Command parser."""
    if not user_input or not user_input.strip():
        return None, []
    cmd, *args = user_input.strip().split()
    cmd = cmd.lower()
    return cmd, args


@input_error
def add_contact(args, book):
    """Add or update a contact."""
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    """Change phone number for existing contact."""
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phone(args, book):
    """Show phone numbers for a contact."""
    name, *_ = args
    record = book.find(name)
    phones = '; '.join([p.value for p in record.phones])
    return phones if phones else "No phones saved."


def show_all(book):
    """Show all contacts."""
    if not book.data:
        return "No contacts saved."
    result = []
    for record in book.data.values():
        result.append(str(record))
    return '\n'.join(result)


@input_error
def add_birthday(args, book):
    """Add birthday to a contact."""
    name, birthday, *_ = args
    record = book.find(name)
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args, book):
    """Show birthday for a contact."""
    name, *_ = args
    record = book.find(name)
    return record.show_birthday()


@input_error
def birthdays(args, book):
    """Show upcoming birthdays in the next 7 days."""
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays in the next 7 days."
    result = []
    for item in upcoming:
        result.append(f"{item['name']}: {item['congratulation_date']}")
    return '\n'.join(result)


def main():
    """Main loop."""
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        if not user_input or not user_input.strip():
            print("Please enter a command.")
            continue

        command, args = parse_input(user_input)

        if command is None:
            print("Please enter a command.")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()