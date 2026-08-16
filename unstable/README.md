# [WIP] The Basics of Kinematic Modeling and Control of Serial-link Manipulators Using `numpy`

> **Warning:** These are text-based (MyST) notebooks under active development. The canonical `.ipynb` versions remain in [`basic_lessons/`](../basic_lessons/).

This directory contains the same five-lesson tutorial as [`basic_lessons/`](../basic_lessons/) but converted to
[MyST text notebooks](https://mystmd.org/guide/notebooks-with-markdown). The content is identical; only the file format
has changed from `.ipynb` to `.md` with `{code-cell}` directives.

## Contents

| Number | Title and Link | Content |
|--------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | [](./lesson1_tutorial.md) | Basic operations in Python and `numpy` |
| 2 | [](./lesson2_tutorial.md) | Learn about elements and operations in $\mathbb{R}^n$, $SO(n)$, and $SE(n)$ with $n\in{\{2,3\}}$ related to positions, orientations, and poses, respectively. |
| 3 | [](./lesson3_tutorial.md) | Learn about the composition of rigid body motion in series to obtain the forward kinematics model of a robotic manipulator. |
| 4 | [](./lesson4_tutorial.md) | Learn about the first-order differential mapping $\dot{\myvec{x}}=\mymatrix{J}\dot{\myvec{q}}$ through the calculation of the Jacobian $\mymatrix{J}$. |
| 5 | [](./lesson5_tutorial.md) | Employ the previous knowledge in all previous lessons to employ a Lyapunov-stable control law to move a manipulator in task space using configuration-space signals. |

### Exercise Answers

| Lesson | Link |
|--------|------|
| L1 | [](./lesson1_exercise_answers.md) |
| L2 | [](./lesson2_exercise_answers.md) |
| L3 | [](./lesson3_exercise_answers.md) |
| L4 | [](./lesson4_exercise_answers.md) |
| L5 | [](./lesson5_exercise_answers.md) |