from collections import UserDict

class Field:
    def __init__(self,value):
        self.value=value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass        

class Phone(Field):
    def __init__(self,value):
        if self.validate_number(value):
            super().__init__(value)
        else:
            raise ValueError("Your phone should be consisted of 10 digits.")

    
    def validate_number(self,phone):
        return len(phone)==10 and phone.isdigit()
                         
       
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        if phone not in [phone.value for phone in self.phones]:
            self.phones.append(Phone(phone))
        else:
            print("The phone is already on the list.")    

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value==phone:
                self.phones.remove(phone)
            else:
                print("The phone does not exist in the list.")

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value=new_phone
                return
            else:
                raise ValueError("The old phone number does not exist in the list.")   

    def find_phone(self,phone_number):
        for phone in self.phones:
            if phone.value==phone_number:
                return phone.value 
            else:
                return None
        return None
          
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self,record):
        if record.name.value not in self.data:
            self.data[record.name.value]=record
        return self.data
    
    def find(self,name):
        return self.data.get(name, None)
    
    def delete(self,name):

        if name in self.data:
            del self.data[name]
        else:
            print(f"No contact with name {name} has been found.")    
                 