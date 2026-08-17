---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# L2 Rigid Body Motion

*License: CC-BY-NC-SA 4.0*

*Author: Murilo M. Marinho (murilo.marinho@manchester.ac.uk)*

### Prerequisites for the learner
The user of this notebook is expected to have prior knowledge in
- All the content and prerequisites of lesson 1.

### I found an issue
Thank you! Please report it at https://github.com/MarinhoLab/OpenExecutableBooksRobotics/issues

### Latex Macros

# Installing prerequisites

````{code-cell}
%pip install numpy
````

# Imports

````{code-cell}
import numpy as np
from math import pi, sin, cos
````

# Rigid bodies
If the relative transformation between all points of a given object remain the same regardless of motion, it is a rigid body.

In other words, the object has no flexibility and the motion of the entire body can be prescribed by its *position* and *orientation* with respect to a given *reference frame*.

This tends to be the initial topic of robotics textbooks. That is because we can use this to derive the equations of motion for many classes of robots and objects from first principles.

# Reference frames

Positions/translations and orientations/rotations of objects are always defined with respect to a reference frame. Reference frames can be attached to rigid bodies or at fixed locations in space. Reference frames are usually defined in such way to make the mathematical derivations simpler.

In this tutorial, the World (or neutral) reference frame has the following notation

$$\mathcal{F}.$$

**Unless otherwise stated, a given position/orientation/pose is given with respect to the World frame**. When other frames are needed we usually rely on notations such as $$\mathcal{F}',\mathcal{F}''$$ when frames are sequential or $$\mathcal{F}_a,\mathcal{F}_b$$ when relationships are more complex.

# 2D Position/translation

Positions/translations in 2D can be uniquely defined as any $$\myvec{p} \in \mathbb{R}^2.$$ Hence, if we would like to define 

$$\myvec{p} = \left[\begin{array}{ccc}
         x \\
         y
        \end{array}\right] =\left[\begin{array}{ccc}
         1 \\
         2
        \end{array}\right],$$

we can do so programmatically with the following piece of code.

<div class="alert alert-block alert-info">
It is common for column and row vectors to not be distinguishable in Python with <b>numpy</b>. That is in general convenient but can cause problems when the dimension is important, so always pay close attention to what each function expects as input.
</div>

````{code-cell}
p = np.array([1.0, 2.0])

print(f"p={p}")
````

## Composition of translations

Sequential translations, such as 

$$\mathbb{R}^2 \ni \myvec{p}_i = \left[\begin{array}{ccc}
         x_i \\
         y_i
        \end{array}\right],$$

with $$i \in \mathbb{N}$$ can be composed with sequential additions

$$\myvec{p} = \myvec{p}_{0} + \myvec{p}_{1} + \myvec{p}_{2} + \myvec{p}_{3}.$$

````{code-cell}
p0 = np.array([1.0, 2.0])
p1 = np.array([2.0, 3.0])
p2 = np.array([3.0, 4.0])
p3 = np.array([4.0, 5.0])

p = p0 + p1 + p2 + p3

print(f"p={p}")
````


## Inverse translation

The inverse translation can be obtained by subtractions and the element of no translation is the zero vector, that is, if we unwind all translations we're back to the origin of the reference frame

$$\myvec{p}' = \myvec{p} - \myvec{p}_{0} - \myvec{p}_{1} - \myvec{p}_{2} - \myvec{p}_{3} = \left[\begin{array}{ccc}
         0 \\
         0
        \end{array}\right].$$

````{code-cell}
p0 = np.array([1.0, 2.0])
p1 = np.array([2.0, 3.0])
p2 = np.array([3.0, 4.0])
p3 = np.array([4.0, 5.0])
p = p0 + p1 + p2 + p3

p_ = p - p0 - p1 - p2 - p3

print(f"p_={p_}")
````

# 2D orientation/rotation 

Orientations/rotations in 2D can be defined in many different ways. In this tutorial, we will address the special orthogonal group for two dimensions, i.e., SO(2). These rotations are defined, in this representation, as a matrix

$$\mymatrix{R} \in \mathbb{R}^{2 \times 2}.$$

The identity rotation means no rotation. For any frame $\mathcal{F}_a$,

$$\mymatrix{R}^{a}_{a} = \mymatrix{I}_2.$$

An element of SO(2) is simply a matrix with the correct properties, therefore we can define one directly in `numpy`. For

$$\mymatrix{R}(\theta) = \left[\begin{array}{ccc}
             \cos{\theta} & -\sin{\theta} \\
             \sin{\theta} & \cos{\theta} 
        \end{array}\right],$$

