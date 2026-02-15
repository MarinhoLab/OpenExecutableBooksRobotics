# Making your own executable book 

```{warning}
  This notebook is a work in progress. This is based on `Jupyter Book 2.0` which is currently in alpha, meaning that
  it might change considerably before release.
```

```{seealso}
  - Jupyter book: https://next.jupyterbook.org
  - MyST: https://mystmd.org/guide/
```

## Dependencies

Remember to set a `venv` first. The Python policies are becoming evermore stringent in this regard.

```commandline
python -m venv venv
source venv/bin/activate
```

Installation can be done as follows.

```{important}
  The `--pre` flag is important while this version is not released.
```

```commandline
python -m pip install jupyter-book --pre
```

## Cloning or downloading the repository

To clone, please use the usual.

```commandline
git clone https://github.com/MarinhoLab/OpenExecutableBooksRobotics.git
```

Further, the package can be downloaded from [here](https://github.com/MarinhoLab/OpenExecutableBooksRobotics/archive/refs/heads/main.zip).

## Building the book

### Live document

```commandline
jupyter book start
```

Then click on the link, output below

```
     ✨✨✨  Starting Book Theme  ✨✨✨



🔌 Server started on port 3000!  🥳 🎉


        👉  http://localhost:3000  👈

```

which usually, as described, connects to `http://localhost:3000`.

### Building the HTML

```
jupyter book build --html
```

If needed, the page can be opened at `_build/html/index.html`.

## Notebook configuration

In this version of jupyter notebook, `myst.yml` is the soul of the book. It is very uncommon that `conf.py` is needed.

```{literalinclude} myst.yml
```

Everything in `myst.yml` is standard.


```{literalinclude} build_html.sh
```

We currently only need `conf.py` below for math commands in MySt documents.

```{literalinclude} conf.py
```

## Deployment in GitHub

```{important}
  It is very common for GitHub Actions to change how it works internally. This can affect, for instance, the version of the
  images run by the GitHub Actions runners, how GitHub Pages works, or how artifact upload works. If the workflow mentioned
  herein no longer works in the future, it is important to look at initially newer versions of the imported actions.
  Currently:
  - `actions/checkout@v4`
  - `actions/upload-pages-artifact@v3`
  - `actions/configure-pages@v4`
  - `actions/deploy-pages@v4`
```

This workflow is straightforward and effective. The only external action needed is to set, in your repository,
`⚙Settings > Pages > Build and deployment > Source > GitHub Actions`.


```{literalinclude} .github/workflows/notebook_to_html.yml
```


