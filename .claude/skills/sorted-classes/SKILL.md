from scripts import openapifrom scripts.sort_class import sort_class---
name: Sort methods in PyGithub classes
description: A Python script to make PyGithub class conform to method and attribute order convention
---

Classes implementing GithubObject must have methods and attributes ordered as specified in "Internal Class Order" section in [ARCHITECTURE.md].

Python script `scripts/sort_class.py` implements order logic and applies this to given (or all) classes.

Run
```bash
python scripts/sort_class.py --dry-run openapi.index class1 class2 ...
```

The file `openapi.index` is a file created via `openapi.py` script. This index file first has to be created if it does not exist. See "openapi" skill.

Option `--dry-run` makes this a read-only operation: it does not change any files. Always show the changes to the user
for review and ask to apply the changes. Rerun the command and omit `--dry-run` if user explicitly wishes to apply the changes without further review.
