---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# L2 Exercise Answers

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
θ_a = pi/4.0

R_a =  np.array([[cos(θ_a),-sin(θ_a)],
                 [sin(θ_a), cos(θ_a)]])

# Printing the result is NOT a mandatory part of the answer.
print(f'R_a = {R_a}')
````

## Exercise b

````{code-cell}
θ_b1 = pi/12.0
θ_b2 = -pi/2.0

R_b1 =  np.array([[cos(θ_b1),-sin(θ_b1)],
                  [sin(θ_b1), cos(θ_b1)]])

R_b2 =  np.array([[cos(θ_b2),-sin(θ_b2)],
                  [sin(θ_b2), cos(θ_b2)]])

R_b = R_b1 @ R_b2

print(f'R_b = {R_b}')
````

## Exercise c

````{code-cell}
θ_c = pi/3.0
x_c = 2.0
y_c = 5.0

H_c1 = np.array([[cos(θ_c),-sin(θ_c), 0],
                 [sin(θ_c), cos(θ_c), 0],
                 [0,        0,        1]])

H_c2 = np.array([[1,0,x_c],
                 [0,1,y_c],
                 [0,0,1]])

H_c = H_c1 @ H_c2

print(f'H_c = {H_c}')
````

## Exercise d

````{code-cell}
θ_d = pi/3.0
x_d = 2.0
y_d = 5.0


H_d1 = np.array([[1,0,x_d],
                 [0,1,y_d],
                 [0,0,1]])

H_d2 = np.array([[cos(θ_d),-sin(θ_d), 0],
                 [sin(θ_d), cos(θ_d), 0],
                 [0,        0,        1]])


H_d = H_d1 @ H_d2

print(f'H_d = {H_d}')
````

`H_c` is *not* the same as `H_d`. This indicates that the order of operations matters. That is, sequential pose transformations are not commutative.

# Extra challenge 1

$$R = \left[\begin{array}{cc}
             \cos\left(\sin(t) + 2\cos(t)\right) & -\sin\left(\sin(t) + 2\cos(t)\right) \\
             \sin\left(\sin(t) + 2\cos(t)\right) & \cos\left(\sin(t) + 2\cos(t)\right)
        \end{array}\right].$$

````{code-cell}
t = 10.0

θ = sin(t) + 2 * cos(t)

R = np.array([[cos(θ),-sin(θ)],
              [sin(θ), cos(θ)]])
````

# Extra challenge 2

See DH parameters in lesson 3.

````{code-cell}
θ = pi/10.0
d = 0.3
a = 0.5
α = -pi/2.0

H1 = np.array(
    [[cos(θ), -sin(θ), 0, 0],
    [ sin(θ),  cos(θ), 0, 0],
    [ 0,       0,      1, 0],
    [ 0,       0,      0, 1]]
)

H2 = np.array(
    [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, d],
     [0, 0, 0, 1]]
)

H3 = np.array(
    [[1, 0, 0, a],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]
)

H4 = np.array(
    [[1, 0,       0,      0],
     [0, cos(α), -sin(α), 0],
     [0, sin(α),  cos(α), 0],
     [0, 0,       0,      1]]
)

H = H1 @ H2 @ H3 @ H4
````
