# 📒 Address Book Bot

A console assistant bot for managing contacts with data persistence between sessions.

## 📋 Description

This is a console application for managing an address book. The bot allows you to:
- ➕ Add and edit contacts
- 📞 Store multiple phone numbers for one contact
- 🎂 Add birthdays
- 🔔 View upcoming birthdays (next 7 days)
- 💾 **Automatically save data** on exit and load on startup

## 🗂️ Project Structure

```
project/
├── address_book.py      # Classes for data storage
├── main.py              # Main application with commands
├── README.md            # Project documentation
└── addressbook.pkl      # Data file (created automatically)
```

## 🚀 Installation and Launch

### Requirements
- Python 3.7 or higher

### Launch
```bash
python main.py
```

## 📖 Available Commands

| Command | Format | Description |
|---------|--------|-------------|
| `hello` | `hello` | Greeting |
| `add` | `add [name] [phone]` | Add new contact or add phone to existing |
| `change` | `change [name] [old_phone] [new_phone]` | Change phone number |
| `phone` | `phone [name]` | Show contact's phones |
| `all` | `all` | Show all contacts |
| `add-birthday` | `add-birthday [name] [date]` | Add birthday (format: DD.MM.YYYY) |
| `show-birthday` | `show-birthday [name]` | Show contact's birthday |
| `birthdays` | `birthdays` | Show upcoming birthdays (next 7 days) |
| `close` / `exit` | `close` or `exit` | Exit (with auto-save) |

## 💡 Usage Examples

```bash
# Start the bot
Welcome to the assistant bot!

# Add contacts
Enter a command: add John 1234567890
Contact added.

Enter a command: add Alice 0987654321
Contact added.

# Add birthday
Enter a command: add-birthday John 15.05.1990
Birthday added.

# View all contacts
Enter a command: all
Contact name: John, phones: 1234567890, birthday: 15.05.1990
Contact name: Alice, phones: 0987654321

# View upcoming birthdays
Enter a command: birthdays
John: 15.05.2025

# Change phone
Enter a command: change John 1234567890 1111111111
Contact updated.

# Exit with auto-save
Enter a command: exit
Good bye!
```

## 🔧 Technical Details

### Data Persistence
- Uses **pickle** protocol for serialization/deserialization
- Data is automatically saved to `addressbook.pkl` file on exit
- Data is automatically loaded from file on startup
- If file doesn't exist on first launch, creates new empty address book

### Phone Validation
- Phone number must contain exactly **10 digits**
- Only digits are allowed

### Birthday Format
- Format: **DD.MM.YYYY** (e.g., 25.12.1990)
- Invalid format will show error message

### Weekend Birthday Handling
- If birthday falls on Saturday → congratulation moves to Monday
- If birthday falls on Sunday → congratulation moves to Monday

## 📁 Classes

### `Field`
Base class for record fields.

### `Name(Field)`
Stores contact name.

### `Phone(Field)`
Stores phone number with validation (10 digits).

### `Birthday(Field)`
Stores birthday with date format validation (DD.MM.YYYY).

### `Record`
Stores complete contact information (name, phones, birthday).

**Methods:**
- `add_phone(phone)` - add phone number
- `remove_phone(phone)` - remove phone number
- `edit_phone(old_phone, new_phone)` - edit phone number
- `find_phone(phone)` - find phone number
- `add_birthday(date)` - add birthday
- `show_birthday()` - show birthday

### `AddressBook(UserDict)`
Stores and manages all records.

**Methods:**
- `add_record(record)` - add record to book
- `find(name)` - find record by name
- `delete(name)` - delete record by name
- `get_upcoming_birthdays()` - get list of upcoming birthdays (next 7 days)

## 🎯 Features

✅ Object-oriented architecture  
✅ Input validation  
✅ Error handling with decorators  
✅ Data persistence between sessions  
✅ Birthday reminders  
✅ Weekend handling for birthdays  
✅ Clean console interface  

## 📝 Notes

- All data is stored locally in `addressbook.pkl` file
- File is created automatically on first exit
- Data persists between program restarts
- Phone numbers must be exactly 10 digits
- Date format for birthdays: DD.MM.YYYY

## 👨‍💻 Author

Homework assignment - Python course

## 📄 License

Educational project