from Perception import Perception
from Environment import Environment
from Action import Action


class Agent:

    @staticmethod
    def act(action: Action, env: Environment):
        env.update(action.name)

    @staticmethod
    def perceive(environment):
        if environment.agentLocation == 1:
            local = 1
            localStatus = environment.isDirtyA
        else:
            local = 0
            localStatus = environment.isDirtyB
        percept = Perception(local, localStatus)
        return percept


