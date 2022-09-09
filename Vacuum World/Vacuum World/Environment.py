class Environment:
    def __init__(self, isDirtyA, isDirtyB, agentLocation):
        self.isDirtyA = isDirtyA
        self.isDirtyB = isDirtyB
        self.agentLocation = agentLocation

    def update(self, action: str):
        if action == 'clean':
            if self.agentLocation == 1:
                self.isDirtyA = 0
            else:
                self.isDirtyB = 0

        elif action == 'right':
            if self.agentLocation == 1:  #A -> B
                self.agentLocation = 0

        elif action == 'left': # action == 'left'
            if self.agentLocation == 0: #A <- B
                self.agentLocation = 1



