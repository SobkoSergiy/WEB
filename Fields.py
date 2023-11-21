from datetime import datetime
import re
# from ShowFields import ShowAddress, ShowBirthday, ShowEmail, ShowPhone, ShowName

class ShowField:
    def show_field(self, value):
        raise NotImplemented("ShowField.show_field") #pass

class ShowAddress(ShowField):
    def show_field(self, value):
        return 'address:' + str(value)

class ShowBirthday(ShowField):
    def show_field(self, value):
        return 'birthday:' + str(value)
    
class ShowEmail(ShowField):
    def show_field(self, value):
        return 'email:' + str(value)

class ShowName(ShowField):
    def show_field(self, value):
        return 'name:' + str(value)   
        
class ShowPhone(ShowName):
    def show_field(self, value):
        return f"phone: ({self.value[0:3]}){self.value[3:6]}-{self.value[6:]}"
   


class Field:
    def __init__(self):
        self.__value = ""
        self.show = ShowField()

    def __str__(self):
        return self.show.show_field(self.value)
        # return str(self.value)

    def __eq__(self, other):
        value = other.value if isinstance(other, Field) else other
        return self.value == value
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, newvalue): 
        self.validate(newvalue)
        self.__value = newvalue
    
    def validate(self, newvalue):
        raise NotImplemented("Field.validate") #pass


class Address(Field):
    def validate(self, newvalue):
        if newvalue != "" and (newvalue.isalnum()):
            raise ValueError(f"ERROR: invalid letters in the address '{newvalue}'")


class Birthday(Field):
    def validate(self, newvalue): 
        if newvalue:
            try:
                bd = datetime.strptime(newvalue, '%d-%m-%Y')
            except ValueError:
                raise ValueError(f"ERROR: date of birth '{newvalue}' is wrong")
            today = datetime.today()
            if bd > today:
                raise ValueError(f"ERROR: date of birth '{newvalue}' in the future")
            if (today.year - bd.year) > 120:
                raise ValueError(f"ERROR: date of birth '{newvalue}' is very ancient")
            

class Email(Field):
    def validate(self, newvalue):
        if newvalue:
            pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
            # pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
            if re.match(pattern, newvalue) is None:
                raise ValueError(f"ERROR: invalid e-mail name: '{newvalue}'")


class Name(Field):
    def __init__(self, value):
        super().__init__()
        self.__value = None
        self.value = value    
        
    def validate(self, newvalue):
        if (len(newvalue) <=2) or (len(newvalue) >=12):
            raise ValueError(f"ERROR: Name '{newvalue}' shoud be from 3 to 12 letters")
        if not newvalue.isalpha():
            raise ValueError(f"ERROR: invalid letters in the name '{newvalue}'")

class Phone(Name):
    def __str__(self):
        return f"({self.value[0:3]}){self.value[3:6]}-{self.value[6:]}"

    def validate(self, newvalue):
        if len(newvalue) != 10:
            raise ValueError(f"ERROR: phone number '{newvalue}' must be 10 digits long")
        if not newvalue.isnumeric():
            raise ValueError(f"ERROR: phone number '{newvalue}' contains invalid characters")


if __name__ == '__main__':

    def main_modul():
        print("\n\n>>> Домашнє завдання №1: створення класу ShowField")
        address = Address()
        address.value = "49000 м.Дніпро, вул.Коцюбинського 12/34"    
        address.show = ShowAddress()    
        print(address)
        bday = Birthday()
        bday.value = "12-07-2002"    
        bday.show = ShowBirthday()    
        print(bday)
        email = Email()
        email.value = "exam.email@gmail.com"    
        email.show = ShowEmail()    
        print(email)
        name = Name("Personname")
        name.show = ShowName()    
        print(name)
        phone = Phone("0671234567")
        phone.show = ShowPhone()    
        print(phone)

    main_modul()
