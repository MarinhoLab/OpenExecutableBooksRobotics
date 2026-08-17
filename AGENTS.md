# AGENTS.md — Repository Best Practices

## Overview

**Open Executable Books in Robotics** is a collection of MyST text notebooks teaching kinematic modelling and control of serial-link robotic manipulators. The project is licensed under [CC-BY-NC-SA 4.0](LICENSE) and hosted at <https://github.com/MarinhoLab/OpenExecutableBooksRobotics>.

---

## Repository Structure

| Path | Purpose |
|------|---------|
| `basic_lessons/` | Canonical source: MyST text notebooks (`.md` with `{code-cell}` directives) — 6 tutorials + 5 exercise answer keys |
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
pip install mystmd jupyter-server ipykernel

# For legacy jupyter-book builds:
pip install jupyter-book --pre
```

### Build Commands

**jupyter-book build (CI pipeline):**
```bash
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

### CI/CD

The GitHub Actions workflow (`.github/workflows/notebook_to_html.yml`) runs on pushes to `main` and on pull requests:
1. Runs `./build_html.sh` (jupyter-book pipeline)
2. Uploads `_build/html/` as Pages artifact
3. Deploys to GitHub Pages

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
- `venv/` — Python virtual environment
- `_build/` — Build artifacts

---

## Adding a New Lesson

1. Create `basic_lessons/lesson<N>_tutorial.md` (and optionally `basic_lessons/lesson<N>_exercise_answers.md`)
2. Add YAML frontmatter with kernelspec at the top of the file
3. Follow the header format convention above
4. Use `{code-cell}` directives for Python code blocks
5. Update `myst.yml` → add new file(s) to `project.toc` list
6. Update `basic_lessons/README.md` → add the new lesson to the contents table
7. Test: `./build_html.sh` from the repository root
8. Open PR with descriptive title and body