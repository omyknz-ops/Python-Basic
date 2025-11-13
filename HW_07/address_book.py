from collections import UserDict
from datetime import datetime, date, timedelta


class Field:
    """Base class for record fields."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Class for storing contact name."""
    pass


class Phone(Field):
    """Class for storing phone number with validation."""

    @staticmethod
    def is_valid(phone_number):
        """Check if phone number is valid."""
        return phone_number.isdigit() and len(phone_number) == 10

    def __init__(self, value):
        if not Phone.is_valid(value):
            raise ValueError(
                "Phone number must be exactly 10 digits."
            )
        super().__init__(value)


class Birthday(Field):
    """Class for storing birthday information."""

    DATE_FORMAT = "%d.%m.%Y"

    def __init__(self, value):
        try:
            date_object = datetime.strptime(value, self.DATE_FORMAT)
            super().__init__(date_object)
        except ValueError:
            raise ValueError(f"Invalid date format. Use {self.DATE_FORMAT}")

    def __str__(self):
        """Return formatted date string."""
        return self.value.strftime(self.DATE_FORMAT)


class Record:
    """Class for storing contact information."""

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones)
        birthday_str = (
            f", birthday: {self.birthday}" if self.birthday else ""
        )
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones_str}{birthday_str}"
        )

    def add_phone(self, phone_number):
        """Add phone number to contact."""
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        """Remove phone number from contact."""
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError("Phone number not found.")

    def edit_phone(self, old_number, new_number):
        """Edit existing phone number."""
        if self.find_phone(old_number):
            new_phone = Phone(new_number)
            self.remove_phone(old_number)
            self.add_phone(new_phone.value)
        else:
            raise ValueError("Old phone number not found.")

    def find_phone(self, phone_number):
        """Find phone number in contact."""
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_birthday(self, birthday_str):
        """Add birthday to contact."""
        self.birthday = Birthday(birthday_str)

    def show_birthday(self):
        """Show birthday of the contact."""
        if self.birthday:
            return str(self.birthday)
        return "Birthday not set"


class AddressBook(UserDict):
    """Class for storing and managing records."""

    def add_record(self, record):
        """Add record to address book."""
        self.data[record.name.value] = record

    def find(self, name):
        """Find record by name."""
        return self.data.get(name)

    def delete(self, name):
        """Delete record by name."""
        if name in self.data:
            del self.data[name]

    def _adjust_for_weekend(self, birthday_date):
        """Adjust congratulation date if birthday falls on weekend."""
        weekday = birthday_date.weekday()

        if weekday == 5:  # Saturday
            return birthday_date + timedelta(days=2)
        elif weekday == 6:  # Sunday
            return birthday_date + timedelta(days=1)
        else:
            return birthday_date

    def get_upcoming_birthdays(self):
        """Get contacts with birthdays in the next 7 days."""
        today = date.today()
        result = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            name = record.name.value
            birthday_date = record.birthday.value.date()

            birthday_this_year = birthday_date.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(
                    year=today.year + 1
                )

            days_until_birthday = (birthday_this_year - today).days

            if 0 <= days_until_birthday <= 7:
                congratulation_date = self._adjust_for_weekend(
                    birthday_this_year
                )

                result.append({
                    'name': name,
                    'congratulation_date': congratulation_date.strftime(
                        Birthday.DATE_FORMAT
                    )
                })

        return result