when $\theta = \frac{\pi}{2}$, we have the following equivalent piece of code.

````{code-cell}
θ = pi/2

R = np.array([[cos(θ),-sin(θ)],
              [sin(θ), cos(θ)]])

print(f"R={R}")
````

# 2D poses (combined translation/orientation)

2D poses can be represented using elements of SE(2). A translation followed by a rotation can be combined into a single $\mymatrix{H}\in\mathbb{R}^{3 \times 3}$ with the following structure

$$\mymatrix{H}(x,y,\theta) =
\left[\begin{array}{ccc}
             1 & 0 & x \\
             0 & 1 & y \\
             0 & 0 & 1
        \end{array}\right]
\left[\begin{array}{ccc}
             \cos{\theta} & -\sin{\theta} & 0 \\
             \sin{\theta} & \cos{\theta}  & 0 \\
             0            & 0             & 1
        \end{array}\right] =
\left[\begin{array}{ccc}
             \cos{\theta} & -\sin{\theta} & x \\
             \sin{\theta} & \cos{\theta}  & y \\
             0            & 0             & 1
        \end{array}\right].$$

<div class="alert alert-block alert-info">
The translation and rotation order is extremely important. Check the exercises at the end of this lesson.
</div>

For $\theta = \frac{\pi}{2}$, $x = 0.1$, and $y = 0.2$, we have the following equivalent piece of code.

````{code-cell}
θ = pi/2
x = 0.1
y = 0.2

H = np.array([[cos(θ),-sin(θ), x],
              [sin(θ), cos(θ), y],
              [0,      0,      1]])


print(f"H = {H}")
````

# 3D Position/translation

The 3D position/translations are a trivial extention of the 2D ones with one extra dimension.

$$\mathbb{R}^3 \ni \myvec{p}_i = \left[\begin{array}{ccc}
         x_i \\
         y_i \\
         z_i
        \end{array}\right].$$

There is nothing surprising in terms of properties, so we will move on to SO(3).

# 3D orientation/rotation 

For rotational matrices in 3D, we usually compose basic rotations. For rotations about the basis vectors, we have

$$\mymatrix{R}(z,\theta) = \left[\begin{array}{ccc}
             \cos{\theta} & -\sin{\theta} & 0 \\
             \sin{\theta} & \cos{\theta}  & 0 \\
             0            & 0             & 1
        \end{array}\right],$$

$$\mymatrix{R}(y,\theta) = \left[\begin{array}{ccc}
        \cos{\theta}   & 0 & \sin{\theta} \\
        0              & 1  & 0 \\
        -\sin{\theta}  & 0  & \cos{\theta}
\end{array}\right],$$

$$\mymatrix{R}(x,\theta) = \left[\begin{array}{ccc}
        1   & 0 & 0 \\
        0   &  \cos{\theta}  & -\sin{\theta} \\
        0  & \sin{\theta}  & \cos{\theta}
\end{array}\right].$$

````{code-cell}
Rz = np.array([[cos(θ),-sin(θ), 0],
               [sin(θ), cos(θ), 0],
               [0,      0,      1]])

Ry = np.array([[ cos(θ), 0, sin(θ)],
               [      0, 1, 0],
               [-sin(θ), 0, cos(θ)]])

Rx = np.array([[1,      0,  0],
               [0, cos(θ), -sin(θ)],
               [0, sin(θ),  cos(θ)]])

# A rotation about z
print(f"Rz={Rz}")

# A rotation about y
print(f"Ry={Ry}")

# A rotation about x
print(f"Rx={Rx}")
````

## Compositions of rotations in SO(3)

Compositions in SO(3) follow the same rules as SO(2), where sequential rotations are represented by right multiplications. For instance,

$$\mymatrix{R}^0_c = \mymatrix{R}^0_a\mymatrix{R}^a_b\mymatrix{R}^b_c.$$

This can be represented by the following equivalent piece of code using sample angles.

````{code-cell}
θ0_a = pi/4
R0_a = np.array([[cos(θ0_a),-sin(θ0_a), 0],
               [sin(θ0_a), cos(θ0_a), 0],
               [0,      0,        1]])

θa_b = -pi/2
Ra_b = np.array([[ cos(θa_b), 0, sin(θa_b)],
                 [         0, 1, 0],
                 [-sin(θa_b), 0, cos(θa_b)]])

