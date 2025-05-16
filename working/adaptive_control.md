---
kernelspec:
  name: python3
  display_name: python3
---

# Adaptive Control with Partial or Complete Task-Space Measurements

This is an example implementation of the adaptive controller described in ()[http://doi.org/10.1109/TRO.2022.3181047].

## Installation

```{code-cell} ipython3
%pip install dqrobotics --pre
%pip install dqrobotics --pre --break-system-packages
%pip install marinholab-papers-tro2022-adaptivecontrol
%pip install marinholab-papers-tro2022-adaptivecontrol --break-system-packages
```

## Importing

```{attention}
  Currenlly, `dqrobotics` must be installed with the `--pre` flag. 
```

```{literalinclude} adaptive_control/example.py
:start-after: # IMPORT START
:end-before: # IMPORT END
```

## Usage

### Kinematic Model

In this implementation we rely on the object called `Example_SerialManipulatorEDH`. This object 
inherits from `DQ_SerialManipulator`. By `EDH`, it was meant `E`xtended `DH`, from which the 
parametric Jacobians can also be obtained.

```{note}
  In future stable versions of `dqrobotics`, this could inherit from `DQ_SerialManipulatorDH`.
```

```{literalinclude} adaptive_control/example.py
:start-after: # ROBOT RAW KINEMATICS START
:end-before: # ROBOT RAW KINEMATICS END
```

```{literalinclude} adaptive_control/example.py
:start-after: # MAIN START
:end-before: # MAIN END
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
%matplotlib inline
from adaptive_control.example import main
fig, ax = main()
plt.show()
```
