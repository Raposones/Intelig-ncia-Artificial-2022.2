"""
ALUNOS
Raphael Carvalho Garcia - 412557
Francisco Bruno Rodrigues Martins - 420855
"""


from traceback import print_tb


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Node:
    def __init__(self, state_name, father, father_cost):
        self.state_name = state_name
        self.father = father
        self.father_cost = father_cost


def lenght_search(map_dict, start, end):
    border = []
    border_state_names = []
    used = []
    start_node = Node(start, None, None)
    border.append(start_node)
    border_state_names.append(start_node.state_name)
    while True:
        if len(border) == 0:
            print('error')
            return 0
        actual = border[0]
        border.pop(0)
        border_state_names.remove(actual.state_name)
        used.append(actual.state_name)
        actual_transitions = map_dict.get(actual.state_name)
        for transition in actual_transitions:
            child = Node(transition[0], actual, transition[1])
            if child.state_name not in border_state_names and child.state_name not in used:
                if child.state_name == end:
                    path_distance = ls_solution(child)
                    path = list(reversed(path_distance[0]))
                    path_cost = list(reversed(path_distance[2]))
                    return path_print(path, path_distance[1], path_cost)
                border.append(child)
                border_state_names.append(child.state_name)


def ls_solution(node):
    path = []
    path_cost = []
    distance = 0
    actual = node
    while actual.father != None:
        path.append(actual.state_name)
        path_cost.append(actual.father_cost)
        distance += actual.father_cost
        actual = actual.father
    path.append(actual.state_name)
    return path, distance, path_cost


def path_print(path, total_dist, path_cost):
    print(bcolors.WARNING + path[0] + bcolors.ENDC +
          ' to ' + bcolors.OKGREEN + path[-1] + bcolors.ENDC + '\n')
    for ind, state in enumerate(path):
        if state == path[-2]:
            print(f'{state} --> ' + bcolors.OKGREEN + f'{path[ind+1]}' + bcolors.ENDC
                  + f' || Distance: {path_cost[ind]} Km'
                  + '\nTravel distance: ' + bcolors.OKCYAN + f'{total_dist} Km' + bcolors.ENDC)
            break
        elif state == path[0]:
            print(bcolors.WARNING + f'{state}' +
                  bcolors.ENDC + f' --> {path[1]}'
                  + f' || Distance: {path_cost[ind]} Km')
        else:
            print(f'{state} --> {path[ind+1]}'
                  + f' || Distance: {path_cost[ind]} Km')


map_dict = {
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Zerind': [('Oradea', 71), ('Arad', 75)],
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilceu', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu_Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu_Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu_Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Pitesti', 101), ('Fagaras', 211), ('Giurgiu', 90)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]}

states_list = list(map_dict.keys())

end = 'Bucharest'
start = input(
    f'You are going on a bus trip to Bucharest. Where are you at?\n ==> ')
if start not in states_list:
    print(bcolors.FAIL + f'{start} is not a Romanian state.' + bcolors.ENDC)
elif start == end:
    print(bcolors.FAIL + 'You are already in Bucharest!' + bcolors.ENDC)
else:
    lenght_search(map_dict, start, end)
