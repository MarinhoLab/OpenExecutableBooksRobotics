---
title: Introduction
...

## Description

  In this five-lesson tutorial, we start from the very basics of scalar and matricial operations in Python using `numpy`,
  all the way until the basics of kinematic control. Until kinematic control, most is based on [@spong2020robot].

# Using this book

Each lesson is a [Jupyter notebook](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html). Each lesson can be
opened and executed with popular IDEs, such as [VSCode](https://code.visualstudio.com) and [PyCharm](https://www.jetbrains.com/pycharm/).
The reader is expected to follow it sequentially.

# Table of Contents

- [](./lesson1_tutorial.ipynb) \
  Basic operations in Python and `numpy`.
  
- [](./lesson2_tutorial.ipynb) \
  Learn about elements and operations in $\mathbb{R}^n$, $SO(n)$, and $SE(n)$ with $n\in{\{2,3\}}$ related to positions,
  orientations, and poses, respectively. 

- [](./lesson3_tutorial.ipynb) \
  Learn about the composition of rigid body motion in series to obtain the forward kinematics model of a robotic manipulator,
  mapping their configuration space $\myvec{q}\in\mathbb{R}^n$ into their task space $\myvec{x}\in\mathbb{R}^m$.

- [](./lesson4_tutorial.ipynb) \
  Learn about the first-order differential mapping $\dot{\myvec{x}}=\mymatrix{J}\dot{\myvec{q}}$ between joint space and 
  task space velocities through the calculation of the Jacobian $\mymatrix{J}$.

- [](./lesson5_tutorial.ipynb) \
  Employ the previous knowledge in all previous lessons to employ a Lyapunov-stable control law to move a manipulator
  in task space using configuration-space signals.