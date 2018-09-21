import random
import math
# import itertools

class Agent:    
    def __init__(self, environment, agents, neighbourhood):
        self.agents = agents
        self.environment = environment        
        self.y = random.randint(0, len(self.environment[1]))        
        self.x = random.randint(0, len(self.environment))
        self.store = 0 
        self.neighbourhood = neighbourhood


    def __str__(self):        
        return str(self.y) + ',' + str(self.x) + ',' + str(self.store)
        
    
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.environment)
        else:
            self.x = (self.x - 1) % len(self.environment)

        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.environment[1])
        else:
            self.y = (self.y - 1) % len(self.environment[1])        


    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0    
            
            
    def sick(self):
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0
    
    
    def distance_between(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    
    def share_with_neighbours(self, neighbourhood):
        i = 0
        for agent in self.agents:
            i += 1
            if agent != self:
                distance = self.distance_between(agent) 
                if distance <= neighbourhood:
                    average = (self.store + agent.store)/2
                    self.store = average
                    agent.store = average
                    #print("sharing " + str(distance) + " " + str(average))
                    
                    #print(f"{str(self)} sharing with {str(agent)}: dist = {str(distance)}, ave = {str(average)}")
                    print(f"Agent ({self}) sharing with Agent ({agent}): dist = {str(distance)}, ave = {str(average)}")
                    print("\n")

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @x.setter
    def x(self, value):
        self._x = value 
        
    @y.setter 
    def y(self, value):
        self._y = value
        
    



#a.move()
#print(a.y, a.x)


#a = Agent(environment, agents, neighbourhood)
#a.neighbourhood
















