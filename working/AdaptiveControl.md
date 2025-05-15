---
file_format: mystnb
kernelspec:
  name: python3
  display_name: python3
---

# Installing

```{code-cell} ipython3
 :caption: Installing the library
%%capture
%pip install dqrobotics --pre
%pip install dqrobotics --pre --break-system-packages
%pip install marinholab-papers-tro2022-adaptivecontrol
%pip install marinholab-papers-tro2022-adaptivecontrol --break-system-packages
```

# Importing

```{attention}
  In a Jupyter notebook, you can wrap the import in a `try--except` block because the kernel does not always handle
  well the import from the dynamic library.
```

```{code-cell} ipython3
 :caption: Importing the library
try:
    from dqrobotics import *
    from marinholab.papers.tro2022.adaptive_control import *
except ImportError as e:
    print(f"In Jupyter notebooks, we sometimes have the `already registered` error. See error specifics: {e}")
```

# Usage

##