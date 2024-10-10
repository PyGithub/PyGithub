## Upload a new version to PyPI

Github [PyPi release](.github/workflows/pypi-release.yml) workflow will push tagged commits to PyPI. Here are the steps:

1. Run `scripts/prepare_release.sh`

```bash
./scripts/prepare_release.sh
```

2. Complete the changes in `doc/changes.rst`:
   - Replace `Version ?.?.?` with the release version.
   - Organize commits into sub-sections like "New features" or "Bug Fixes", see earlier releases for inspiration.

3. Commit these changes and create a pull request.

4. After merging those changes into `main` branch, create a new Github [release](https://github.com/PyGithub/PyGithub/releases):
   - Choose the merge commit in `main`.
   - Choose a new tag with release version prefixed with `v`, e.g. `v2.2.0`.
   - Add the same release note from `doc/changes.rst`.

   Creating the release also creates the tag chosen, which will trigger the PyPi release workflow.

5. Once the PyPi release workflow completes, a new version will appear on [PyPI](https://pypi.org/project/PyGithub/#history) shortly.
