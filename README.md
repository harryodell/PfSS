# Programming for Social Sciences - ABM

This repository contains code pertaining to a simple agent based model (ABM) that simulates a scenario in which there are two defined agent classes - agents and wolves. Both classes are introduced to a limited virtual environment in which they move pseudo-randomly. As agents move around the environment, they display behaviours including eating, sharing their resources with neighbours and throwing up their resources. The wolves navigate the environment and eat sheep that they encounter within a user-defined neighbourhood. 

The simulation runs until one of three stopping conditions are met:

* The maximum number of iterations is met
* The sheep have depleted the overall value of the environment by 50%
* All the sheep have been eaten


## Motivation

The motivation behind this project was to fulfil the requirements for assessment 1 of the [GEOG5995 Programming for Social Scientists: Core Skills [Python] course](http://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/ "GEOG5995") at Leeds University. This is a one-week intensive course aimed at social scientists that want to learn how to program in Python. The course teaches basic Python along with useful elements and conventions within the core programming culture. 

For this assignment, it was required that we build a simple ABM, following on from an example provided in the course practicals. Additional and original contributions have been added including:

* The introduction of wolves to the model
* Providing the user with system arguments to initialize model parameters
* Inclusion of stopping conditions
* Removal of agents list as a constructor method to increase model efficiency



## ABM

### Running the model

The model runs from the command-line or terminal. The user should download or clone the repository and navigate (in the prompt) to the local directory. Then, the model runs as:

```python model.py [arg1=100] [arg2=10] [arg3=1000] [arg4=20]```

where the arguments are defined as:

* ```arg1```: number of agents
* ```arg2```: number of wolves
* ```arg3```: max number of iterations
* ```arg4```: neighbourhood distance in which sheep share resources and wolves can eat sheep

The arguments should be passed as integers, however, failing this the user will be given another opportunity. Given that no parameters are attempted to be passed or that the user has failed to pass the arguments correctly after three attempts, the model will revert to default parameters.

### Visualization prompt

Following the initialization of the model, the user will be asked to input whether they would like to see the visualization of the animation. We use ```matplotlib.animation.FuncAnimation()``` to make the animation - this function provides a plot of the current state of the model following each iteration and is recommended because of its use in helping the user understand the interactions within the model.

### Model outputs

When the model stops running, it can be assumed that a stopping criterion has been fulfilled - the user will see which one printed to the command line. 

Two files will then be written out to the same directory in which the code is in:

* ```out.txt```: a text file providing a copy of the state of the environment at the end of the simulation
* ```stored.txt``` a text file listing the stores of the wolves having consumed sheep and acquired their stores

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgemnts

Many thanks to Dr. Andy Evans for providing the material for the course and to his co-lecturers and teaching assistants for the delivery of the course. 
