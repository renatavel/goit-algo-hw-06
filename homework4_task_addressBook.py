from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass        

class Phone(Field):
    def __init__(self, value):
        if self.validate_number(value):
            super().__init__(value)
        else:
            raise ValueError("Your phone should be consisted of 10 digits.")

    def validate_number(self, phone):
        return len(phone) == 10 and phone.isdigit()
                         
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if phone not in [phone.value for phone in self.phones]:
            self.phones.append(Phone(phone))
        else:
            print("The phone is already on the list.")    

    def remove_phone(self, phone):
        phone_to_remove = None
        for p in self.phones:
            if p.value == phone:
                phone_to_remove = p
                break

        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:        
            print("The phone does not exist in the list.")

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = None
        for phone in self.phones:
            if phone.value == old_phone:
                phone_to_edit = phone
                break

        if not phone_to_edit:
            raise ValueError("The old phone number does not exist in the list.")
        
        if not Phone(new_phone).validate_number(new_phone):
            raise ValueError("The new phone number is invalid. It must be 10 digits.")
        
       
        phone_to_edit.value = new_phone

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record
        return self.data
    
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"No contact with name {name} has been found.")    
            
    def __str__(self):
        return "\n".join(f"{name}: {record}" for name, record in self.data.items())             


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")

book.add_record(jane_record)
print(book)

john = book.find("John")
if john:
    john.edit_phone("1234567890", "1112223333")

print(book)

found_phone = john.find_phone("5555555555")
print(f"\nPhone found in John's contact: {found_phone}")

book.delete("Jane")
print(book)