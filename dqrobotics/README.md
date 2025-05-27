# Kinematic modeling and control of serial-link robotic manipulators using `dqrobotics` Python: From zero to hero.

This executable book contains eight lessons representing serial-link manipulator modeling in dual quaternions using `dqrobobotics` described in http://doi.org/10.1109/MRA.2020.2997920. It is a derivative
work of a [`dqrobotics` MATLAB course](https://github.com/dqrobotics/learning-dqrobotics-in-matlab/tree/master/robotic_manipulators) from Murilo M. Marinho.

The theory used in this book is described in works such as [@adorno:tel-00641678], [@vilhenaadorno:hal-01478225], and https://doi.org/10.1109/TRO.2019.2920078.

# Using this book

Each lesson is a [Jupyter notebook](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html). Each lesson can be
opened and executed with popular IDEs, such as [VSCode](https://code.visualstudio.com) and [PyCharm](https://www.jetbrains.com/pycharm/).
The reader is expected to follow it sequentially.

# Contents

| Number | Title and Link                                                  | Content                                                                                                                                                                                                                                                      |
|--------|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | [](./lesson1/lesson_dq1_python_basics.ipynb)                    | The very basics of Python and `numpy`, including simple mathematical operations.                                                                                                                                                                             |
| 2      | [](./lesson2/lesson_dq2_quaternion_basics.ipynb)                | Representing and manipulating quaternions using `dqrobotics` Python. Unit quaternions are also introduced and used to represent the rotation of rigid bodies                                                                                                 |
| 3      | [](./lesson3/lesson_dq3_dual_quaternion_basics_part1.ipynb)     | Representing and manipulating dual quaternions using `dqrobotics` Python. Unit dual quaternions are introduced and used to represent the pose transformation of rigid bodies.                                                                                |
| 4      | [](./lesson4/lesson_dq4_dual_quaternion_basics_part2.ipynb)     | Unit dual quaternions are used to represent lines and planes. Distance functions between points, lines, and planes are also introduced                                                                                                                       |
| 5      | [](./lesson5/lesson_dq5_robot_control_basics_part1.ipynb)       | The basics of the kinematic control of serial-link robotic manipulators. Forward kinematics model, inverse kinematics model, task-space velocity and position control using a 1-DoF planar robot.                                                            |
| 6      | [](./lesson6/lesson_dq6_robot_control_basics_part2.ipynb)       | Modeling serial robots using the Denavit-Hartenberg (DH) parameters; the forward kinematics model using the DH parameters; the pose, rotation, translation Jacobians; translation, rotation, and pose task-space controlers; all using a 3-DoF planar robot. |
| 7      | [](./lesson7/lesson_dq7_robot_control_basics_part3.ipynb)       | Understanding and handling task-space singularities with a 7-DoF planar robot.                                                                                                                                                                               |
| 8      | [](./lesson8/lesson_dq8_optimization_based_robot_control.ipynb) | Revisiting the topic of kinematic control using mathematical optimization formulation, implement joint-space and task-space constraints using quadratic programming.                                                                                         |
