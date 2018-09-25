# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import math



### first agent
y0 = random.randint(0,100)
x0 = random.randint(0,100)

# random walk
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

# second random walk
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1





### second agent
y1 = random.randint(0,100)
x1 = random.randint(0,100)
# random walk
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

# second random walk
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1


print(y0, x0)
print(y1, x1)




#### find distance

distance = math.sqrt( (y1-y0)**2 + (x1-x0)**2 )
print(distance)


























