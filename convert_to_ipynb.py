#!/usr/bin/env python
"""Convert MyST text notebooks (.md) into downloadable Jupyter notebooks (.ipynb).

The conversion is a two-step pipeline:

    .md -> intermediate.md -> .ipynb

1. **Expand LaTeX macros.** The lessons use custom LaTeX macros (e.g. ``\\myvec``,
   ``\\mymatrix``, ``\\quat``, ``\\dual``) whose definitions live in ``myst.yml``
   under ``project.math``. MyST expands them at build time by passing them to KaTeX,
   but most ``.ipynb`` renderers (JupyterLab, VS Code, nbviewer, ...) do not know
   these macros, so they would render literally. The intermediate ``.md`` therefore
   has every macro expanded inline to its definition, so the resulting ``.ipynb``
   only ever contains standard LaTeX that any renderer can draw.
2. **Convert to notebook.** ``jupytext`` reads the intermediate ``.md``
   (``md:myst`` format) and writes the standard ``.ipynb``.

The intermediate file is written next to the source, named ``<stem>_expanded.md``
(e.g. ``lesson1_tutorial_expanded.md``). It is a build artifact: it is not tracked
in git, is not referenced in ``myst.yml``, and is not listed in
``basic_lessons``. You only ever edit the original ``.md`` (which keeps the
convenient macros); the intermediate and ``.ipynb`` are regenerated on every build.

Usage:
    python convert_to_ipynb.py                 # convert every lesson in basic_lessons/
    python convert_to_ipynb.py --keep          # also keep the intermediate .md files
    python convert_to_ipynb.py path/to/file.md # convert a single file
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

# Matches a MyST code-cell directive fence, e.g. ````{code-cell}`` or ````{code-cell} python`.
CODE_CELL_RE = re.compile(r"^\s*````\s*\{code-cell\}[^`]*$")

DEFAULT_GLOB = "basic_lessons/lesson*.md"


def load_macros(myst_path: Path) -> dict[str, str]:
    """Read the ``project.math`` macro definitions from ``myst.yml``.

    Returns a dict mapping the macro *name* (without the leading backslash, e.g.
    ``"myvec"``) to its LaTeX definition (e.g. ``"\\mathbf{\\boldsymbol{ #1 }}"``).
    """
    with open(myst_path, "r", encoding="utf-8") as fh:
        config = yaml.safe_load(fh) or {}
    math_macros = (config.get("project") or {}).get("math") or {}
    macros: dict[str, str] = {}
    for key, value in math_macros.items():
        name = key.lstrip("\\")
        macros[name] = value
    return macros


def _brace_group(text: str, pos: int) -> tuple[str, int] | None:
    """Read a balanced ``{...}`` group starting at ``text[pos] == '{'``.

    Returns the *inner* content and the index just past the closing brace, or
    ``None`` if the group is not balanced. Handles nested braces, e.g. ``{H^{-1}}``.
    """
    if pos >= len(text) or text[pos] != "{":
        return None
    depth = 0
    for i in range(pos, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[pos + 1 : i], i + 1
    return None


def _expand_at(text: str, pos: int, macros: dict[str, str]) -> tuple[str, int] | None:
    """If a macro call starts at ``text[pos]`` (which must be ``\\``), expand it.

    Returns ``(expansion, index_just_past_the_call)`` or ``None`` if no macro is
    called at ``pos``. Mirrors KaTeX/TeX macro semantics for the argument forms the
    lessons use (see the ``#1`` definitions in ``myst.yml``):

    * ``\\name{arg}``   -- braced argument, braces may be nested.
    * ``\\name arg``    -- a single space-separated token (e.g. ``\\myvec H`` grabs
                           the ``H`` and leaves any following ``_{...}^{...}`` intact).
    * ``\\name``        -- no argument (the definition has no ``#1``).

    The macro name must not be followed by a letter (so ``\\dual`` never matches
    ``\\dualfoo``). Like TeX, the macro is treated as a control sequence no matter
    what token precedes it (e.g. ``\\mymatrix{B}_2\\mymatrix{A}_2``).
    """
    if pos >= len(text) or text[pos] != "\\":
        return None
    for name in sorted(macros, key=len, reverse=True):
        start = pos + 1
        end = start + len(name)
        if text[start:end] != name:
            continue
        after = text[end] if end < len(text) else ""
        if after.isalpha():
            continue  # a longer command that merely shares this prefix
        if "#" not in macros[name]:
            # No-argument macro.
            return macros[name], end
        if after == "{":
            group = _brace_group(text, end)
            if group is None:
                return None
            arg, next_pos = group
            return macros[name].replace("#1", arg.strip()), next_pos
        if after == " ":
            # Single-token argument: take the next ``{...}`` group or one char.
            j = end + 1
            if j < len(text) and text[j] == "{":
                group = _brace_group(text, j)
                if group is None:
                    return None
                arg, next_pos = group
            elif j < len(text) and not text[j].isspace():
                arg, next_pos = text[j], j + 1
            else:
                return None
            return macros[name].replace("#1", arg.strip()), next_pos
    return None


def expand_macros(text: str, macros: dict[str, str]) -> str:
    """Expand every LaTeX macro in *text* to its definition.

    Scans left-to-right and never re-scans replaced text, so the process is
    idempotent and terminates. See :func:`_expand_at` for the supported forms.
    """
    if not macros:
        return text
    out: list[str] = []
    pos = 0
    while pos < len(text):
        if text[pos] == "\\":
            hit = _expand_at(text, pos, macros)
            if hit is not None:
                expansion, next_pos = hit
                out.append(expansion)
                pos = next_pos
                continue
        out.append(text[pos])
        pos += 1
    return "".join(out)


def expand_macros_outside_code_cells(text: str, macros: dict[str, str]) -> str:
    """Expand LaTeX macros in the prose, leaving ``{code-cell}`` bodies untouched.

    Macros are only ever used in the surrounding prose (LaTeX math). If a macro name
    ever appears inside a code cell (e.g. a variable named ``quat``), expanding it
    would corrupt the Python source, so code-cell bodies are copied through verbatim.
    """
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    in_code_cell = False
    for line in lines:
        if not in_code_cell and CODE_CELL_RE.match(line):
            in_code_cell = True
            out.append(line)
            continue
        if in_code_cell and line.strip() == "````":
            in_code_cell = False
            out.append(line)
            continue
        if in_code_cell:
            out.append(line)
        else:
            out.append(expand_macros(line, macros))
    return "".join(out)


def convert(md_path: Path, myst_path: Path, keep_intermediate: bool) -> Path:
    """Run the ``.md -> intermediate.md -> .ipynb`` pipeline for one file."""
    import jupytext  # imported lazily so --help works without it installed

    text = md_path.read_text(encoding="utf-8")
    macros = load_macros(myst_path)
    expanded = expand_macros_outside_code_cells(text, macros)

    intermediate = md_path.with_name(md_path.stem + "_expanded.md")
    intermediate.write_text(expanded, encoding="utf-8")
    try:
        nb = jupytext.read(str(intermediate), fmt="md:myst")
        ipynb_path = md_path.with_suffix(".ipynb")
        jupytext.write(nb, str(ipynb_path), fmt="ipynb")
    finally:
        if not keep_intermediate:
            intermediate.unlink(missing_ok=True)

    return ipynb_path


def main(argv: list[str] | None = None) -> int:
    repo_root = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        help="Specific .md files to convert. If omitted, every file matching --glob is used.",
    )
    parser.add_argument(
        "--glob",
        default=DEFAULT_GLOB,
        help="Glob (relative to the repo root) for lesson files when no explicit paths are given.",
    )
    parser.add_argument(
        "--myst",
        default=str(repo_root / "myst.yml"),
        help="Path to myst.yml (source of the project.math macro definitions).",
    )
    parser.add_argument(
        "--keep",
        action="store_true",
        help="Keep the intermediate _expanded.md files instead of deleting them.",
    )
    args = parser.parse_args(argv)

    myst_path = Path(args.myst)
    if not myst_path.is_file():
        print(f"error: {myst_path} not found", file=sys.stderr)
        return 1

    if args.paths:
        md_files = [Path(p) for p in args.paths]
    else:
        md_files = sorted(repo_root.glob(args.glob))
    if not md_files:
        print(f"error: no .md files matched {args.paths or args.glob}", file=sys.stderr)
        return 1

    for md_path in md_files:
        if not md_path.is_file():
            print(f"skip: {md_path} not found", file=sys.stderr)
            continue
        ipynb_path = convert(md_path, myst_path, keep_intermediate=args.keep)
        print(f"generated: {ipynb_path} (from {md_path})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
