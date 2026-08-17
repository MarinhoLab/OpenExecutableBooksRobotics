---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# L1 Exercise Answers

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

## Exercise 1

````{code-cell}
phi = pi/4.0

e1 = sin(phi) + 4 * cos(phi / 5)

# Printing the result is NOT a mandatory part of the answer.
print(f'e1 = {e1}')
````

## Exercise 2

````{code-cell}
A2 = np.array([[5, 2],
              [3, 5]])
B2 = np.array([[5, 3],
              [3, 8]])

C2 = A2 + B2 + (A2 @ B2) - (B2 @ A2)

# Printing the result is NOT a mandatory part of the answer.
print(f'C2 = {C2}')
````
