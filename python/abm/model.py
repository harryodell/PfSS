import random
import matplotlib.pyplot as plt 
import agentframework
import matplotlib.colors as colors


# read in data 
environment = []
with open('in.txt', 'r') as file_for_reading:
    for row in file_for_reading:
        rowlist = row.split(',')
        rowlisty = list(map(int, rowlist))
        environment.append(rowlisty)


# initialize 
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
leny = len(environment[1])
lenx = len(environment)
colours = list(colors._colors_full_map.values())
wolves = []
num_of_wolves = 100


# make the agents using list comp
agents = [agentframework.Agent(environment, agents, neighbourhood, colours) for n in range(num_of_agents)]

# make the wolves using list comp
wolves = [agentframework.Wolf(environment, wolves, neighbourhood, agents) for n in range(num_of_wolves)]


# agent interactions
for j in range(num_of_iterations):
    random.shuffle(agents)
    for agent in agents:
        agent.move()
        agent.eat()
        # agent.sick()
        agent.share_with_neighbours(neighbourhood)

# wolf interactions
for i in range(num_of_iterations):
    for wolf in wolves:
        wolf.move()
        wolf.eatSheep(agents, neighbourhood)


# plot agents on grid
plt.xlim(0, lenx)
plt.ylim(0, leny)
plt.imshow(environment)
for i in range(num_of_agents):
    plt.scatter(agents[i].x, agents[i].y, s=50)
for wolf in wolves:
    plt.scatter(wolf.x, wolf.y, s=50, c = wolf.colours, marker = '*')
plt.show()









