import random
import operator
import matplotlib.pyplot 
import itertools
import time
import agentframework
import csv 
import pandas as pd
import matplotlib.animation 

# read in data 
environment = []
with open('in.txt', 'r') as file_for_reading:
    for row in file_for_reading:
        rowlist = row.split(',')
        rowlisty = list(map(int, rowlist))
#        rowlist = []	
#        for value in row:
#            rowlist.append(value)
        environment.append(rowlisty)

# initialize 
num_of_agents = 10
num_of_iterations = 10
neighbourhood = 20
agents = []
leny = len(environment[1])
lenx = len(environment)
 
# make the agents using list comp
agents = [agentframework.Agent(environment, agents, neighbourhood) for n in range(num_of_agents)]

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

def update(blah):
    
    fig.clear()   
    

    for j in range(num_of_iterations):
        random.shuffle(agents)
        for agent in agents:
            agent.move()
            agent.eat()
            agent.sick()
            agent.share_with_neighbours(neighbourhood)
            
        
    # plot agents on grid
    matplotlib.pyplot.xlim(0, lenx)
    matplotlib.pyplot.ylim(0, leny)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y, s=50)



#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
#animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False, frames=num_of_iterations)
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations) 
matplotlib.pyplot.show()
















