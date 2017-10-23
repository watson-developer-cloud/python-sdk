# Release process

Standard practice with pypi libraries is to commit all of the changes for a release except updating the version. We use [bumpversion] to update the version file, commit, and tag the changes.

## 1. Updating the version

A small command line tool to simplify releasing software by updating all version strings in your source code by the correct increment.

Install it with:

```bash
pip install bumpversion
```

## 2. Doing a release

(The pypandoc module should be installed on the system doing the release, to generate the documentation for pip.)

```sh
bumpversion major|minor|patch
git push origin master
git push origin --tags
python setup.py publish
```

`bumpversion *` will update the version field appropriately, create a git commit and tag for the version, and publish the tag to github.

`git push origin master` will publish the changes to package.json.

`git push origin --tags` will publish the tag to github., and then immediately.

`python setup.py publish` will publish the module to pypi.

The reason for this is that it allows someone to easily view the source code (and readme) for whatever version they happen to have downloaded from pypi. This is particularly helpful when github is ahead of pypi.

[bumpversion]: https://pypi.python.org/pypi/bumpversion
