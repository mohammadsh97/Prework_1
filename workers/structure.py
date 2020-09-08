import abc

from workers.person import Person

list_of_team = {}


class Group:
    list_of_sub_groups_or_workers = []

    def __init__(self, name, description, parent_group=None):
        self.name = name
        self.description = description

        if parent_group is None:
            self.parent_group = ""
        else:
            self.parent_group = parent_group

    def add_sub_group_or_worker(self, temp):
        if isinstance(temp, Worker) or isinstance(temp, Group):
            self.list_of_sub_groups_or_workers.add(temp)

    def get_workers(self):
        list_of_workers = []
        return [list_of_workers.add(worker) for worker
                in self.list_of_sub_groups_or_workers if type(worker) == Worker]

    def get_parents(self):
        list_of_sub_group = []
        return [list_of_sub_group.add(sub_group) for sub_group
                in self.list_of_sub_groups_or_workers if type(sub_group) == Group]


class Team:

    def __init__(self, worker, parent_group):

        if parent_group in list_of_team:
            list_of_team[parent_group].append(worker)
        else:
            list_of_team[parent_group] = [worker]


class Worker:
    def __init__(self, person, salary):
        if isinstance(person, Person):
            self.person = person
        else:
            print("First variable isn't type of person\n")
            exit(1)
        self.salary = salary

    def get_salary(self):
        return self.salary


class Engineer(Worker):
    def __init__(self, person, salary, bonus):
        super().__init__(person, salary)
        self.bonus = bonus

    @abc.abstractmethod
    def get_salary(self):
        try:
            return super(Engineer, self).get_salary() + self.bonus
        except:
            raise NotImplementedError()


class SalesPerson(Worker):
    def __init__(self, person, salary, commission, deals):
        super(SalesPerson, self).__init__(person, salary)
        self.commission = commission
        self.deals = deals

    @abc.abstractmethod
    def get_salary(self):
        try:
            return self.get_salary() + (self.commission * sum(self.deals))
        except:
            raise NotImplementedError()
