---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# L0 Setting up the virtual environment

*License: CC-BY-NC-SA 4.0*

*Author: Murilo M. Marinho (murilo.marinho@manchester.ac.uk)*

## Prerequisites for the learner
This lesson has no prerequisites. It is designed to be the first lesson in the course.

## I found an issue
Thank you! Please report it at https://github.com/MarinhoLab/OpenExecutableBooksRobotics/issues

# Introduction

Before starting with the lessons, you need to set up a suitable Python environment.
This lesson guides you through creating a Python virtual environment and installing all the dependencies required for this project.

A **virtual environment** is an isolated Python environment that allows you to install packages without affecting your system-wide Python installation. This ensures reproducibility and avoids dependency conflicts.

# Creating a virtual environment

The recommended approach is to use Python's built-in `venv` module. Open a terminal and run:

```bash
python3 -m venv venv
```

This creates a directory called `venv` in your current working directory containing the virtual environment.

# Activating the virtual environment

Before installing packages or running the notebooks, activate the virtual environment:

### Linux / macOS
```bash
source venv/bin/activate
```

### Windows (Command Prompt)
```cmd
venv\Scripts\activate.bat
```

### Windows (PowerShell)
```powershell
venv\Scripts\Activate.ps1
```

Once activated, your shell prompt should display `(venv)` to indicate the virtual environment is active.

# Installing the required packages

All lessons in this project use the following core dependencies:

- **numpy**: Numerical computing library for arrays, matrices, and linear algebra operations.
- **matplotlib**: Plotting library used in later lessons for visualisation.

Run the following command to install them:

```bash
pip install numpy matplotlib
```

# Verifying the installation

You can verify that the packages are correctly installed by running the cell below.

````{code-cell}
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

print(f'numpy version: {np.__version__}')
print(f'matplotlib version: {matplotlib.__version__}')
````

# Deactivating the virtual environment

When you are finished working, you can deactivate the virtual environment:

```bash
deactivate
```

# Summary

This lesson covered:

- Creating a Python virtual environment using `venv`.
- Activating and deactivating the virtual environment.
- Installing the required packages (`numpy` and `matplotlib`).
- Verifying the installation.

Now you are ready to proceed to [Lesson 1](./lesson1_tutorial.md).
