# AGENTS.md — Repository Best Practices

## Overview

**Open Executable Books in Robotics** is a collection of MyST text notebooks teaching kinematic modelling and control of serial-link robotic manipulators. The project is licensed under [CC-BY-NC-SA 4.0](LICENSE) and hosted at <https://github.com/MarinhoLab/OpenExecutableBooksRobotics>.

---

## Repository Structure

| Path | Purpose |
|------|---------|
| `basic_lessons/` | Canonical source: MyST text notebooks (`.md` with `{code-cell}` directives) — 6 tutorials + 5 exercise answer keys |
| `basic_lessons/.gitignore` | Excludes generated `.ipynb` files (produced at build time) |
| `convert_to_ipynb.py` | Builds the downloadable `.ipynb` files: `.md` → intermediate `.md` (LaTeX macros expanded) → `.ipynb` |
| `other/` | Supplementary content (e.g. `dqrobotics.md`) |
| `myst.yml` | MyST project config (root): LaTeX macros, TOC, site options |
| `build_html.sh` | Build script for `jupyter-book` |
| `conf.py` | MyST parser extensions (`dollarmath`) |
| `_build/` | Build artifacts (excluded from git) |

---

## Modifying MyST Text Notebooks

Lessons are [MyST text notebooks](https://mystmd.org/guide/notebooks-with-markdown) — plain Markdown files with `{code-cell}` directives. They are version-control friendly and human-readable.

### Structure

Each `.md` lesson file begins with YAML frontmatter declaring the kernel:

```yaml
---
kernelspec:
  name: python3
  display_name: 'Python 3'
---
```

Code cells are delimited with `{code-cell}` directives:

````markdown
````{code-cell}
import numpy as np
x = np.array([1, 2, 3])
````
````

### Editing guidelines

- Edit `.md` files directly — they are plain text.
- Every lesson should follow the header format convention (see below).
- Keep code cells focused and self-contained.
- LaTeX equations use inline `$...$` or display `$$...$$` syntax with the `dollarmath` MyST extension enabled in `conf.py`.
- Custom macros (`\myvec`, `\mymatrix`, `\quat`, `\dual`) are defined in `myst.yml` under `project.math`.

### `%%capture` magic

**`%%capture` magic IS supported** in MyST text notebooks. MyST uses a Jupyter Server with an IPython kernel to execute code cells ([Execute Notebooks at Build Time](https://mystmd.org/guide/execute-notebooks)). The `%%capture` magic is a built-in IPython cell magic ([Built-in magic commands — IPython](https://ipython.readthedocs.io/en/stable/interactive/magics.html)) and works correctly during MyST execution. Use `%%capture` on `%pip install` cells to suppress output.

### Downloadable `.ipynb` from `.md` notebooks

The `basic_lessons/` `.md` files are the canonical source. `.ipynb` files are generated at build time so visitors can download them. The conversion is a **two-step pipeline** run by `convert_to_ipynb.py`:

```
basic_lessons/*.md  ->  <stem>_expanded.md  (LaTeX macros expanded)  ->  basic_lessons/*.ipynb
```

1. **CI pipeline** (`.github/workflows/notebook_to_html.yml`) runs `python convert_to_ipynb.py` before the MyST build.
2. **Why the intermediate step?** The lessons use custom LaTeX macros (e.g. `\myvec{q}`) that MyST expands at build time by passing them to KaTeX. Most standalone `.ipynb` renderers (JupyterLab, VS Code, nbviewer, ...) do **not** know these macros and would show them literally. So `convert_to_ipynb.py` first expands every macro to its definition from `myst.yml` (`project.math`), writing a temporary `<stem>_expanded.md`; `jupytext` then converts that expanded file to `.ipynb`. The generated `.ipynb` therefore contains **only standard LaTeX** and renders anywhere. You keep writing the original `.md` with the convenient macros.
3. **`myst.yml` TOC** references the generated `.ipynb` for the lesson section — MyST renders these identically to the `.md` but provides native "Download notebook" buttons.
4. **`basic_lessons/.gitignore`** excludes `.ipynb` so only `.md` is tracked in git.

The intermediate `<stem>_expanded.md` files are also build artifacts — deleted after conversion (use `--keep` to inspect them). They are not tracked and not referenced in `myst.yml`.

To generate locally (e.g. for testing):
```bash
pip install jupytext pyyaml
python convert_to_ipynb.py          # all lessons
python convert_to_ipynb.py --keep   # keep the intermediate _expanded.md files
```

### Image references

- Use relative paths: `![alt](Lesson4.png)` (relative to `basic_lessons/`)
- Images (`Lesson4.png`, `Lesson4.svg`) live alongside the lesson files in `basic_lessons/`.

---

## Building & Testing

### Dependencies

```bash
# Create venv
python3 -m venv venv
source venv/bin/activate

# For MyST text notebook builds:
pip install mystmd jupyter-server ipykernel jupytext

# For legacy jupyter-book builds:
pip install jupyter-book --pre
```

### Build Commands

**jupyter-book build (CI pipeline):**
```bash
# Step 1: Generate .ipynb from .md (required for download buttons)
pip install jupytext pyyaml
python convert_to_ipynb.py

# Step 2: Build the site
chmod +x build_html.sh
./build_html.sh
```
- Installs `jupyter-book --pre` (Jupyter Book 2.0 alpha)
- Sets `BASE_URL` for correct link resolution
- Runs `python -m jupyter book build --html --execute`
- Outputs to `_build/html/`

**MyST build (local development):**
```bash
pip install mystmd jupyter-server ipykernel
myst build --html
```
- `--execute` runs all code cells and caches results in `_build/execute/`
- `--html` produces HTML output in `_build/html/`

### Keeping the build warning-free

The CI `build` job runs the real build, so keep it free of warnings. The three
warning classes seen so far (all fixed in #11):

- **`missing heading depth N`** — a page jumps heading levels (e.g. `#` then
  `###`, skipping `##`). Use consecutive depths.
- **`textEnv, Too few columns specified in the {array} column argument`** — a
  `\begin{array}{...}` declares fewer columns than a row has. Match the spec to
  the actual column count (e.g. a 4×4 matrix needs `{cccc}`, not `{ccc}`).
- **`Language is not defined for code block`** — a `{code-cell}` with no
  language. Add `python` (``{code-cell} python``). Note this only surfaces for
  lessons referenced in `myst.yml` as **`.md`** (currently lesson 0): lessons
  1–5 are referenced as **`.ipynb`**, where Jupyter carries the Python language,
  so their bare `{code-cell}` directives are fine.

### CI/CD

The GitHub Actions workflow (`.github/workflows/notebook_to_html.yml`) runs on pushes to `main` and on pull requests:
1. Generates `.ipynb` from `.md` via `python convert_to_ipynb.py` (expanding LaTeX macros into an intermediate `.md` first)
2. Runs `./build_html.sh` (jupyter-book pipeline)
3. Uploads `_build/html/` as Pages artifact
4. Deploys to GitHub Pages

**Timeout:** 5 minutes. Keep cells fast to avoid CI failures.

---

## Content Conventions

### Notebook header format (every tutorial):
```markdown
# LN <Title>
*License: CC-BY-NC-SA 4.0*

*Author: Murilo M. Marinho (murilo.marinho@manchester.ac.uk)*

## Prerequisites for the learner
The user of this notebook is expected to have prior knowledge in
- All the content and prerequisites of lessons X.

## I found an issue
Thank you! Please report it at https://github.com/MarinhoLab/OpenExecutableBooksRobotics/issues
```

### Equation macros:
- `\myvec{q}` for vectors
- `\mymatrix{H}` for matrices
- `\quat{}` for quaternions
- `\dual{}` for dual numbers

These are defined in `myst.yml` under `project.math` (KaTeX `#1` substitutions) and
are expanded by MyST when building the site. Use them freely in the `.md` source —
`convert_to_ipynb.py` expands them into the downloadable `.ipynb` so the notebooks
also render in standalone viewers. **Code cells are left untouched** (a macro name
in a Python comment/variable is never expanded).

### Image references:
- Use relative paths: `![alt](Lesson4.png)` (relative to `basic_lessons/`)
- Images live alongside the lesson files in `basic_lessons/`.

### Language:
- **UK English** spelling (e.g. *behaviour*, *modelling*, *summarised*)
- Angles in **radians**, lengths in **meters**

---

## Git Workflow

- **Main branch:** `main`
- **Never push directly to `main`** — always use feature branches and PRs
- Feature branch naming: `fix/<short-description>` or `feat/<short-description>`
- Example: `fix/typos-and-uk-english`, `feat/add-lesson6`

### Files excluded from version control:
- `basic_lessons/*.ipynb` — Generated at build time from `.md` files (via `basic_lessons/.gitignore`)
- `basic_lessons/*_expanded.md` — transient intermediate files from `convert_to_ipynb.py` (deleted after conversion; `--keep` retains them for inspection)

There is intentionally no root `.gitignore`. If you create local `venv/` or `_build/`
directories, keep them out of commits (e.g. via `.git/info/exclude`).

---

## Adding a New Lesson

1. Create `basic_lessons/lesson<N>_tutorial.md` (and optionally `basic_lessons/lesson<N>_exercise_answers.md`)
2. Add YAML frontmatter with kernelspec at the top of the file
3. Follow the header format convention above
4. Use `{code-cell}` directives for Python code blocks
5. Use `%%capture` on `%pip install` cells to suppress output
6. Update `myst.yml` — add new file(s) to `project.toc` list as `.ipynb` (generated at build time)
7. Update `basic_lessons/README.md` — add the new lesson to the contents table, linking to the generated `.ipynb` (not the `.md`)
8. Test: run `python convert_to_ipynb.py` to regenerate the `.ipynb`, then `./build_html.sh` from the repository root
9. Open PR with descriptive title and body
