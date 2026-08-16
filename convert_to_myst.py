#!/usr/bin/env python3
"""Convert Jupyter notebooks (.ipynb) to MyST text notebooks (.md).

Each code cell becomes a ````{code-cell}```` directive.
Markdown cells are preserved as-is.
Raw cells and latex macro cells are removed (handled by myst.yml).
"""

import json
import re
import sys
from pathlib import Path


def _join_source(source):
    """Join cell source lines, ensuring proper newlines between them.

    Handles both formats:
    - ["line1\n", "line2\n"]  (original ipynb format)
    - ["line1", "line2"]      (json.dump re-saved without trailing newlines)
    """
    if isinstance(source, str):
        return source
    parts = list(source)
    if not parts:
        return ""
    # Check if lines already have trailing newlines
    if parts and parts[0].endswith("\n"):
        return "".join(parts)
    # No trailing newlines — join with \n and add one at the end
    return "\n".join(parts) + "\n"


def notebook_to_myst(nb_path: Path, output_path: Path, title_prefix: str = ""):
    """Convert a single notebook to a MyST text notebook."""
    with open(nb_path) as f:
        nb = json.load(f)

    lines: list[str] = []

    # Frontmatter
    lines.append("---")
    lines.append("kernelspec:")
    lines.append("  name: python3")
    lines.append("  display_name: 'Python 3'")
    lines.append("---")
    lines.append("")

    for cell in nb["cells"]:
        cell_type = cell["cell_type"]
        source = _join_source(cell["source"])

        if not source.strip():
            continue

        # Skip raw cells
        if cell_type == "raw":
            continue

        # Skip latex macro definition cells
        lower_src = source.lower().strip()
        if "providecommand" in lower_src and ("myvec" in lower_src or "mymatrix" in lower_src):
            continue

        if cell_type == "markdown":
            # Fix ipynb attachment syntax: ![img](attachment:img.png) -> ![img](img.png)
            fixed = re.sub(
                r'!\[(.*?)\]\(attachment:(.*?)\)',
                r'![\1](\2)',
                source,
            )
            lines.append(fixed.rstrip("\n"))
            lines.append("")

        elif cell_type == "code":
            code = source.rstrip("\n")
            lines.append("````{code-cell}")
            lines.append(code)
            lines.append("````")
            lines.append("")

    # Remove trailing blank lines but keep one
    while len(lines) > 1 and not lines[-1].strip():
        lines.pop()
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  {nb_path} -> {output_path}")


def main():
    base = Path(__file__).parent
    src_dir = base / "basic_lessons"
    dst_dir = base / "unstable"
    dst_dir.mkdir(exist_ok=True)

    # Copy images
    for img in src_dir.glob("*.*"):
        if img.suffix.lower() in (".png", ".svg"):
            dst = dst_dir / img.name
            dst.write_bytes(img.read_bytes())
            print(f"  Copied {img.name}")

    # Convert tutorial notebooks
    tutorials = [
        "lesson1_tutorial.ipynb",
        "lesson2_tutorial.ipynb",
        "lesson3_tutorial.ipynb",
        "lesson4_tutorial.ipynb",
        "lesson5_tutorial.ipynb",
    ]

    exercise_answers = [
        "lesson1_exercise_answers.ipynb",
        "lesson2_exercise_answers.ipynb",
        "lesson3_exercise_answers.ipynb",
        "lesson4_exercise_answers.ipynb",
        "lesson5_exercise_answers.ipynb",
    ]

    print("Converting tutorials...")
    for nb in tutorials:
        src = src_dir / nb
        dst = dst_dir / nb.replace(".ipynb", ".md")
        notebook_to_myst(src, dst)

    print("\nConverting exercise answers...")
    for nb in exercise_answers:
        src = src_dir / nb
        dst = dst_dir / nb.replace(".ipynb", ".md")
        notebook_to_myst(src, dst)

    print("\nDone.")


if __name__ == "__main__":
    main()