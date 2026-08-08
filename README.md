# LADSource Documentation

Public developer documentation and generated LADBot API reference for
Like a Dragon: Source.

The site is published at <https://team-lad-s.github.io/LADSource-Docs/>.

## Local preview

```powershell
python -m venv .venv-docs
.\.venv-docs\Scripts\python.exe -m pip install -r requirements-docs.txt
.\.venv-docs\Scripts\python.exe -m mkdocs serve
```

## Regenerating the framework reference

The private `LADSource` checkout and this repository should be placed next to
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

The generator reads `../LADSource/lua/entities/lad_framework_base` by default
and writes the publishable snapshot to `docs/reference`. Commit regenerated
reference pages alongside documentation changes.

To use another checkout location:

```powershell
.\.venv-docs\Scripts\python.exe tools/docs/generate_reference.py `
  --source-root "C:\path\to\LADSource"
```
