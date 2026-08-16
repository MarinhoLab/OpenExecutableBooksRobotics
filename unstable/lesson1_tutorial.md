---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# L1 A quick Python refresher

*License: CC-BY-NC-SA 4.0*

*Author: Murilo M. Marinho (murilo.marinho@manchester.ac.uk)*

### Prerequisites
The user of this notebook is expected to have prior knowledge in
- Basic Python [[Tutorial]](https://docs.python.org/3/tutorial/index.html)
- Numpy 
    - [[Tutorial: basics for beginners]](https://numpy.org/doc/stable/user/absolute_beginners.html)
    - [[Tutorial: for MATLAB users]](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)
- Jupyter Notebook Basics [[Tutorial]](https://docs.jupyter.org/en/latest/)

### I found an issue
Thank you! Please report it at https://github.com/MarinhoLab/OpenExecutableBooksRobotics/issues

### Latex Macros

# A quick Python refresher

## Variable assignment 

Let

$$a\triangleq 10,b\triangleq 5.$$

We can replicate the above in Python with

````{code-cell}
a = 10
b = 5
````

## Output variables
Variables can be output using `print`. For example, for $a$

````{code-cell}
print(a)
````


### Output text and variables using f-strings
To output $a$ and $b$ within a string, we can use `print` and f-strings as follows

````{code-cell}
print(f'The value of a = {a} and b = {b}.')
````

# Basic Arithmetics

Basic mathematical operations are trivially performed as follows.

#### Sum

$$c = a + b.$$

````{code-cell}
c = a + b

print(f'c={c}')
````

#### Subtraction
$$c = a - b.$$

````{code-cell}
c = a - b

print(f'c={c}')
````

#### Multiplication
$$c=ab$$

````{code-cell}
c = a * b

print(f'c={c}')
````

#### Division
$$c = \frac{a}{b}$$

````{code-cell}
c = a / b

print(f'c={c}')
````

### Exponentiation
$$c = a^{b}$$

````{code-cell}
c = a ** b

print(f'c={c}')
````

### Math functions

For the following functions, we will need Python's built-in `math` module.

````{code-cell}
from math import sqrt, exp, log, pi, sin, cos, tan
````

### Square root

$$c = \sqrt{a}$$

````{code-cell}
c = sqrt(a)
````

### n-th root
The nth root,

$$c= \sqrt[n]{a}, n \in \mathbb{N},$$

does not seem to have a shorthand version in Python, but can be computed through simple properties such as

$$c = \sqrt[n]{a} = a^{\frac{1}{n}} = e^{\frac{ln(a)}{n}}.$$

For example, suppose that

$$n = 3.$$ 

Then,

````{code-cell}
n=3
````

and we can calculate the n-th root like so

````{code-cell}
# n-th root using fractional exponent. Might be easier but most languages do not support a similar syntax
c = a ** (1/n)

print(f'c={c}')
````

or like so

````{code-cell}
c = exp(log(a)/n)

print(f'c={c}')
````

and both should output the same value.

### Trigonometric functions

$$ \phi = \frac{\pi}{4},$$
$$ s_{\phi} = \sin \left( \phi \right),$$
$$ c_{\phi} = \cos \left( \phi \right),$$
$$ t_{\phi} = \tan \left( \phi \right).$$

````{code-cell}
phi = pi/4.0
s_phi = sin(phi)
c_phi = cos(phi)
t_phi = tan(phi)

print(f'phi={phi}')
print(f's_phi={s_phi}')
print(f'c_phi={c_phi}')
print(f't_phi={t_phi}')
````

# Linear Algebra with Numpy

### Installing the library

Just in case `numpy` is not already installed, we can install it with the following command. Nothing will happen if the library is already installed.

````{code-cell}
%pip install numpy 
%pip install numpy --break-system-packages
````

### Importing the library

````{code-cell}
import numpy as np
````

### Instantiating vectors
A row vector can be instantiated from a list of lists. For instance, for 
$$\myvec{v} = \left[\begin{array}{ccc}
         1 & 2 
        \end{array}\right],
$$ 
we have

````{code-cell}
# Note the double [[]] to instanteate a vector with explicit row shape.
v = np.array([[1, 2]])

print(f'v={v}')
````

A column vector can be instantiated from a list of singleton *lists*. For instance, for 
$$\myvec{u} = \left[\begin{array}{ccc}
         1 \\
         2
        \end{array}\right],$$ 
we have

````{code-cell}
# Note that each row is defined by a single element within a [], while the whole vector is within an external []
u = np.array([[1],
              [2]])

print(f'u={u}')
````

### Dot product

$$\myvec{c} = <\myvec{u},\myvec{u}>$$ 

````{code-cell}
c = np.vdot(u,u)

print(f'c={c}')
````

### Cross product

Cross product is defined for vectors in $\mathbb{R}^3$.

For example, for 

$$\myvec{u}_3 = \left[\begin{array}{ccc}
         1 \\
         2 \\
         3
        \end{array}\right],$$ 

and

$$\myvec{v}_3 = \left[\begin{array}{ccc}
         4 \\
         5 \\
         6
        \end{array}\right],$$ 

we can obtain the cross product

$$\myvec{c} = \myvec{u}_3 \times \myvec{v}_3$$ 

````{code-cell}
u3 = np.array([[1, 2, 3]])
v3 = np.array([[4, 5, 6]])

c = np.cross(u3,v3)

print(f'c={c}')
````

### Euclidean norm

$$\myvec{c} = ||\myvec{u}||$$ 

<div class="alert alert-block alert-info">
Note that the function is np.<b>linalg</b>.norm, as the norm calculation is within the module <b>linalg</b>.
</div>

````{code-cell}
c = np.linalg.norm(u)

print(f'c={c}')
````

### Instantiating matrices
For instance, suppose that we want to instantiate two real square matrices
$$\mymatrix{A} = \left[\begin{array}{ccc}
         1 & 2 \\
         3 & 4 
        \end{array}\right],
\mymatrix{B} = \left[\begin{array}{ccc}
        5 & 6 \\
        7 & 8 
        \end{array}\right] 
$$

````{code-cell}
A = np.array([[1, 2], 
              [3, 4]])
B = np.array([[5, 6], 
              [7, 8]])

print(f'A={A},\n\nB={B}')
````

### Transpose

$$\mymatrix{C} = \mymatrix{A}^T$$ 

````{code-cell}
C = A.T

print(f'C={C}')
````

### Sum

$$ \mymatrix{C} = \mymatrix{A} + \mymatrix{B} $$

````{code-cell}
C = A + B

print(f'C={C}')
````

### Subtraction

$$ \mymatrix{C} = \mymatrix{A} - \mymatrix{B} $$

````{code-cell}
C = A - B

print(f'C={C}')
````

### Matrix multiplication

For instance,
$$C = AB$$
is implemented with

<div class="alert alert-block alert-info">
The matrix multiplication operator, <b>@</b>, is very unusual. Pay close attention.
Mistaking this can be a major source of bugs and confusion.
</div>

````{code-cell}
C = A @ B # Alternatively C = np.matmul(A,B), but that is too verbose

print(f'C={C}')
````

which will naturally work for the vectors we defined. For example
$$\myvec{c} = \myvec{u}\myvec{v} = \left[\begin{array}{ccc}
         1 & 2 \\
         2 & 4 
        \end{array}\right],
$$
$$ \myvec{d} = \myvec{v}\myvec{u} = 5.
$$

````{code-cell}
c = u @ v 
d = v @ u 

print(f'c={c},\n\nd={d}')
````

and, of course, matrices and vectors

$$ \myvec{c} = \myvec{A}\myvec{u} $$

<div class="alert alert-block alert-info">
We only use the "." sign to denote matrix multiplication when otherwise it would be difficult to read the equation.
</div>

````{code-cell}
c = A @ u 

print(f'c={c},\n')
````

### Diagonal matrices

Diagonal matrices get increasingly sparse with size, so it is important to have shorthand commands for creating them. For instance, suppose that we have the following diagonal matrix

$$\mymatrix{D} = \left[\begin{array}{ccc}
         1 & 0 & 0 \\
         0 & 2 & 0 \\
         0 & 0 & 3   
        \end{array}\right] ,
$$

this can be instantiated in `numpy` with

````{code-cell}
D = np.diag([1, 2, 3])

print(f'D={D}.')
````

### Identity matrix

Among frequently used diagonal matrices, the identity matrix appears frequently. For instance, 

$$ \mymatrix{I}_3 = \left[\begin{array}{ccc}
         1 & 0 & 0 \\
         0 & 1 & 0 \\
         0 & 0 & 1   
        \end{array}\right],
$$ 

can be instantiated in `numpy` with

````{code-cell}
I_3 = np.eye(3)

print(f'I_3={I_3}.')
````

### Zero matrix

Another frequently used matrix is the zero matrix. For instance,

$$ \mymatrix{O}_3 = \left[\begin{array}{ccc}
         0 & 0 & 0 \\
         0 & 0 & 0 \\
         0 & 0 & 0   
        \end{array}\right],
$$ 

<div class="alert alert-block alert-info">
The <b>np.zeros</b> function takes a tuple to generate a properly sized matrix. Do not confuse it with <b>np.eye</b> that accepts a scalar.
</div>

````{code-cell}
O_3 = np.zeros((3,3))

print(f'O_3={O_3}.')
````

# Exercises

## Exercise 1

For $\phi = \pi/4$, let

$$ e_1 = \sin(\phi) + 4\cos(\frac{\phi}{5}).$$

Using the `math` module which is already imported, calculate the value of $e_1$ and store it in the variable `e1` shown in the cell below.

````{code-cell}
e1 = None # Replace None with your solution to this exercise.
````

## Exercise 2

Given

$$\mymatrix{A}_2 = \left[\begin{array}{ccc}
         5 & 2 \\
         3 & 5
        \end{array}\right]$$
and
$$
\mymatrix{B}_2 = \left[\begin{array}{ccc}
        5 & 3 \\
        3 & 8
        \end{array}\right].$$

Let
$$\mymatrix{C}_2 = \mymatrix{A}_2 + \mymatrix{B}_2 + \mymatrix{A}_2\mymatrix{B}_2 - \mymatrix{B}_2\mymatrix{A}_2.$$

Using the numpy module which is already imported, calculate the value of $\mymatrix{C}_2$ and store it in the variable `C2` shown in the cell below.

````{code-cell}
C2 = None # replace None with your solution to this exercise.
````
