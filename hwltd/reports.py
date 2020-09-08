import numpy as np

from workers.structure import list_of_team, Worker

# My Structure
hello_world_temp = {
    "Engineering Department":
        {"SW Group":
             [0, {"Infrastructure": 0, "App Team": 0, "Drivers": 0, "QA": 0}],
         "HW Group":
             [0, {"Chip": 0, "Board": 0, "Power": 0}],
         "CTO Group":
             [0],
         "System Group":
             [0, {"Design": 0, "Poc": 0}]},

    "HR Department":
        {"Recruitment Group":
             [0, {"Tech": 0, "Staff": 0}],
         "Culture Group":
             [0]},

    "Finance Department":
        {"Salaries Group":
             [0],
         "Budget Group":
             [0, {"Income": 0, "Outcome": 0}]}
}

department_dic = {
    "Engineering Department": 0, "HR Department": 0, "Finance Department": 0
}


def get_num_employees(department, depth):
    group_counter = 0
    department_counter = 0

    # insert all of data
    # depth_one is a department
    for depth_one in [k for k, v in hello_world_temp.items()]:
        # depth_two is a Groups
        for depth_two in hello_world_temp[depth_one]:
            # the len of group with team structure is equal to 2
            if len(hello_world_temp[depth_one][depth_two]) == 2:
                # The key is name of team for my structure
                for key in hello_world_temp[depth_one][depth_two][1].keys():
                    # The key_team is name of team i have
                    for key_team in list_of_team.keys():
                        # if name of team is equal the name of team in my structure
                        if key_team.lower() in key.lower():
                            hello_world_temp[depth_one][depth_two][1][key] = list_of_team[key_team]
                            group_counter += len(list_of_team[key_team])

                    hello_world_temp[depth_one][depth_two][0] += group_counter
                    department_counter += group_counter
                    # to reset the counter of group
                    group_counter = 0
            # the len of group without team structure is equal to 1
            elif len(hello_world_temp[depth_one][depth_two]) == 1:
                for key_team in list_of_team.keys():
                    if key_team.lower() in depth_two.lower():
                        hello_world_temp[depth_one][depth_two][0] = {
                            len(list_of_team[key_team]): list_of_team[key_team]}
                        group_counter += len(list_of_team[key_team])
                        department_counter += group_counter
                        group_counter = 0
        # to save counter of sub group of department in dictionary
        department_dic[depth_one] = department_counter
        department_counter = 0
    # #######################################################################################################################
    # read the data and print department with depth
    # depth_one is a department
    for depth_one in [k for k, v in hello_world_temp.items()]:
        if department.lower() in depth_one.lower():
            print(depth_one, "-", department_dic[depth_one], "Workers")
            if depth == 1:
                break
            # depth_two is a Groups
            for depth_two in hello_world_temp[depth_one]:
                # the len of group with team structure is equal to 2
                if len(hello_world_temp[depth_one][depth_two]) == 2:
                    print(" ", depth_two, "-", hello_world_temp[depth_one][depth_two][0], "Workers")
                    if depth == 3:
                        # The key is name of team for my structure
                        for key in hello_world_temp[depth_one][depth_two][1].keys():
                            if hello_world_temp[depth_one][depth_two][1][key] == 0:
                                print("  ", key, "-", hello_world_temp[depth_one][depth_two][1][key], "Workers")
                            else:
                                print("  ", key, "-", len(hello_world_temp[depth_one][depth_two][1][key]), "Workers")
                # the len of group without team structure is equal to 1
                elif len(hello_world_temp[depth_one][depth_two]) == 1:
                    if hello_world_temp[depth_one][depth_two][0] != 0:
                        key = [key for key, value in hello_world_temp[depth_one][depth_two][0].items()]
                        print(" ", depth_two, "-", key[0], "Workers")
                    else:
                        print(" ", depth_two, "-", 0, "Workers")


def get_average_salary(group):
    sum = 0
    # get the specific name of department
    depth_one = [k for k, v in hello_world_temp.items() if group.parent_group.lower() in k.lower()]

    if len(depth_one).__eq__(0):
        raise Exception(ValueError)
    # get the specific name of group
    depth_two = [k for k in hello_world_temp[depth_one[0]].keys() if group.name.lower() in k.lower()]
    # check if department and group names is not null
    if not (len(depth_two).__eq__(0)):
        all_of_teams = [all_of_teams for all_of_teams in hello_world_temp[depth_one[0]][depth_two[0]]]
        value = [v for k, v in all_of_teams[1].items() if v != 0]
        # number of worker in the group
        number_of_worker = all_of_teams[0]
        for x in value:
            for y in x:
                sum += np.double(y.get_salary()[0])
        return sum / number_of_worker
    else:
        raise Exception(ValueError)


def get_relational_salary(worker):
    if not isinstance(worker, Worker):
        raise Exception("The type is not worker")
    dict_relational_salary = {}

    for k, v in list_of_team.items():
        for each_worker in v:
            if each_worker != worker:
                if each_worker.get_salary()[0] != department_dic.keys():
                    dict_relational_salary[np.double(each_worker.get_salary()[0])] = \
                        np.double(np.double(each_worker.get_salary()[0]) / np.double(worker.get_salary()[0]))

    return dict_relational_salary
