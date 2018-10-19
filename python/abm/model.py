import random
#matplotlib.use('macosx') 
# %matplotlib qt
import matplotlib
import matplotlib.pyplot as plt
import agentframework
import matplotlib.animation 
import sys
import csv

import functions


# If the correct number of arguments are passed
if len(sys.argv) == 5:
    while True:
        try:
            # try to run model using user parameters
            num_of_agents = int(sys.argv[1])
            num_of_wolves = int(sys.argv[2])
            num_of_iterations = int(sys.argv[3])
            neighbourhood = int(sys.argv[4]) 
            print(f"Running model for {num_of_agents} Agents, {num_of_wolves} Wolves, "
                  f"{num_of_iterations} iterations and a neighbourhood of {neighbourhood}"
                  f"\n")
            break
        except ValueError:
            # else, revert to sys_args function
            print("Arguments must be passed as integers, please enter:")
            num_of_agents, num_of_wolves, num_of_iterations, neighbourhood = functions.sys_args()
            break


# If no effort is made to pass model parameters, default values will be assigned
elif len(sys.argv) == 1:
    num_of_agents = 100
    num_of_wolves = 5
    num_of_iterations = 1000
    neighbourhood = 20
    print(f"No arguments attempted to be passed, running for default parameters: \n"
          f"{num_of_agents} Agents, {num_of_wolves} Wolves, "
          f"{num_of_iterations} iterations, neighbourhood of {neighbourhood}"
          f"\n")    
# If an incorrect number of parameters are passed, revert to sys_args function
else:
    print("Incorrect number of arguments passed, please enter:")
    num_of_agents, num_of_wolves, num_of_iterations, neighbourhood = functions.sys_args()


# Ask user if they want to visualise animation
attempts = 0
while True:
    try:
        plot = str(input("Do you want to visualise the animation? Y/N: "))
        break
    except ValueError:
        attempts += 1
        if attempts < 3:
            print("Please enter: Y/N")
            continue
        else:
            print("Failed to pass argument correctly, visualisation will be made.")
            plot = 'Y'
            break


# read in data as a list of lists
environment = []
with open('in.txt', 'r') as file_for_reading:
    for row in file_for_reading:
        rowlist = row.split(',')
        rowlisty = list(map(int, rowlist))
        environment.append(rowlisty)


# initialize variables
agents = []                     # list of agents
wolves = []                     # list of wolves
infants = []                    # list of infants
leny = len(environment[1])      # length of y-axis as determined from the environment
lenx = len(environment)         # length of x-axis as determined from the environment
carry_on = True                 # boolean for stopping functions            
fig = plt.figure(figsize=(7, 7))    
ax = fig.add_axes([0, 0, 1, 1])
env_total = sum(sum(x) for x in environment)      # sum of all values in environment
counter = 0  # counter for num_of_iterations
agents_pop = []
infants_pop = []

# make the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,
                                       neighbourhood))

# make the wolves
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolf(environment,
                                       neighbourhood))


# update function 
def update(misc):
    
    """
    Update function to be called at each frame, actions include:
        Agents and wolves will be made to interact with the environment and themselves
        Stopping conditions will be assessed
        Environment, wolves and agents will be plotted
    """

    fig.clear()  
    global carry_on
    global counter 
    global agents_pop
    global infants_pop
    
    # make agents interact 10 times for each function call 
    # this gives agents a chance to move and eat a sufficient amount
    for _interactions in range(10):
        random.shuffle(agents)
        for agent in agents:
            agent.move()
            agent.eat()
            # agent.sick()
            agent.share_with_neighbours(neighbourhood, agents)
            agent.have_infant(neighbourhood, agents, infants)
    
    # infant interactions
    for infant in infants:
        infant.move()
        infant.eat()
        
    agents_pop.append(len(agents))        
    infants_pop.append(len(infants))
            
    # move wolves and make them eat!
    for wolf in wolves:
        wolf.move()
        wolf.eat_agents(neighbourhood, wolves, agents)
        wolf.eat_infants(neighbourhood, wolves, infants)

    ### stopping conditions
    if sum(sum(x) for x in environment) < env_total*0.5:
        carry_on = False
        print("Stopping condition met - Environment depleted by %50")

    if len(agents) == 0:
        carry_on = False
        print("Stopping condition met - no sheep left!")
    
    if counter == (num_of_iterations):
        carry_on = False
        print("Stopping condition met - number of iterations reached")
    else:
        counter += 1

    # overlay agents, wolves and infants on plot of environment
    plt.xlim(0, lenx)
    plt.ylim(0, leny)
    plt.imshow(environment)
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.title('Agent based model')
    
    for agent in agents:
        plt.scatter(agent.x, agent.y, s=50, c = 'white', label = 'agents') 
    for wolf in wolves:
        plt.scatter(wolf.x, wolf.y, s=50, c = 'black', marker = '*', label = 'wolves')
    for infant in infants:
        plt.scatter(infant.x, infant.y, s=50, c = 'red', label = 'infants') 
    

# generator function to supply data to update function and each frame of animation
def gen_function(misc = []):
    global carry_on 
    while carry_on:
        yield counter


# animation 
animation = matplotlib.animation.FuncAnimation(fig, update, interval = 100, frames=gen_function, repeat=False)

# plot animation if instructed by user
if plot == 'Y' or plot == 'y' or plot == 'yes' or plot == 'YES' or plot == 'Yes':
    plt.show()
else:
    pass

"""
# write environment to file
f2 = open('env.txt', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)
f2.close()


# write wolves stores to file
f3 = open('stored.txt', 'w', newline='') 
writer = csv.writer(f3, delimiter=',')
for wolf in wolves:
    listy = []
    listy.append(wolf.store) 
    writer.writerow(listy)
f3.close()
"""

plt.plot(agents_pop)
plt.plot(infants_pop)
plt.ylabel('Population')
plt.show()





