---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# L4 Exercise Answers

*License: CC-BY-NC-SA 4.0*

*Author: Murilo M. Marinho (murilo.marinho@manchester.ac.uk)*

## I found an issue
Thank you! Please report it at https://github.com/MarinhoLab/OpenExecutableBooksRobotics/issues


# Valid imports

````{code-cell}
from math import pi, sin, cos
import numpy as np
````

# Exercises

## Exercise a

First, we calculate FKM by hand. You'll notice that it is given by the equation below.
$$\mymatrix{H}^{0}_{3} = \left[\begin{array}{ccc}
         c_{012} & -s_{012} & l_{0}c_0 + l_{1}c_{01} + l_{2}c_{012}\\
         s_{012} & c_{012}  & l_{0}s_0 + l_{1}s_{01} + l_{2}s_{012}\\
         0                  & 0                  & 1
        \end{array}\right].$$

We don't need to compute it explicitly, we just need the task-space values.

$$\begin{align}
p_{x}&=l_{0}c_0 + l_{1}c_{01} + l_{2}c_{012} \\
p_{y}&=l_{0}s_0 + l_{1}s_{01} + l_{2}s_{012} \\
\phi&=q_0 + q_1 + q_2.\\
\end{align}$$

Then, take the derivative to find the Jacobian.

$$\mymatrix{J} = \left[\begin{array}{ccc}
         -l_{0}s_0 - l_{1}s_{01} - l_{2}s_{012} & - l_{1}s_{01} - l_{2}s_{012} & - l_{2}s_{012} \\
         l_{0}c_0 + l_{1}c_{01} + l_{2}c_{012} & l_{1}c_{01} + l_{2}c_{012}  & l_{2}c_{012}\\
         1                 & 1                  & 1
        \end{array}\right].$$

````{code-cell}
q_0 = pi/4.0
q_1 = -pi/8.0
q_2 = pi/12.0

l_0 = 1
l_1 = 1
l_2 = 1

c0 = cos(q_0)
c01 = cos(q_0 + q_1)
c012 = cos(q_0 + q_1 + q_2)

s0 = sin(q_0)
s01 = sin(q_0 + q_1)
s012 = sin(q_0 + q_1 + q_2)

# Task space
p_x = l_0 * c0 + l_1 * c01 + l_2 * c012
p_y = l_0 * s0 + l_1 * s01 + l_2 * s012
phi = q_0 + q_1 + q_2

# Jacobian
J_1_1 = - l_0 * s0 - l_1 * s01 - l_2 * s012
J_1_2 = - l_1 * s01 - l_2 * s012
J_1_3 = - l_2 * s012

J_2_1 = l_0 * c0 + l_1 * c01 + l_2 * c012
J_2_2 = l_1 * c01 + l_2 * c012
J_2_3 = l_2 * c012

J_3_1 = 1
J_3_2 = 1
J_3_3 = 1

J = np.array(
        [[J_1_1, J_1_2, J_1_3],
         [J_2_1, J_2_2, J_2_3],
         [J_3_1, J_3_2, J_3_3]]
)

print(f"The analytical Jacobian at q_0={q_0}, q_1={q_1}, and q_2={q_2} is \n J={J}")
````

## Exercise b

Suppose that we have a `PP` robot defined by the following transformations:
- a translation of $q_0$ along the $x-$axis of the base frame.
- a rotation of 90 degrees with respect to the current frame.
- a translation of $q_1$ along the $x-$axis of the current frame.


First, we calculate FKM by hand. You'll notice that it is given by the equation below.
$$\mymatrix{H}^{0}_{3} = \left[\begin{array}{ccc}
         0 & -1 & q_0\\
         1 &  0 & q_1\\
         0 &  0 & 1
        \end{array}\right].$$

We don't need to compute it explicitly, we just need the task-space values.

$$\begin{align}
p_{x}&= q_0 \\
p_{y}&= q_1 \\
\phi&= \frac{\pi}{2}.\\
\end{align}$$

Then, take the derivative to find the Jacobian.

$$\mymatrix{J} = \left[\begin{array}{cc}
         1 & 0\\
         0 & 1\\
         0 & 0
        \end{array}\right].$$

````{code-cell}
# Jacobian is trivial so we don't need to compute each term separately.
# As you can see, in this example, it the Jacobian always has the same value.
J = np.array(
        [[1, 0],
         [0, 1],
         [0, 0]]
)
print(f"The analytical Jacobian is always\n J={J}")
````

# Challenge 1

To solve this challenge, we notice the patterns in the computation. You can change to the same link values of exercise a to test that this is correct.

````{code-cell}
# Consider manipulator DoFs as the length of the following lists.
# Consider it as the configuration space of the RRR...RRR robot
q = [pi/4.0, -pi/8.0, pi/12.0, -pi/3.0] # Increase length of q if you'd like to check
l = [1, 1, 1, 1] # l must be same size of q

if len(q) != len(l):
    raise Exception("q and l are not the same length")

def c_n(q, n_frame):
    """
    Get cos(q_0 + q_1 + ... + q_n).
    """
    q_sum = 0
    c_result = 0
    for i in range(n_frame+1):
        qi = q[i]
        q_sum += qi # First will be q_0, then q_0 + q_1, then...
        c_result = cos(q_sum) # First will be cos(q_0), then cos(q_0 + q_1), then...
    return c_result

def s_n(q, n_frame):
    """
    Get sin(q_0 + q_1 + ... + q_n).
    """
    q_sum = 0
    s_result = 0
    for i in range(n_frame+1):
        qi = q[i]
        q_sum += qi # First will be q_0, then q_0 + q_1, then...
        s_result = sin(q_sum) # First will be sin(q_0), then sin(q_0 + q_1), then...
    return s_result

def px_n(q, l, n_frame):
    """
    Get l_0*cos(q_0) + l_1*cos(q_0 + q_1) + ... + l_n*cos(q_0 + q_1 + ... + q_n).
    """
    px = 0
    for i in range(n_frame + 1):
        li = l[i]
        px += li * c_n(q, i)
    return px

def py_n(q, l, n_frame):
    """
    Get l_0*sin(q_0) + l_1*sin(q_0 + q_1) + ... + l_n*sin(q_0 + q_1 + ... + q_n).
    """
    py = 0
    for i in range(n_frame + 1):
        li = l[i]
        py += li * s_n(q, i)
    return py


def j_n(q, l, n_frame):
    """
    Construct the n-th column of the Jacobian matrix.
    """
    N = len(q)

    pnx = px_n(q, l, n_frame-1) # starts at 0
    pny = py_n(q, l, n_frame-1) # starts at 0
    pNx = px_n(q, l, N-1)
    pNy = py_n(q, l, N-1)

    px = pNx - pnx
    py = pNy - pny

    jn = np.array(
        [[-py],
          [px],
          [1]]
    )
    return jn

# Jacobian
J = j_n(q, l, 0)
for i in range(1,len(q)):
    J = np.hstack((J, j_n(q, l, i))) # We stack the columns horizontally
print(J)
````
