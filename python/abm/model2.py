import random
import operator
import matplotlib.pyplot as plt 
import agentframework
import matplotlib.colors as colors


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

# data = pd.read_csv('in.txt', header = None)


# plot data
# plt.imshow(environment)
# plt.show()


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

# make the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents,
                                       neighbourhood, colours))
    
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolf(environment, wolves,
                                       neighbourhood, agents))
    
# wolves = [agentframework.Wolf(environment, wolves, neighbourhood, agents) for n in range(num_of_wolves)]
 
# make the agents using list comp
#agents = [agentframework.Agent(environment, agents, neighbourhood) for n in range(num_of_agents)]

# move the agents in random direction 
#for j in range(num_of_iterations):
#    for i in range(num_of_agents):
#        agents[i].move()


# move. eat, sick 
#for j in range(num_of_iterations):
#    random.shuffle(agents)
#    for i, agent in enumerate(agents):
#        print(i)
#        agent.move()
#        agent.eat()
#        # agent.sick()
#        agent.share_with_neighbours(neighbourhood)




#def distance_between(wolf, agent):
#    return (((agent.x - wolf.x)**2) + ((agent.y - wolf.y)**2))**0.5

for j in range(num_of_iterations):
    random.shuffle(agents)
    for agent in agents:
        agent.move()
        agent.eat()
        # agent.sick()
        agent.share_with_neighbours(neighbourhood)


for i in range(num_of_iterations):
    for wolf in wolves:
        wolf.move()
        wolf.eatSheep(agents, neighbourhood)


        
result = []
for k in range(num_of_iterations):
    random.shuffle(agents)
    random.shuffle(wolves)
    for agent in agents:
        agent.move()
        agent.eat()
        # agent.sick()
        #agent.share_with_neighbours(neighbourhood)
    for wolf in wolves:
        wolf.move()
        wolf.eatSheep(agents, neighbourhood)   
    for wolf in wolves:
        for agent in agents:
            if distance_between(wolf, agent) <= 2:
                result.append(agent)
 
agents = set(agents) - set(result)

for i, agent in enumerate(agents):
    if agent.x >= 1:
        print(agents[i])
        agents.remove(agent)

for i, agent in enumerate(agents):
    if 1 <= 10:
        print(agents[i])
        agents.remove(agent)
        
result = []
for wolf in wolves:
    for agent in agents:
        #if 1 <= 10:
        if distance_between(wolf, agent) <= neighbourhood:
            result.append(agent)
            a = result

agents = set(agents) - set(a)


# print agents x, y and store        
for i in range(num_of_agents):
    print(f"Agent {i}: x = {agents[i].x}, "
                          f"y = {agents[i].y}, "
                          f"store = {agents[i].store}")
 
    
# distance between wolves and agents
def distance_between(wolf, agent):
    return (((agent.x - wolf.x)**2) + ((agent.y - wolf.y)**2))**0.5
    
for wolf in wolves:
    for agent in agents:
        distance = distance_between(wolf, agent) 
        if distance <= neighbourhood:
            print('eat')
            del(agent)




# plot agents on grid
plt.xlim(0, lenx)
plt.ylim(0, leny)
plt.imshow(environment)
for i in range(num_of_agents):
    plt.scatter(agents[i].x, agents[i].y, s=50)
for wolf in wolves:
    plt.scatter(wolf.x, wolf.y, s=50, c = wolf.colours, marker = '*')
plt.show()


# distance function
#def distance_between(agents_row_a, agents_row_b):
#    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5



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








