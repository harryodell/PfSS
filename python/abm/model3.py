import random
import matplotlib
#matplotlib.use('macosx') 
import matplotlib.pyplot as plt
import agentframework
import matplotlib.animation 
import matplotlib.colors as colors
# %matplotlib qt
import sys


def sysArgs():

    attempts = 0 
    while True:
        try:
            num_of_agents = int(input("Number of agents: "))
            break
        except ValueError:
            attempts += 1
            if attempts < 3:
                print("Please enter a valid integer.")
                continue
            else:
                print("Failed to pass argument correctly, default number of agents assigned.")
                num_of_agents = 100
                break          
    
    attempts = 0 
    while True:
        try:
            num_of_wolves = int(input("Number of wolves: "))
            break
        except ValueError:
            attempts += 1
            if attempts < 3:
                print("Please enter a valid integer.")
                continue
            else:
                print("Failed to pass argument correctly, default number of wolves assigned.")
                num_of_wolves = 5
                break      

    attempts = 0 
    while True:
        try:
            num_of_iterations = int(input("Number of iterations: "))
            break
        except ValueError:
            attempts += 1
            if attempts < 3:
                print("Please enter a valid integer.")
                continue
            else:
                print("Failed to pass argument correctly, default number of iterations assigned.")
                num_of_iterations = 1000
                break    

    attempts = 0            
    while True:
        try:
            neighbourhood = int(input("Size of neighbourhood: "))
            break
        except ValueError:
            attempts += 1
            if attempts < 3:
                print("Please enter a valid integer.")
                continue
            else:
                print("Failed to pass argument correctly, default neighbourhood size assigned.")
                neighbourhood = 20
                break    

    print(f"\n" 
          f"Running model for {num_of_agents} Agents, {num_of_wolves} Wolves, "
          f"{num_of_iterations} iterations and a neighbourhood of {neighbourhood}"
          f"\n")   
    return (num_of_agents, num_of_wolves, num_of_iterations, neighbourhood)


if len(sys.argv) == 5:
    while True:
        try:
            num_of_agents = int(sys.argv[1])
            num_of_wolves = int(sys.argv[2])
            num_of_iterations = int(sys.argv[3])
            neighbourhood = int(sys.argv[4]) 
            print(f"Running model for {num_of_agents} Agents, {num_of_wolves} Wolves, "
                  f"{num_of_iterations} iterations and a neighbourhood of {neighbourhood}"
                  f"\n")
            break
        except ValueError:
            print("Arguments must be passed as integers, please enter:")
            num_of_agents, num_of_wolves, num_of_iterations, neighbourhood = sysArgs()
            break

elif len(sys.argv) == 1:
    num_of_agents = 100
    num_of_wolves = 5
    num_of_iterations = 1000
    neighbourhood = 20
    print(f"No arguments attempted to be passed, running for default parameters: \n"
          f"{num_of_agents} Agents, {num_of_wolves} Wolves, "
          f"{num_of_iterations} iterations, neighbourhood of {neighbourhood}"
          f"\n")    

else:
    print("Incorrect number of arguments passed, please enter:")
    num_of_agents, num_of_wolves, num_of_iterations, neighbourhood = sysArgs()


# read in data 
environment = []
with open('in.txt', 'r') as file_for_reading:
    for row in file_for_reading:
        rowlist = row.split(',')
        rowlisty = list(map(int, rowlist))
        environment.append(rowlisty)


# initialie variables
#num_of_agents = 100
#num_of_wolves = 5
#num_of_iterations = 1000
#neighbourhood = 20
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


# make the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,
                                       neighbourhood, colours))
    
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolf(environment,
                                       neighbourhood))


def update(blah):
    
    fig.clear()  
    global carry_on
    
    for j in range(10):
        random.shuffle(agents)
        for agent in agents:
            agent.move()
            agent.eat()
            # agent.sick()
            agent.share_with_neighbours(neighbourhood, agents)
    
    #for i in range(num_of_iterations):
    for wolf in wolves:
        wolf.move()
        wolf.eatSheep(neighbourhood, wolves, agents)
            
    if sum(sum(x) for x in environment) < totalenv*0.8:
        carry_on = False
        print("Stopping condition met - Environment depleted by *******")
        
    if len(agents) == 0:
        carry_on = False
        print("Stopping condition met - no sheep left!")
    
    
    # plot agents on grid
    plt.xlim(0, lenx)
    plt.ylim(0, leny)
    plt.imshow(environment)
    for agent in agents:
        plt.scatter(agent.x, agent.y, s=50, c = 'white') #c = agent.colours)

    for wolf in wolves:
        plt.scatter(wolf.x, wolf.y, s=50, c = wolf.colours, marker = '*')



def gen_function(blah = [0]):
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on):
        yield a		
        a += 1

 
animation = matplotlib.animation.FuncAnimation(fig, update, interval = 1, frames=gen_function, repeat=False)
plt.show()






























