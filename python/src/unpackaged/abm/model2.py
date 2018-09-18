import random
import operator
import matplotlib.pyplot
import itertools
import time
import agentframework

start = time.clock()

# initialize 
num_of_agents = 10
num_of_iterations = 10000
agents = []


# make the agents
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])


# move the agents in random direction 
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100


# plot agents on grid
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()


# distance function
def distance_bet(agentA, agentB):
    return (((agentA[0] - agentB[0])**2) + 
        ((agentA[1] - agentB[1])**2))**0.5

distance = []

#for i, j in itertools.combinations(agents, 2):
#    disty = distance_bet(i, j)
#    distance.append(distance)

for i in range(len(agents)):
    for j in range(i + 1, len(agents)):
        disty = distance_bet(agents[i], agents[j])
        distance.append(disty)

end = time.clock()
print("time = " + str(end - start))

a = agentframework.Agent()
print(a.y, a.x)



















