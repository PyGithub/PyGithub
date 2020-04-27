## Upload a new version to PyPI

Github workflow (`.github/workflows/python-publish.yml`) will push tagged commits to PyPI. Here are the steps:

1. Run `manage.py` 

```bash
./manage.sh publish
Next version number? (previous: 'XXX')
```

2. Give the new version number based on previous version (Use semantic versioning)

3. Create a new Github [release](https://github.com/PyGithub/PyGithub/releases) from the tag that has just been committed, with the same release note from `doc/changes.rst`. This step is the hook that will trigger the workflow. (also needed for some web spiders for changelog parsing)
 
4. Now the push will be on hold until you press Enter. Manually inspect the changelog (`doc/changes.rst`) to make changes if necessary. Once you are sure, go back and press Enter. 

5. Once the `python-publish` workflow completes, a new version will appear on [PyPI](https://pypi.org/project/PyGithub/#history) shortly.

