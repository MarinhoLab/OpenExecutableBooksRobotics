# AGENTS.md — Repository Best Practices

## Overview

**Open Executable Books in Robotics** is a collection of Jupyter notebooks teaching kinematic modelling and control of serial-link robotic manipulators. The project is licensed under [CC-BY-NC-SA 4.0](LICENSE) and hosted at <https://github.com/MarinhoLab/OpenExecutableBooksRobotics>.

---

## Repository Structure

| Path | Purpose |
|------|---------|
| `basic_lessons/` | Canonical source: `.ipynb` notebooks (5 tutorials + 5 exercise answer keys) |
| `unstable/` | Work-in-progress text-only MyST notebooks (`.md` with `{code-cell}` directives) |
| `other/` | Supplementary content (e.g. `dqrobotics.md`) |
| `convert_to_myst.py` | Script: converts `basic_lessons/*.ipynb` → `unstable/*.md` |
| `myst.yml` | MyST project config (root): LaTeX macros, TOC (including unstable section), site options |
| `unstable/myst.yml` | Standalone MyST project config for unstable-only builds (optional) |
| `build_html.sh` | Build script for `jupyter-book` (legacy pipeline) |
| `conf.py` | MyST parser extensions (`dollarmath`) |
| `_build/` | Build artifacts (excluded from git via `unstable/.gitignore`) |

---

## Modifying `.ipynb` Files

Jupyter notebooks are JSON files. Every cell's `source` field is a **list of strings**, where **each string must end with `\n`** (trailing newline). This is critical:

### Correct format (renders properly in Jupyter):
```json
"source": [
    "# L1 A quick Python refresher\n",
    "\n",
    "*License: CC-BY-NC-SA 4.0*\n",
    "\n",
    "### Prerequisites\n",
    "The user of this notebook is expected to have prior knowledge in\n"
]
```

### Broken format (renders as one concatenated line):
```json
"source": [
    "# L1 A quick Python refresher",
    "",
    "*License: CC-BY-NC-SA 4.0*",
    ""
]
```

### When editing notebooks programmatically:
1. Load with `json.load()`, modify `cell['source']` entries.
2. **Every source line must end with `\n`** before writing back.
3. Save with `json.dump(nb, f, indent=1)` (single-space indent is standard).
4. Clear execution state on code cells to avoid stale output:
   ```python
   cell['outputs'] = []
   cell['execution_count'] = None
   ```

### When editing notebooks manually:
- Use a notebook editor (Jupyter, VSCode, or nbconvert) rather than raw text edits.
- If editing raw JSON, always verify trailing `\n` on source lines.

### Cell types:
| Type | Purpose |
|------|---------|
| `markdown` | Text, equations, images, headings |
| `code` | Python cells (numpy, math) |
| `raw` | Raw LaTeX macro definitions (`\providecommand`) |

### LaTeX macros:
Custom macros (`\myvec`, `\mymatrix`, `\quat`, `\dual`) are defined in two places:
1. As **raw cells** in each notebook (for Jupyter/LaTeX rendering)
2. In **`myst.yml`** under `project.math` (for MyST rendering)

---

## Converting to MyST Text Notebooks

Run the converter script to regenerate `unstable/*.md` from the canonical notebooks:

```bash
python3 convert_to_myst.py
```

This script:
- Copies images (`Lesson4.png`, `Lesson4.svg`) to `unstable/`
- Converts markdown cells as-is, code cells as `    ````{code-cell}```` directives
- Strips raw cells and LaTeX macro markdown cells (handled by `myst.yml`)
- Fixes `attachment:` image syntax → plain relative paths
- Handles both trailing-newline and no-trailing-newline source formats

### MyST Compatibility Notes

- **`%%capture` magic is not supported** in MyST text notebooks. The converter may produce cells containing `%%capture` (a Jupyter magic that suppresses output). These must be removed manually from the generated `.md` files, as MyST does not support this magic and the cell will fail to execute.
- After regenerating with `convert_to_myst.py`, check all unstable `.md` files for `%%capture` and remove those lines.

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

**MyST build (root — includes all lessons + unstable):**
```bash
myst build --html
```
- `--execute` runs all code cells and caches results in `_build/execute/`
- `--html` produces HTML output in `_build/html/`
- Site format (JSON) goes to `_build/site/`

**MyST build (unstable only — optional):**
```bash
cd unstable
myst build --execute --html
```

**Legacy jupyter-book build (root):**
```bash
chmod +x build_html.sh
./build_html.sh
```
- Requires `BASE_URL` env variable for correct link resolution
- Outputs to `_build/html/`

### CI/CD

The GitHub Actions workflow (`.github/workflows/notebook_to_html.yml`) runs on pushes/PRs to `main`:
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
- In `.ipynb`: `![alt](Lesson4.png)` (relative to `basic_lessons/`)
- In `.md` (unstable): same — images are copied to `unstable/`
- Avoid `attachment:` prefix in MyST notebooks

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
- `_build/` — Build artifacts (both root and `unstable/`)
- `unstable/.gitignore` already excludes `unstable/_build/`

---

## Adding a New Lesson

1. Create `basic_lessons/lesson<N>_tutorial.ipynb` and `basic_lessons/lesson<N>_exercise_answers.ipynb`
2. Follow the header format convention above
3. Add LaTeX macro raw cell (or markdown cell with `vscode` language metadata)
4. Update `myst.yml` → add new file to `project.toc` list
5. Run `python3 convert_to_myst.py` to regenerate `unstable/`
6. Update `myst.yml` → add new unstable `.md` file to the "Unstable" section in `project.toc`
7. Test: `myst build --html` from the repository root
8. Open PR with descriptive title and body