θb_c = pi/8
Rb_c = np.array([[1,         0,  0],
                 [0, cos(θb_c), -sin(θb_c)],
                 [0, sin(θb_c),  cos(θb_c)]])

R0_c = R0_a @ Ra_b @ Rb_c
print(f"R0_c={R0_c}")
````

## Inverse rotations in SO(3)

Inverse operations in SO(3) are analogous to the inversions in SO(2), which are simply matrix transpositions.

For example, we can recover $\mymatrix{R}^0_a$ from $\mymatrix{R}^0_c$ using inverse relative rotations as follows.

$$\begin{align}
\mymatrix{R}^0_a &= \mymatrix{R}^0_c \mymatrix{R}^c_b \mymatrix{R}^b_a \\
\mymatrix{R}^0_a &= \mymatrix{R}^0_c (\mymatrix{R}^b_c)^T (\mymatrix{R}^a_b)^T \\
\end{align}$$

In the example code below, we store this alternative calculation in `R0_a_` to compare it with `R0_a`.

````{code-cell}
R0_a_ = R0_c @ Rb_c.T @ Ra_b.T

if np.allclose(R0_a, R0_a_):
    print('The results are pretty much the same!')
else:
    print('The results are too different.')
````

# 3D poses

In 3D, a translation followed by a rotation in the _current_ frame is represented with elements in SE(3). These elements are matrices $\mymatrix{H}\in\mathbb{R}^{4 \times 4}$ with the following structure

$$\mymatrix{H}(\myvec{t},\mymatrix{R}) =
\left[\begin{array}{ccc}
             \mymatrix{I} & \myvec{t} \\
             \myvec{0} & 1
        \end{array}\right]
\left[\begin{array}{ccc}
             \mymatrix{R} & \myvec{0} \\
             \myvec{0} & 1
        \end{array}\right] =
\left[\begin{array}{ccc}
             \mymatrix{R} & \myvec{t} \\
             \myvec{0} & 1 
        \end{array}\right].$$

<div class="alert alert-block alert-info">
The translation and rotation order is extremely important.
</div>

## Sequential pose transformations

We can also perform pose transformations using sequential right multiplications when they are with respect to the _current_ frame. Note also that we can verify the lack of commutativity on these transformations.

For example, consider a translation in 3D along the _World_ frame, represented by the homogeneous transformation matrix below.

$$\mymatrix{H}^0_a = \mymatrix{H}_a = \left[\begin{array}{ccc}
                                         1 & 0 & 0 & 1 \\
                                         0 & 1 & 0 & 2 \\
                                         0 & 0 & 1 & 3 \\
                                         0 & 0 & 0 & 1
                                       \end{array}\right].$$

Consider a rotation in 3D about the _current_ frame, represented by the homogeneous transformation matrix below.

$$\mymatrix{H}^a_b = \left[\begin{array}{ccc}
                     \cos{\theta_{ab}} & -\sin{\theta_{ab}} & 0 & 0 \\
                     \sin{\theta_{ab}} & \cos{\theta_{ab}}  & 0 & 0 \\
                     0                 & 0                  & 1 & 0 \\
                     0                 & 0                  & 0 & 1
        \end{array}\right].$$

We can calculate their sequential combination as follows.

$$\mymatrix{H}^0_b = \mymatrix{H}_b = \mymatrix{H}_a\mymatrix{H}^a_b$$

We can compute this result with $\theta_{ab} = \frac{\pi}{4}$ as shown in the piece of code below. We also show that

$$\mymatrix{H}_a\mymatrix{H}^a_b \neq \mymatrix{H}^a_b\mymatrix{H}_a,$$

further reinforcing the importance of the order of operations.

````{code-cell}
# An SE(3) translation
x = 1 # distance in metres
y = 2 # distance in metres
z = 3 # distance in metres

H0_a =  np.array([[1, 0, 0, x],
                  [0, 1, 0, y],
                  [0, 0, 1, z],
                  [0, 0, 0, 1]])

# An SE(3) rotation
θab = pi/4 # angle in radians

Ha_b = np.array([[cos(θab), -sin(θab), 0,  0],
                 [sin(θab),  cos(θab), 0,  0],
                 [0,         0,        1,  0],
                 [0,         0,        0,  1]])

# H0_a then Ha_b
H0_b = H0_a @ Ha_b

# Ha_b then Ha
H_wrong = Ha_b @ H0_a

if np.isclose(H0_b,H_wrong).all():
    print('The results are close!')
else:
    print('The results are far, therefore the operation is not commutative')
````

## Inverse transformations

