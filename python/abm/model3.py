import random
import operator
import matplotlib
#matplotlib.use('macosx') 
import matplotlib.pyplot as plt
import agentframework
import matplotlib.animation 
import matplotlib.colors as colors
# %matplotlib qt

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

# initialie variables
num_of_agents = 5
num_of_wolves = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
wolves = []
leny = len(environment[1])
lenx = len(environment)
carry_on = True
a = 0 
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
totalenv = sum(sum(x) for x in environment)
colours = list(colors._colors_full_map.values())


# make the agents using list comp
# make the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents,
                                       neighbourhood, colours))
    
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolf(environment, wolves,
                                       neighbourhood, agents))


def update(blah):
    
    fig.clear()  
    global carry_on

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
            wolf.eatSheep(neighbourhood)
            
    if sum(sum(x) for x in environment) < totalenv*0.8:
        carry_on = False
        print("Stopping condition met - Environment depleted by *******")
               
    # plot agents on grid
    plt.xlim(0, lenx)
    plt.ylim(0, leny)
    plt.imshow(environment)
    #for i in range(num_of_agents):
     #   plt.scatter(agents[i].x, agents[i].y, s=50)
    for agent in agents:
        plt.scatter(agent.x, agent.y, s=50, c = agent.colours)

    for wolf in wolves:
        plt.scatter(wolf.x, wolf.y, s=50, c = wolf.colours, marker = '*')



def gen_function(blah = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on):
        yield a			# Returns control and waits next call.
        a += 1


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations) 
animation = matplotlib.animation.FuncAnimation(fig, update, interval = 1, frames=gen_function, repeat=False)
plt.show()










































