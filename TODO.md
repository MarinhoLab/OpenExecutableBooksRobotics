# TODO

## Known issues in `dqrobotics` lessons

1. Originally, the lessons written in `MATLAB` did not allow the use of latex macros. This means that the conversion from those to Jupyter notebooks brought notation as-is, which is not entirely compliant with the [latest notation](https://github.com/IncompleteGuides/lyx-macros). This is a very time-consuming task, so it will only be attempted with community support or further funding sources.
2. The current `plot` method
   using `dqrobotics-pyplot` in the Jupyter notebook is generating a phantom image besides the animation videos.
   There are instructions online that allow us to tackle this issue, but I haven't been able to find one
that properly shows the video but not the image.
3. The latex macros in all lessons do not seem to render well in `jupyterlab`. It's not yet clear to me why.

## Text-based notebooks

- Converting from traditional Jupyter notebooks to text-based notebooks might be an interesting topic to explore. See
  [link](https://myst-nb.readthedocs.io/en/latest/authoring/text-notebooks.html#authoring-text-notebooks). Classic notebooks
  store cell output on themselves, with implications on version control software. While classic Jupyter notebooks are more
  easily usable without extensions, `jupytext` seemingly allows for the conversions. See [link](https://jupyterbook.org/en/stable/file-types/myst-notebooks.html).
- The so-called [paired notebooks](https://jupytext.readthedocs.io/en/latest/paired-notebooks.html) are possibly the solution. 
  Given that the latex macros sometimes do not render well in `jupyterlab`, this could become indirectly a solution.
  The latex support for `myst` is much less hacky, so it is likely that the notebooks exported from the text version
  are more likely to be compatible with `jupyterlab`.

## Notes

- `jupyterbook2` documentation is at https://next.jupyterbook.org.
