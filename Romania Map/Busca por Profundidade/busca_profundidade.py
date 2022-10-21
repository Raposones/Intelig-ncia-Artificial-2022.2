from types import NoneType
from numpy import append


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
    def __init__(self, state_name, father, cost):
        self.state_name = state_name
        self.father = father
        self.cost = cost

    def __eq__(self, __obj: 'Node'):
        return self.state_name == __obj.state_name


def deep_search(map_dict, start, end):
    used = []
    start_node = Node(start, None, 0)
    border = [start_node]
    while True:
        if len(border) == 0:
            print('error')
            return 0
        actual = border[-1]
        border.pop()
        used.append(actual)
        actual_transitions = map_dict.get(actual.state_name)
        for transition in actual_transitions:
            child = Node(transition[0], actual, actual.cost + transition[1])
            if child not in used + border:
                if child.state_name == end:
                    path_distance = ds_solution(child)
                    path = list(reversed(path_distance[0]))
                    total = path_distance[1]
                    return path_print(path, total)
                border.append(child)


def ds_solution(node):
    path = []
    actual = node
    total = actual.cost
    while type(actual) is not NoneType:
        path.append(actual.state_name)
        actual = actual.father
    return path, total


def path_print(path, total):
    print(bcolors.WARNING + path[0] + bcolors.ENDC +
          ' to ' + bcolors.OKGREEN + path[-1] + bcolors.ENDC + '\n')
    for ind, state in enumerate(path):
        if state == path[-2]:
            print(f'{state} --> ' + bcolors.OKGREEN + f'{path[ind+1]}' + bcolors.ENDC
                  )
            break
        elif state == path[0]:
            print(bcolors.WARNING + f'{state}' +
                  bcolors.ENDC + f' --> {path[1]}'
                  )
        else:
            print(f'{state} --> {path[ind+1]}'
                  )
    print('Total distance: ' + bcolors.OKCYAN +
          f'{total}KM' + bcolors.ENDC)
