---
kernelspec:
  name: python3
  display_name: python3
---

# Adaptive Control with Partial or Complete Task-Space Measurements

This is an example implementation of the adaptive controller described in ()[http://doi.org/10.1109/TRO.2022.3181047].

## Installation

```{attention}
  Currently, `--break-system-packages` is added for compatibility. 
```

```{code-cell} ipython3
%%capture
%pip install matplotlib marinholab-papers-tro2022-adaptivecontrol
%pip install matplotlib marinholab-papers-tro2022-adaptivecontrol --break-system-packages
```

## Preamble

```{warning}
  This API is subject to change.
```

The implementation of the techniques described in the manuscript ()[http://doi.org/10.1109/TRO.2022.3181047] shown
herein is an **example**. This should be unequivocally understood from the prefix `Example_` added to all classes in 
this module. 

It is expected that this module will be an integral part of `dqrobotics`. When that does happen, it might be modified
both in obvious ways, such as the swap to the prefix `DQ_` and more subtle ways such as different ways to retrieve
parameters, variable names, and so on.

## Importing

```{literalinclude} adaptive_control/example.py
:start-after: # IMPORT START
:end-before: # IMPORT END
```

## Kinematic Model

In this implementation we rely on the object called `Example_SerialManipulatorEDH`. This object inherits from 
`DQ_SerialManipulator`. By `EDH`, it was meant `E`xtended `DH`, from which the parametric Jacobians can also be obtained.

```{note}
  In future stable versions of `dqrobotics`, `SerialManipulatorEDH` could inherit from `DQ_SerialManipulatorDH`.
```

This initialization is similar to what is done in `DQ_SerialManipulatorDH`.

```{literalinclude} adaptive_control/example.py
:start-after: # ROBOT RAW KINEMATICS START
:end-before: # ROBOT RAW KINEMATICS END
```

## Parameter Space

```{important}
  This section explains the main difference in the initialization of a `Example_SerialManipulatorEDH` in contrast
  with a `DQ_SerialManipulatorDH`. 
```

```{seealso}
  Section II.A of ()[http://doi.org/10.1109/TRO.2022.3181047] describes the configuration space and the parameter space.
  Table I is also useful.
```

The size of the configuration space {math}`\mathcal{Q}` of a robot is its degrees of freedom. Hence, for a {math}`n`-DoF
robot its Jacobians will have {math}`n` rows.

Differently from that, the parameter space {math}`\mathcal{A}` has a variable size depending on the parameters that
can be adapted. When using the DH convention, they can be, for instance, one of the four parameters for each of the 
joints. Each of which defined as part of the enumeration `Example_ParameterType`.

Each parameter must be specified as an instance of `Example_Parameter`. This object will store the information about
which link index it refers to, what `Example_ParameterType` it is, the current value of the parameter, and its boundaries.

A list of `Example_Parameter` is used as input for `Example_SerialManipulatorEDH.set_parameter_space()` so that the
instance of `Example_SerialManipulatorEDH` can properly calculate the parametric Jacobians for the parameters we chose.

```{note}
  The definition of each `Example_Parameter` in the list sent to `Example_SerialManipulatorEDH.set_parameter_space()` can
  be arbitrary. This means that the user has the freedom to choose any parameters of any joints in any order.
```

```{warning}
  The behavior of having duplicates of `Example_Parameter`, meaning the same index and type, is unspecified.
```

```{literalinclude} adaptive_control/example.py
:start-after: # PARAMETER SPACE START
:end-before: # PARAMETER SPACE END
```

## Main function

```{literalinclude} adaptive_control/example.py
:start-after: # MAIN START
:end-before: # MAIN END
```

## Running the example

```{code-cell} ipython3
import matplotlib.pyplot as plt
%matplotlib inline
from adaptive_control.example import main
fig, ax = main()
plt.show()
```
