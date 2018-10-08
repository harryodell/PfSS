import random
import matplotlib
#matplotlib.use('macosx') 
import matplotlib.pyplot as plt
import agentframework
import matplotlib.animation 
import matplotlib.colors as colors
# %matplotlib qt
import sys

# System arguments 
def sys_args():
    """
    If the user inputs sytem arguments incorrectly when running model, 
    the user will be encouraged to input model parameters.
    
    Three attempts are allowed to input a correct value, failing this
    the default model paramter will be assigned.
    """
    
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
            num_of_agents, num_of_wolves, num_of_iterations, neighbourhood = sys_args()
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
    num_of_agents, num_of_wolves, num_of_iterations, neighbourhood = sys_args()


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


# initialie variables
agents = []                     # list of agents
wolves = []                     # list of wolves
leny = len(environment[1])      # length of y-axis as determined from the environment
lenx = len(environment)         # length of x-axis as determined from the environment
carry_on = True                 # carry on variable for stopping function             
fig = plt.figure(figsize=(7, 7))    # define fig size
ax = fig.add_axes([0, 0, 1, 1])
env_total = sum(sum(x) for x in environment)      # sum of all values in environment
colours = list(colors._colors_full_map.values()) # list of colours to assign to agents
counter = 0  # counter for num_of_iterations


# make the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,
                                       neighbourhood, colours))

# make the wolves
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolf(environment,
                                       neighbourhood))


# update function 
def update(blah):
    
    """
    Update function to be called at each frame, actions include:
        Agents and wolves will be made to interact with the environment and themselves
        Stopping conditions will be assessed
        Environment, wolves and agents will be plotted
    """
    # clear figure each time function runs
    fig.clear()  
    global carry_on
    global counter 
    
    # make agents interact 10 times for each function call 
    # this gives agents a chance to move and eat a sufficient amount
    for interactions in range(10):
        # shuffle order in which agents interact
        random.shuffle(agents)
        for agent in agents:
            agent.move()
            agent.eat()
            # agent.sick()
            agent.share_with_neighbours(neighbourhood, agents)
    
    # move wolves and make them eat!
    for wolf in wolves:
        wolf.move()
        wolf.eat_sheep(neighbourhood, wolves, agents)
            
    # stopping condition: if overall environment is depleted by %50
    if sum(sum(x) for x in environment) < env_total*0.5:
        carry_on = False
        print("Stopping condition met - Environment depleted by %50")

    # stopping condition: if all the sheep have been eaten    
    if len(agents) == 0:
        carry_on = False
        print("Stopping condition met - no sheep left!")
    
    # stopping condition: if iterations exceeded, stop and print to console
    if counter == (num_of_iterations):
        carry_on = False
        print("Stopping condition met - number of iterations reached")
    else:
        counter += 1

    # overlay agents and wolves on plot of environment
    plt.xlim(0, lenx)
    plt.ylim(0, leny)
    plt.imshow(environment)
    plt.ylabel('Y')
    plt.xlabel('X')
    for agent in agents:
        # plot agents as white dots
        plt.scatter(agent.x, agent.y, s=50, c = 'white') #c = agent.colours)
    for wolf in wolves:
        # plot wolves as black stars
        plt.scatter(wolf.x, wolf.y, s=50, c = wolf.colours, marker = '*')


# generator function to supply data to update function and each frame of animation
def gen_function(blah = [0]):
    global carry_on 
    while carry_on:
        yield counter

# animation function
animation = matplotlib.animation.FuncAnimation(fig, update, interval = 100, frames=gen_function, repeat=False)

if plot == 'Y' or plot == 'y' or plot == 'yes' or plot == 'YES' or plot == 'Yes':
    plt.show()
else:
    pass





