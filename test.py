from hwltd.organization import HelloWorld
from hwltd.reports import get_average_salary, get_num_employees, get_relational_salary
from workers.structure import Group, list_of_team

hellow_world = HelloWorld()
get_num_employees("engineering", 1)
group = Group("SW", "Hello", "engi")
AGV = get_average_salary(group)
print(AGV)
relational = get_relational_salary(list_of_team['qa'][0])
print(relational)
