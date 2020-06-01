from Task1_Ship import Solution
import random
import time
import copy
import csv
import os
from urllib.request import urlopen

def dictcreator():
    solution_dict = {}
    solution_dict["Ship's capacity"] = []
    solution_dict["Number of containers"] = []
    solution_dict["Dynamic algorithm time"] = []
    solution_dict["Greedy algorithm time"] = []
    solution_dict["Greedy algorithm quality"] = []
    return solution_dict

def timer(object, n, backpack_size):

    tic_dynamic = time.perf_counter()
    dynamic_solution = object.dynamic_pack_it(n, backpack_size)
    toc_dynamic = time.perf_counter()
    dynamic_time = round(toc_dynamic - tic_dynamic, 5)

    tic_greedy = time.perf_counter()
    greedy_solution = object.greedy_pack_it(n, backpack_size)
    toc_greedy = time.perf_counter()
    greedy_time = round(toc_greedy - tic_greedy, 5)

    greedy_solution_quality = round((dynamic_solution - greedy_solution)/dynamic_solution, 5)
    print("""
    size list: {} 
    value list: {}
    backpack size: {}
    dynamic solution: {}
    greedy solution: {}
    greedy solution quality: {}\n""".format(object.size_list, object.value_list,backpack_size, dynamic_solution, greedy_solution, (100 - (greedy_solution_quality*100))))
    return dynamic_time, greedy_time, (100 - (greedy_solution_quality*100))

def data_creator(ship_capacity, number_of_containers):

    size_list = []
    value_list = []

    for x in range(number_of_containers):
        size_list.append(random.randrange(1, int(ship_capacity*4/number_of_containers)))
        value_list.append(random.randrange(1, int(ship_capacity*4/number_of_containers)))

    return size_list, value_list

def data_input(ship_capacity, number_of_containers, number_of_steps, step_size, step_kind, solution_dict):

    for x in range(number_of_steps):
        ship_capacity_step = 0
        number_of_containers_step = 0
        if step_kind == "capacity": # here i chose which variable i change
            ship_capacity_step = step_size
        else:
            number_of_containers_step = step_size

        ship_capacity += ship_capacity_step
        number_of_containers += number_of_containers_step

        size_list, value_list = data_creator(ship_capacity,number_of_containers)

        s =Solution(size_list, value_list, ship_capacity)

        dynamic_time, greedy_time, greedy_solution_quality = timer(s, number_of_containers, ship_capacity)


        solution_dict["Ship's capacity"].append(ship_capacity)
        solution_dict["Number of containers"].append(number_of_containers)
        solution_dict["Dynamic algorithm time"].append(dynamic_time)
        solution_dict["Greedy algorithm time"].append(greedy_time)
        solution_dict["Greedy algorithm quality"].append(greedy_solution_quality)

if __name__ == '__main__':

    solution_dict_capacity_change = dictcreator()
    solution_dict_number_of_containers_change = dictcreator() # function that creates dictionary with nice key names easy to use in graphs

    # setup when capacity change
    ship_capacity = 500
    number_of_containers = 20
    number_of_steps = 15
    step_size =2000

    # setup when number of containers change
    ship_capacity1 = 10000
    number_of_containers1 = 10
    number_of_steps1 = 15
    step_size1 = 20

    data_input(ship_capacity, number_of_containers, number_of_steps, step_size, "capacity", solution_dict_capacity_change)
    data_input(ship_capacity1, number_of_containers1, number_of_steps, step_size1, "container_number", solution_dict_number_of_containers_change)

    list_of_files = [solution_dict_capacity_change, solution_dict_number_of_containers_change]
    SortingMethods = ["Capacity_change", "Number_of_containers_change"]

    for i in range(0, 2):
        My_Dict = list_of_files[i]
        zd = zip(*My_Dict.values())
        with open(SortingMethods[i] + ".csv", 'w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(My_Dict.keys())
            writer.writerows(zd)







