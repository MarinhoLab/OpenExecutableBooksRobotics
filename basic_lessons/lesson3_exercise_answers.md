---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# L3 Exercise Answers

*License: CC-BY-NC-SA 4.0*

*Author: Murilo M. Marinho (murilo.marinho@manchester.ac.uk)*

### I found an issue
Thank you! Please report it at https://github.com/MarinhoLab/OpenExecutableBooksRobotics/issues

### Latex Macros

# Valid imports

````{code-cell}
from math import pi, sin, cos
import numpy as np
````

# Exercises

## Exercise a

````{code-cell}
q_A0 = pi/4.0 # As given in the exercise
q_A1 = -0.1 # As given in the exercise

H_A0_A0p = np.array(
    [[cos(q_A0), -sin(q_A0), 0, 0],
    [sin(q_A0),  cos(q_A0), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]]
)

H_A0p_A0pp = np.array(
    [[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0.5],
    [0, 0, 0, 1]]
)

H_A0pp_A1 = np.array(
    [[1, 0, 0, 0],
    [0, cos(pi/2), -sin(pi/2), 0],
    [0, sin(pi/2),  cos(pi/2), 0],
    [0, 0, 0, 1]]
)

H_A1_A2 = np.array(
    [[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, q_A1],
    [0, 0, 0, 1]]
)


H_A0_A2 = H_A0_A0p @ H_A0p_A0pp @ H_A0pp_A1 @ H_A1_A2

# Printing the result is NOT a mandatory part of the answer.
print(f'H_A0_A2 = {H_A0_A2}')
````

## Exercise c

````{code-cell}
# All rotations are the same
H_Rz = np.array(
    [[cos(pi/5.0), -sin(pi/5.0),  0, 0],
     [sin(pi/5.0),  cos(pi/5.0),  0, 0],
     [0,          0,          1, 0],
     [0,          0,          0, 1]]
)

# All translations are the same
H_Tx = np.array(
    [[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0.25],
    [0, 0, 0, 1]]
)

H_C0_C3 = H_Rz @ H_Tx @ H_Rz @ H_Tx @ H_Rz @ H_Tx

# Printing the result is NOT a mandatory part of the answer.
print(f'H_C0_C3 = {H_C0_C3}')
````

# Challenge 1

````{code-cell}
# Consider manipulator DoFs as the length of the following lists.
# Consider it as the configuration space of the RRR...RRR robot
q = [pi/2, pi/10, -pi/10, pi/2] # Increase length of q if you'd like to check
l = [1, 2, 3, 4] # l must be same size of q

if len(q) != len(l):
    raise Exception("q and l are not the same length")

def link_rotation(qi):
    return np.array(
            [[cos(qi), -sin(qi),  0],
             [sin(qi),  cos(qi),  0],
             [0,         0,       1]])

def link_translation(li):
    return np.array(
            [[1, 0, li],
             [0, 1, 0],
             [0, 0, 1]])

H = np.eye(3)
for qi, li in zip(q, l):
    H = H @ link_rotation(qi) @ link_translation(li)

# Printing the result is NOT a mandatory part of the answer.
print(f"Final answer is {H}")
````
