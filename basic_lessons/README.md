# The Basics of Kinematic Modelling and Control of Serial-link Manipulators Using `numpy`

In this six-lesson tutorial, we start from the very basics of setting up your Python environment,
then cover scalar and matricial operations in Python using `numpy`,
all the way until the basics of kinematic control. Until kinematic control, most is based on [@spong2020robot].

## Using this book

Each lesson is a [MyST text notebook](https://mystmd.org/guide/notebooks-with-markdown). Each lesson can be
opened and executed with popular IDEs, such as [VSCode](https://code.visualstudio.com) and [PyCharm](https://www.jetbrains.com/pycharm/).
The reader is expected to follow it sequentially.

## Contents


| Number | Title and Link               | Content                                                                                                                                                                                                                                    |
|--------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0      | [](./lesson0_tutorial.md)    | Setting up the virtual environment and installing all required dependencies.                                                                                                                                                               |
| 1      | [](./lesson1_tutorial.md)    | Basic operations in Python and `numpy`                                                                                                                                                                                                     |
| 2      | [](./lesson2_tutorial.md)    | Learn about elements and operations in $\mathbb{R}^n$, $SO(n)$, and $SE(n)$ with $n\in{\{2,3\}}$ related to positions, orientations, and poses, respectively.                                                                              |
| 3      | [](./lesson3_tutorial.md)    | Learn about the composition of rigid body motion in series to obtain the forward kinematics model of a robotic manipulator, mapping their configuration space $\myvec{q}\in\mathbb{R}^n$ into their task space $\myvec{x}\in\mathbb{R}^m$. |
| 4      | [](./lesson4_tutorial.md)    | Learn about the first-order differential mapping $\dot{\myvec{x}}=\mymatrix{J}\dot{\myvec{q}}$ between joint space and task space velocities through the calculation of the Jacobian $\mymatrix{J}$.                                       |
| 5      | [](./lesson5_tutorial.md)    | Employ the previous knowledge in all previous lessons to employ a Lyapunov-stable control law to move a manipulator   in task space using configuration-space signals.                                                                     |

### Exercise Answers

| Lesson | Link |
|--------|------|
| L1 | [](./lesson1_exercise_answers.md) |
| L2 | [](./lesson2_exercise_answers.md) |
| L3 | [](./lesson3_exercise_answers.md) |
| L4 | [](./lesson4_exercise_answers.md) |
| L5 | [](./lesson5_exercise_answers.md) |