As you have learned in theory, the inverse transformation can be found as

$$\mymatrix{H^{-1}}(\myvec{t},\mymatrix{R}) = \left[\begin{array}{ccc}
             \mymatrix{R}^T & -\mymatrix{R}^T\myvec{t} \\
             \myvec{0} & 1 
        \end{array}\right],$$

so it is important to remember to _never_ invert the matrix with general matrix inversion algorithms. Using the matricial properties leads to a simpler, faster, and more accurate inversion. The only "trick" is to obtain the submatrix corresponding to the rotation matrix.

````{code-cell}
# Extract R from H
R0_b = H0_b[0:3,0:3] # The 3x3 Rotation matrix
t0_b = H0_b[0:3,3].reshape((3,1)) # The 3x1 translation vector at the fourth column. Reshape it into a column vector.

A =  R0_b.T
B = -R0_b.T @ t0_b
C = np.array([0,0,0])
D = np.array([1])

# This is how you can use `np.block` to build a matrix like so
# | A B |
# | C D |
H0_b_inv = np.block([[A, B],
                     [C, D]])

print(f"H0_b_inv={H0_b_inv}")

print(f"H0_b @ H0_b_inv = {H0_b @ H0_b_inv}")
````

# Exercises

Consider that the `numpy` and `math` modules are already imported as shown earlier in this lesson.

## Exercise a

For $\theta_a = \frac{\pi}{4}$, calculate

$$\mymatrix{R}^0_{a} = \mymatrix{R}_{a} = R(\theta_a) \in SO(2)$$

and store it in the variable `R_a` shown in the cell below.

````{code-cell}
θ_a = pi/4.0 # As given in the exercise

R_a = None # Replace None with your solution to this exercise.
````

## Exercise b

Calculate the result of a rotation of $\theta_{b1} = \frac{\pi}{12}$ followed by a rotation of $\theta_{b2} = -\frac{\pi}{2}$, in the _current_ frame, using elements of SO(2).

Store the result in the variable `R_b` shown in the cell below.

````{code-cell}
θ_b1 = pi/12.0 # As given in the exercise
θ_b2 = -pi/2.0 # As given in the exercise

R_b = None # Replace None with your solution to this exercise.
````

## Exercise c

Consider the translation

$$\myvec{p}_c = \left[\begin{array}{ccc}
         x_c \\
         y_c
        \end{array}\right],$$

and the rotation

$$R(\theta_c) = \left[\begin{array}{ccc}
             \cos{\theta_c} & -\sin{\theta_c} \\
             \sin{\theta_c} & \cos{\theta_c}
        \end{array}\right].$$

Starting at the World frame, calculate the homogeneous transformation representing the rotation $R(\theta_c)$, about the _World_ frame, followed by the translation $\myvec{p}_c$, in the _current_ frame.

Consider $\theta_c = \frac{\pi}{3}$, $x_c = 2$, $y_c = 5$, and store the result in the variable `H_c` shown in the cell below.

````{code-cell}
θ_c = pi/3.0 # As given in the exercise
x_c = 2.0 # As given in the exercise
y_c = 5.0 # As given in the exercise

H_c = None # Replace None with your solution to this exercise.
````

## Exercise d

Consider the same variables as in `Exercise c` by replacing the subscripts with `d`. Calculate, instead, the translation followed by the rotation. Store the result in the variable `H_d` shown in the cell below.

Is `H_c` the same as `H_d`? What does that indicate?

````{code-cell}
θ_d = pi/3.0 # As given in the exercise
x_d = 2.0 # As given in the exercise
y_d = 5.0 # As given in the exercise

H_d = None # Replace None with your solution to this exercise.
````

# Extra challenge(s)
1. Let a rotation represented by a SO(2) element have a time-varying angle of $\theta(t) = \sin(t) + 2\cos(t)$.
    - Write down its general form in SO(2) so that all four elements are clearly visible.
    - Using this written down solution, compute the SO(2) representation at $t=10$.
2. Using SE(3) elements, calculate the final rigid body motion after four sequential transformations.
    - The first transformation is a rotation of $\theta=\frac{\pi}{10}$ about the $z$-axis of the _World_ frame.
    - The second transformation is a translation of $d=0.3$ about the $z$-axis of the _current_ frame.
    - The third transformation is a translation of $a=0.5$ about the $x$-axis of the _current_ frame.
    - The fourth and last transformation is a rotation of $\alpha=-\frac{\pi}{2}$ about the $x$-axis of the _current_ frame.
