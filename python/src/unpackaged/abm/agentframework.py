import random

class Agent:    
    def __init__(self, environment):
        self.y = random.randint(0,99)        
        self.x = random.randint(0,99)
        self.environment = environment
        self.store = 0 

        
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100        


    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0    
    
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
        
    

#a = Agent()
#print(a.y, a.x)

#a.move()
#print(a.y, a.x)



















