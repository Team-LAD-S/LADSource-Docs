# LADSource Documentation

Public developer documentation for Like a Dragon: Source.

The site is published at <https://team-lad-s.github.io/LADSource-Docs/>.

## Local preview

```powershell
python -m venv .venv-docs
.\.venv-docs\Scripts\python.exe -m pip install -r requirements-docs.txt
.\.venv-docs\Scripts\python.exe -m mkdocs serve
```

## Regenerating the framework reference

The `LADSource` checkout and this repository should be placed next to
each other:

```text
addons/
├─ LADSource/
└─ LADSource-Docs/
```

Then run:

```powershell
.\.venv-docs\Scripts\python.exe tools/docs/generate_reference.py
```

Currently the generator reads the LADBot base, shared Entity extensions, and Battle
Manager from the sibling `../LADSource` checkout by default. It writes the
publishable snapshot to `docs/reference`, with one index per API module and one
page per method. Commit regenerated reference pages alongside documentation
changes.

To use another checkout location:

```powershell
.\.venv-docs\Scripts\python.exe tools/docs/generate_reference.py `
  --source-root "C:\path\to\LADSource"
```
