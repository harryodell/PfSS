import random
import operator
import matplotlib.pyplot 
import itertools
import time
import agentframework
import csv 
import pandas as pd

#start = time.clock()
 
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

#lenx = len(environment)
#leny = len(environment[1])

data = pd.read_csv('in.txt', header = None)


# plot data
# matplotlib.pyplot.imshow(environment)
# matplotlib.pyplot.show()


# initialize 
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
leny = len(environment[1])
lenx = len(environment)

# make the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents,
                                       neighbourhood))
 
# make the agents using list comp
agents = [agentframework.Agent(environment, agents, neighbourhood) for n in range(num_of_agents)]

# move the agents in random direction 
#for j in range(num_of_iterations):
#    for i in range(num_of_agents):
#        agents[i].move()


# move. eat, sick 
for j in range(num_of_iterations): 
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].sick()
        agents[i].share_with_neighbours(neighbourhood)

for j in range(num_of_iterations):
    random.shuffle(agents)
    for i, agent in enumerate(agents):
        print(i)
        agent.move()
        agent.eat()
        agent.sick()
        agent.share_with_neighbours(neighbourhood)
        
        
# print agents x, y and store        
for i in range(num_of_agents):
    print(f"Agent {i}: x = {agents[i].x}, "
                          f"y = {agents[i].y}, "
                          f"store = {agents[i].store}")
 

# plot agents on grid
matplotlib.pyplot.xlim(0, lenx)
matplotlib.pyplot.ylim(0, leny)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y, s=50)
matplotlib.pyplot.show()


# distance function
#def distance_between(agents_row_a, agents_row_b):
#    return (((agents_row_a.x - agents_row_b.x)**2) + 
#    ((agents_row_a.y - agents_row_b.y)**2))**0.5

#distance = []

#for i, j in itertools.combinations(agents, 2):
#    disty = distance_bet(i, j)
#    distance.append(distance)

#for i in range(len(agents)):
#    for j in range(i + 1, len(agents)):
#        disty = distance_between(agents[i], agents[j])
#        distance.append(disty)

#end = time.clock()
#print("time = " + str(end - start))

# write environment to file
#f2 = open('env.txt', 'w', newline='') 
#writer = csv.writer(f2, delimiter=' ')
#for row in environment:		
#	writer.writerow(row)		# List of values.
#f2.close()


# write agent store to file
for i in agents:
    print(i.store)

#f3 = open('stored.txt', 'w', newline='') 
#writer = csv.writer(f3, delimiter=' ')
#for i in agents:
#    listy = []
#    listy.append(i.store)
#    writer.writerow(listy)		# List of values.
#f3.close()















