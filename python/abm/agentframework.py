import random
import math


class Agent:
    
    """
    Defines a single agent in an environment.
    
    Attributes:
        environment: A list of lists defining a theoretical environment
        x/y: Coordinates defining agents location within the environment
        store: A store of an agents resources having 'eaten' the environment
        neighbourhood: The euclidean distance in which agents will share its store
        
    Behaviours:
        move: Move pseudo-randomly around the environment
        eat: Depletes the environment store at its location
        sick: Dumps its store in the environment having eaten too much
        share_with_neighboursbours: Agent shares its store evenly with neighbour
        have_infant: Creates an instance of an infant class
        
    """
    
    # Constuctor methods
    def __init__(self, environment, neighbourhood):
        self.environment = environment        
        self.y = random.randint(0, len(self.environment[1]))        
        self.x = random.randint(0, len(self.environment))
        self.store = 0 
        self.neighbourhood = neighbourhood


    # Agent string - returns agents coordinates and store 
    def __str__(self):        
        return str(self.y) + ',' + str(self.x) + ',' + str(self.store) + ',' 
        

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
        # if environment value is more than 20, eat 20.
        if self.environment[self.y][self.x] > 20:
            self.environment[self.y][self.x] -= 20
            self.store += 20
        else: 
            # eat remaining value 
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0    
            
            
    def sick(self):
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0
    
    
    # Calculates the euclidean distance between agents
    def distance_between(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    
    def share_with_neighbours(self, neighbourhood, agents):
        for agent in agents:
            # if agent not equal to itself
            if self != agent:
                if self.distance_between(agent) <= neighbourhood:
                    average = (self.store + agent.store)/2
                    self.store = average
                    agent.store = average
                    
                    
    def have_infant(self, neighbourhood, agents, infants):
        for agent in agents:
            # if agent not equal to itself
            if self != agent:
                if self.distance_between(agent) <= 2:
                    infants.append(Infant(self.environment, neighbourhood))
                    
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
        
        
        
        
class Infant(Agent):
    
    """
    Infant class inherits behaviour from Agent class
    """
    
    def __init__(self, environment, neighbourhood):
        super().__init__(environment, neighbourhood)
    
        
        
        
class Wolf:
    
    """
    A single wolf in a pre-defined environment.
    
    Attributes:
        environment: A list of lists defining a theoretical environment
        x/y: Coordinates defining wolfs location within the environment
        neighbourhood: The euclidean distance in which a wolf can eat an agent
        store: Store of values attained from eating and aquiring agents store
        direc: General direction of wolfs trajectory - up or east
        
    Behaviours:
        move: Move randomly around the environment
        eat_agents: Removes agents from environment and aquires agents store
        eat_infants: Removes infants from environment and aquires infants store
    """
    
    # Constructor methods
    def __init__(self, environment, neighbourhood):
        self.environment = environment    
        self.y = random.randint(0, len(self.environment[1]))        
        self.x = random.randint(0, len(self.environment))
        self.neighbourhood = neighbourhood
        self.store = 0
        if random.randint(0,1) == 1:
            self.direc = 'up' 
        else:        
            self.direc = 'east' 


    # Wolf string - returns wolfs coordinates and direction
    def __str__(self):        
        return str(self.y) + ',' + str(self.x) + ',' + str(self.direc)


    def move(self):
        # wolves move up to 10 places per iteration to increase distance covered
        if self.direc == 'up':
            if random.random() < 0.5:
                self.x = (self.x + 10) % len(self.environment)
            else:
                self.x = (self.x - 10) % len(self.environment)

            if random.random() < 0.5:
                self.y = (self.y + 10) % len(self.environment[1])
            else:
                self.y = (self.y - 0) % len(self.environment[1])
        else:
            if random.random() < 0.5:
                self.x = (self.x + 10) % len(self.environment)
            else:
                self.x = (self.x - 0) % len(self.environment)

            if random.random() < 0.5:
                self.y = (self.y + 10) % len(self.environment[1])
            else:
                self.y = (self.y - 10) % len(self.environment[1])


    # Calculates the euclidean distance between wolf and agent
    def distance_between(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)    

 
    def eat_agents(self, neighbourhood, wolves, agents):
        for _wolf in wolves:
            for agent in agents:
                distance = self.distance_between(agent) 
                if distance <= neighbourhood:
                    # wolf aquires agents store and removes agent
                    self.store += agent.store
                    agents.remove(agent)
                

    def eat_infants(self, neighbourhood, wolves, infants):
        for _wolf in wolves:
            for infant in infants:
                distance = self.distance_between(infant) 
                if distance <= neighbourhood:
                    # wolf aquires infants store and removes infant
                    self.store += infant.store
                    infants.remove(infant)
        
        
        
        
        
        