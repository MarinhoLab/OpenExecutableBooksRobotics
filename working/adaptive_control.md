---
file_format: mystnb
kernelspec:
  name: python3
  display_name: python3
---

# Installing

```{code-cell} ipython3
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

```{literalinclude} adaptive_control/example.py
:start-after: # IMPORT START
:end-before: # IMPORT END
```

# Usage

##