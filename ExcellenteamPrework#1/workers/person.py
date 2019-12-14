import re

class Person():
    ID = 1
    def __init__(self,fname,lname, yob, email,phone):
        self.ID = Person.ID
        Person.ID += 1
        if not fname:
            raise ValueError('first name is empty ')
        if not lname:
            raise ValueError('last name is empty')
        self.FirstName = fname
        self.LastName = lname
        self.YearOfBirth = yob
        if Person.validateEmail(email):
            self.email = email
        phone = Phone.validatePhone(phone)
        address = ""

    @staticmethod
    def validateEmail(email):
        regex = '^([a-z\d]+)@([a-z\.]+)(\.hwltd.com)$'
        if not email:
            raise ValueError('email is empty')
        if (re.search(regex, email)):
            print("Valid Email")
        else:
            print("Invalid Email")
        return True

class Phone():
    def __init__(self, phone):
        if Phone.validatePhone(phone):
            self.phone = phone

    @staticmethod
    def validatePhone(phone):
        regex1 = '^[+][(]{0,1}[0-9]{1,3}[)]{0,1}-[0-9]{2}-[0-9]{3}-[0-9]{4}%'
        regex2 = '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        if (re.search(regex1, phone) or re.search(regex2, phone)):
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number")
        return True

#phone1 = Phone("054-233-2222")


person1 = Person("x","y",1990,"jake@japan.hwltd.com","054-233-2222")

#print(person1.ID)
#person2 = Person("x","y",1990,"jake@japan.asia.hr.hwltd.com")
#print(person2.ID)