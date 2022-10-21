from calendar import c
from types import NoneType


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


def greedy_search(map_dict, hv, start, end):
    start_node = Node(start, None, 0)
    border, used = [start_node], []
    while True:
        if len(border) == 0:
            return 'error'
        border = greedy_order(border, hv)
        actual = border[0]
        border.pop(0)
        if actual.state_name == end:
            path = list(reversed(hs_solution(actual)))
            return path_print(path)
        used.append(actual)
        actual_transitions = map_dict.get(actual.state_name)
        for transition in actual_transitions:
            child = Node(transition[0], actual,
                         actual.cost + transition[1])
            if child not in border + used:
                border.append(child)
            elif child in border:
                for x in border:
                    if x == child and x.cost > child.cost:
                        x.cost == child.cost
                        x.father == child.father


def greedy_order(border, hv):
    border = [(x, hv.get(x.state_name)) for x in border]
    border.sort(key=lambda tup: tup[1])
    border = [x[0] for x in border]
    return border


def star_search(map_dict, hv, start, end):
    start_node = Node(start, None, 0)
    border, used = [start_node], []
    while True:
        if len(border) == 0:
            return 'error'
        border = star_order(border, hv)
        actual = border[0]
        border.pop(0)
        if actual.state_name == end:
            path = list(reversed(hs_solution(actual)))
            return path_print(path)
        used.append(actual)
        actual_transitions = map_dict.get(actual.state_name)
        for transition in actual_transitions:
            child = Node(transition[0], actual,
                         actual.cost + transition[1])
            if child not in border + used:
                border.append(child)
            elif child in border:
                for x in border:
                    if x == child and x.cost > child.cost:
                        x.cost = child.cost
                        x.father = child.father


def star_order(border, hv):
    border = [(x, hv.get(x.state_name) + x.cost) for x in border]
    border.sort(key=lambda tup: tup[1])
    border = [x[0] for x in border]
    return border


def hs_solution(node):
    path = []
    while type(node) is not NoneType:
        path.append(node.state_name)
        node = node.father
    return path


def path_print(path):
    print(bcolors.WARNING + path[0] + bcolors.ENDC +
          ' to ' + bcolors.OKGREEN + path[-1] + bcolors.ENDC + '\n')
    for ind, state in enumerate(path):
        if state == path[-2]:
            print(f'{state} --> ' + bcolors.OKGREEN +
                  f'{path[ind+1]}' + bcolors.ENDC)
            break
        elif state == path[0]:
            print(bcolors.WARNING + f'{state}' +
                  bcolors.ENDC + f' --> {path[1]}')
        else:
            print(f'{state} --> {path[ind+1]}')
