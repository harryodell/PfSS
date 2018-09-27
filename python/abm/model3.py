import random
import operator
import matplotlib.pyplot 
import agentframework
import matplotlib.animation 
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

# initialize 
num_of_agents = 10
num_of_iterations = 10000
neighbourhood = 20
agents = []
leny = len(environment[1])
lenx = len(environment)
carry_on = True
 
# make the agents using list comp
agents = [agentframework.Agent(environment, agents, neighbourhood) for n in range(num_of_agents)]

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
totalenv = sum(sum(x) for x in environment)

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
            
    if sum(sum(x) for x in environment) < totalenv*0.98:
        carry_on = False
        print("Stopping condition met - Environent depleted")
        
        
    # plot agents on grid
    matplotlib.pyplot.xlim(0, lenx)
    matplotlib.pyplot.ylim(0, leny)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y, s=50)

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on):
        yield a			# Returns control and waits next call.
        a += 1
    else:
        print("Stopping condition met - Max iterations reached")
        

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations) 
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()
















