# TODO

## Known issues in `dqrobotics` lessons

1. Originally, the lessons written in `MATLAB` did not allow the use of latex macros. This means that the conversion from those to Jupyter notebooks brought notation as-is, which is not entirely compliant with the [latest notation](https://github.com/IncompleteGuides/lyx-macros). This is a very time consuming task so it will only be attempted with community support or further funding sources.
1. The current `plot` method using `dqrobotics-pyplot` in the Jupyter notebook is generating a phantom image besides the animation videos. There are instructions online that allow us to tackle this issue, but I haven't been able to find one
that properly shows the video but not the image.

## Text-based notebooks

- Converting from traditional Jupyter notebooks to text-based notebooks might be an interesting topic to explore. See
  [link](https://myst-nb.readthedocs.io/en/latest/authoring/text-notebooks.html#authoring-text-notebooks). Classic notebooks
  store cell output on itself, with implications on version control software. While classic Jupyter notebooks are more
  easily usable without extensions, `jupytext` seemingly allows for the conversions. See [link](https://jupyterbook.org/en/stable/file-types/myst-notebooks.html).