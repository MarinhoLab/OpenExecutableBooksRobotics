# Open Executable Books in Robotics

## Link for the website

https://marinholab.github.io/OpenExecutableBooksRobotics/

## License
This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png

## This project has been funded by

|Duration        |Fund                      |Funder                          |
|----------------|--------------------------|--------------------------------|
|Aug 24 -  Jul 25| [Open Research Fellowship](https://manchester-uk.libanswers.com/OOR/faq/279379) | [Office for Open Research (UoM)](https://www.openresearch.manchester.ac.uk)  |

## Basic Lessons

These lessons are linked to the [Robotic Manipulators](https://www.manchester.ac.uk/study/masters/courses/list/20967/msc-robotics/course-details/EEEN62012#course-unit-details) course at UoM.

|Lesson|Title|
|------|-----|
|1|Python basics|
|2|Rigid body motion|
|3|Forward kinematics|
|4|Differential kinematics|
|5|Kinematic control|

## Changelog

### 2025

- I'm removing `spatialmath` from the tutorials and moving any old content to `legacy/spatialmath`. The original intention when adding this library was to facilitate more complex content in later parts of the module. With variable levels of programming knowledge in the standard cohort this is not possible, and the following issues were observed:
   - `spatialmath` not being available as binary package in many distributions, causing students to have to compile the `wheel` even when using `pip`. 
        - In Windows enviroments, for example, this means having a working VS Compiler installation which is not default and is beyond the scope of this module. 
        - In any distribution, this could take several minutes and even fail depending on student's enviroments.
   - Students tend to default to memorising the library functions instead of understanding the underlying mechanism, irrespective of how trivial the operations are. It is more pedagogical to rely on the matricial operations that they are expected to learn and reinforce that knowledge.

- Remove all mentions of `import` in sample code, and keep them to explicit and isolated import cells. Despite the clear indication in the text that the `import` statement was merely illustrative, novice readers often default to copying and pasting chunks of example code causing extraneous `import` statements that result in unprofessional code that, beyond aesthetics, can cause all sorts of issues.


## Advanced Lessons

Eight lessons representing the Python version of the course below, related to dual-quaternion algebra using [DQ Robotics](https://dqrobotics.github.io).

```
Kinematic modeling and control of serial-link robotic manipulators using DQ Robotics: From zero to hero.
```

|Number|Title|Content|
|---|---|---|
|1|*Python Basics*|The very basics of Python and `numpy`, including simple mathematical operations.|
|2|*Quaternion Basics*|Representing and manipulating quaternions using DQ Robotics Python. Unit quaternions are also introduced and used to represent the rotation of rigid bodies|
|3|*Dual Quaternion Basics (Part 1)*| Representing and manipulating dual quaternions using DQ Robotics Python. Unit dual quaternions are introduced and used to represent the pose transformation of rigid bodies.|
|4|*Dual Quaternion Basics (Part 2)*| Unit dual quaternions are used to represent lines and planes. Distance functions between points, lines, and planes are also introduced|
|5|*Robot Control Basics (Part 1)*| The basics of the kinematic control of serial-link robotic manipulators. Forward kinematics model, inverse kinematics model, task-space velocity and position control using a 1-DoF planar robot.|
|6|*Robot Control Basics (Part 2)*| Modeling serial robots using the Denavit-Hartenberg (DH) parameters; the forward kinematics model using the DH parameters; the pose, rotation, translation Jacobians; translation, rotation, and pose task-space controlers; all using a 3-DoF planar robot.|
|7|*Robot Control Basics (Part 3)*| Understanding and handling task-space singularities with a 7-DoF planar robot.|
|8|*Optimization-based Robot Control*| Revisiting the topic of kinematic control using mathematical optimization formulation, implement joint-space and task-space constraints using quadratic programming.|