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


