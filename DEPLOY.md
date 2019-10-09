## Upload a new version to PyPI

Travis-ci will push tagged commits to PyPI. Here are the steps:

1. Run `manage.py` 

```bash
./manage.sh publish
Next version number? (previous: 'XXX')
```

2. Give the new version number based on previous version (see semantic release)

3. Now the push will be on hold until you press Enter. Manually inpect the changelog (`doc/changes.rst`) to make changes if necessary. Once you are sure, go back and press Enter. 

4. Once the travis job (Python2.7) is done, the new version should be uploaded to PyPI. 

5. Update the Github [release](https://github.com/PyGithub/PyGithub/releases) page with the same release note from `doc/changes.rst`. (needed for some web spiders for changelog parsing)
