import abc
import re


class Person:
    __id = 0
    list_phone = []
    address = []

    @staticmethod
    def generatId(self):
        self.__id += 1

    @staticmethod
    def validEmail(email):
        fields = email.split("@")
        if len(fields) != 2:
            return False
        else:
            regex = '[a-z0-9]+'
            if re.search(regex, fields[0]):
                if fields[1].endswith(".hwltd.com"):
                    return True
        return False

    def __init__(self, last_name, first_name, year_of_birth, email, phones, address):
        # Generating id
        self.generatId(self)

        # First and last name must not be empty
        if len(first_name) != 0 and len(last_name) != 0:
            self.__name = first_name
            self.__lastName = last_name
        else:
            print("the first or last name is empty")
            exit(1)

        self.yearOfBirth = year_of_birth

        if self.validEmail(email):
            self.__email = email
        else:
            print("Invalid Email")
            return Exception("Invalid Email")

        self.list_phone = phones
        self.address = address

    def removePhone(self, phone_number):
        if phone_number in self.list_phone:
            self.list_phone.remove(phone_number)
        else:
            print("Not present")
            exit(1)

    def addPhone(self, phone_number):
        if phone_number in self.list_phone:
            print("The number is exists")
            exit(1)
        else:
            self.list_phone.append(phone_number)

    def editAddress(self, address):
        self.address = address


class Phone:
    def __init__(self, phone_number):
        # regex = '[+]?[[0-9]+[-]?[0-9]+]*'
        if len(phone_number) > 0:
            for index in range(len(phone_number)):
                if (index != 0 and phone_number[0] == "+") or (
                        "0" > phone_number[index] > "9"):
                    print("The phone number is illegal")
                    break
            self.phone_number = phone_number
        else:
            print("The phone number is illegal")


class Address:
    def __init__(self, country, city):
        if len(country) != 0 and len(city) != 0:
            self._country = country
            self._city = city

    def getAddress(self):
        return "Country: " + self._country + ",City: " + self._city + "."


class StreetAddress(Address):
    def __init__(self, country, city, street_name, house_number):
        super().__init__(country, city)
        self.street_name = street_name
        self.house_number = house_number

    @abc.abstractmethod
    def getAddress(self):
        try:
            return "Street Number: " + self.street_name + ",Street Number: " + self.house_number + "."
        except:
            raise NotImplementedError()


class PobAddrees(Address):
    def __init__(self, country, city, box_number):
        super().__init__(country, city)
        self.box_number = box_number

    @abc.abstractmethod
    def getAddress(self):
        try:
            return "Post Office Box Number: " + self.box_number + "."
        except:
            raise NotImplementedError()
