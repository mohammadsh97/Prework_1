from workers.person import Person, Phone, StreetAddress, PobAddrees
from workers.structure import Worker, Engineer, SalesPerson, Team


class Employees:
    dict_of_all_employees = {}

    def add_employees(self, name, email):
        if email in self.dict_of_all_employees.keys():
            raise Exception("the email is already exist")
        else:
            self.dict_of_all_employees[email] = name


class HelloWorld:
    employees = Employees()
    address = []
    flag_correct = True
    counter = 0
    my_list = []

    def __init__(self):
        global worker
        self.f = open("/Users/mohammadSharabati/PycharmProjects/Prework_1/hwltd/prework-python-data.txt", 'r')
        for line in self.f:
            self.counter += 1
            if not (line[0].__eq__("#")) and not (line[0].__eq__("\n")):
                fields = [x.strip() for x in line.split(',')]
                length = len(fields)
                if length == 9 or length == 8:
                    self.phones = []
                    self.last_name = fields[0]
                    self.first_name = fields[1]
                    self.year_of_birth = fields[2]
                    if Person.validEmail(fields[3]):
                        self.email = fields[3]
                    else:
                        self.flag_correct = False

                    if length == 9:
                        if Phone(fields[4].split(";")):
                            self.phones.append(fields[4].split(";"))
                        else:
                            self.flag_correct = False
                        self.address = fields[5].split(";")
                        self.team = fields[6].split(";")
                        self.role = fields[7].split(";")
                        self.data = fields[8].split(";")
                    if length == 8:
                        self.address = fields[4].split(";")
                        self.team = fields[5].split(";")
                        self.role = fields[6].split(";")
                        self.data = fields[7].split(";")

                    if self.flag_correct:

                        if len(self.address).__eq__(4):
                            self.address = StreetAddress(self.address[0], self.address[1], self.address[2],
                                                         self.address[3])

                        elif len(self.address).__eq__(3):
                            self.address = PobAddrees(self.address[0], self.address[1], self.address[2])

                        person = Person(self.last_name, self.first_name, self.year_of_birth, self.email,
                                        self.phones, self.address)

                        self.employees.add_employees([self.first_name, self.last_name], self.email)

                        if self.role.__eq__("staff"):
                            worker = Worker(person, self.data)
                        elif self.role.__eq__("engineer"):
                            worker = Engineer(person, self.data[0], self.data[1])
                        else:
                            if self.role.__eq__("sales"):
                                if len(self.data) > 2:
                                    worker = SalesPerson(person, self.data[0], self.data[1], self.data[2:])
                                else:
                                    print("Error: the data isn't enough <data>: ",
                                          self.data)
                                    exit(1)
                            else:
                                raise Exception("Error: Type of <Role>: ", self.role)
                        Team(worker, self.team[0])
                    self.flag_correct = True
            else:
                continue
        self.f.close()
