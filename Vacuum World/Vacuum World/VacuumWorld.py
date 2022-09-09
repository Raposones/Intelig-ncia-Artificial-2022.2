from Environment import Environment
from Agent import Agent
from Action import Action


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


env = Environment(1, 1, 1)
agent = Agent()


while True:
    percept = Agent.perceive(env)

    if env.isDirtyA == 0 and env.isDirtyB == 0:
        print(bcolors.OKBLUE + 'All locations are clean. Shutting down...' + bcolors.ENDC)
        break

    if percept.location == 1:
        print(bcolors.BOLD + 'Vacuum bot is in location A' + bcolors.ENDC)
        if percept.isDirty:
            print(bcolors.WARNING + 'A is dirty. Starting cleanup...' + bcolors.ENDC)
            action = Action('clean')
            agent.act(action, env)
            print(bcolors.OKGREEN + 'Cleanup done.\n' + bcolors.ENDC)
        else:
            print(bcolors.OKCYAN + 'A is clean. Moving to B.\n' + bcolors.ENDC)
            action = Action('right')
            agent.act(action, env)
    else:
        print(bcolors.BOLD + 'Vacuum bot is in location B' + bcolors.ENDC)
        if percept.isDirty:
            print(bcolors.WARNING + 'B is dirty. Starting cleanup...' + bcolors.ENDC)
            action = Action('clean')
            agent.act(action, env)
            print(bcolors.OKGREEN + 'Cleanup done.\n' + bcolors.ENDC)
        else:
            print(bcolors.OKCYAN + 'B is clean. Moving to B.\n' + bcolors.ENDC)
            action = Action('right')
            agent.act(action, env)