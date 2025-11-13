from collections import UserDict #importing UserDict for AddressBook implementation


class Field: #basic field class
    def __init__(self, value):
        self.value = value 

    def __str__(self):  #string representation of the field
        return str(self.value)

class Name(Field): #child class for Name field from Field
		pass

class Phone(Field): #child class for Phone field from Field
        def __init__(self, value): 
              if not value.isdigit() or len(value) != 10: #check the phone number validity
                    raise ValueError("Phone number must be exactly 10 digits and contain only numbers.")
              super().__init__(value) #calling parent constructor


#initializing Record with Name and empty phone list
class Record:
    def __init__(self, name): 
        self.name = Name(name) #storing name as Name field
        self.phones = [] #list to store Phone fields

    #string representation of the Record
    def __str__(self): #string representation of the Record
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    #method to add phone number
    def add_phone(self, phone_number): 
        phone = Phone(phone_number) #creating Phone field
        self.phones.append(phone) #adding to phones list

    #method to remove phone number
    def remove_phone(self, phone_number): 
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return
        raise ValueError("Phone number not found.")
    
    #method to edit phone number
    def edit_phone(self, old_number, new_number): 
        for i, phone in enumerate(self.phones): #iterating through phones with index
            if phone.value == old_number:  
                self.phones[i] = Phone(new_number) 
                return
        raise ValueError("Old phone number not found.") #raise error if not found
    
    #method to find phone number
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
 
# AddressBook class with methods to add, find, and delete records
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record  #adding record to AddressBook using name as key
    def find(self, name):
        return self.data.get(name)  #finding record by name
    def delete(self, name):
        if name in self.data:
            del self.data[name]  #deleting record by name
        else:
             pass


if __name__ == "__main__":    
    book = AddressBook()
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    
    book.add_record(john_record)

    
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    
    for name, record in book.data.items():
        print(record)

    
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  

   
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  


    book.delete("Jane")
