import random
import math

# Create agent class
class Agent:
    
    """
    A single agent in a pre-defined environment.
    
    Attributes:
        environment: A list of lists defining a theoretical environment
        agents: A list of all agents in the environment
        x/y: Coordinates defining agents location within the environment
        store: A store of an agents resources having 'eaten' the environment
        colours: A colour to be plotted for an agent
        neighbourhood: The euclidean distance in which agents will share its store
        
    Behaviours:
        move: Move randomly around the environment
        eat: Depletes the environment store at its location
        sick: Dumps its store in the environment having eaten too much
        share_with_neighboursbours: Agent shares its store evenly with neighbour
        
    """
    
    # Constuctor methods
    def __init__(self, environment, agents, neighbourhood, colours):
        self.agents = agents
        self.environment = environment        
        self.y = random.randint(0, len(self.environment[1]))        
        self.x = random.randint(0, len(self.environment))
        self.store = 0 
        self.neighbourhood = neighbourhood
        self.colours = random.choice(colours)


    # Agent string - returns agents coordinates, store and colour
    def __str__(self):        
        return str(self.y) + ',' + str(self.x) + ',' + str(self.store) + ',' + str(self.colours)
        
    
    # Function to move the agent
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.environment)
        else:
            self.x = (self.x - 1) % len(self.environment)
            
        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.environment[1])
        else:
            self.y = (self.y - 1) % len(self.environment[1])        


    # Function to eat
    def eat(self):
        # if environment value is more than 10, eat 10..
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else: # else eat remaining value 
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0    
            
            
    # Function to be sick        
    def sick(self):
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0
    
    
    # Calculates the euclidean distance between agents
    def distance_between(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    
    # Function to share store
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            if agent != self:
                distance = self.distance_between(agent) 
                if distance <= self.neighbourhood:
                #if self.distance_between(agent) <= self.neighbourhood:           
                    average = (self.store + agent.store)/2
                    self.store = average
                    agent.store = average
                    print(f"Agent ({self}) sharing with Agent ({agent}): dist = {str(distance)}, ave = {str(average)}")
                    print("\n")

    def die(self):
        raise NotImplementedError
        
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
        
        
        
        
        
# Create wolf class      
class Wolf:
    def __init__(self, environment, wolves, neighbourhood, agents):
        self.wolves = wolves
        self.environment = environment    
        self.y = random.randint(0, len(self.environment[1]))        
        self.x = random.randint(0, len(self.environment))
        self.neighbourhood = neighbourhood
        self.colours = 'black'
        
        
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.environment)
        else:
            self.x = (self.x - 1) % len(self.environment)

        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.environment[1])
        else:
            self.y = (self.y - 1) % len(self.environment[1])            

    def distance_between(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)    
    
    def eatSheep(self, agents, neighbourhood):
        for wolf in self.wolves:
            for agent in agents:
                distance = self.distance_between(self.agent) 
                if distance <= neighbourhood:
                    print('eat')
                    #del(agent)
                    
        

#wolves = []
#wolves = [Wolf(environment, wolves, neighbourhood) for n in range(num_of_wolves)]
        
        
        
        
        
        
        
        
        
        
        