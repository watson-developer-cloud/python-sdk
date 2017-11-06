#!/bin/bash
# checking the build/job numbers allows it to only
# publish once even though we test against multiple python versions

[[ -z "$TRAVIS_BRANCH" ]] && { echo "TRAVIS_BRANCH cannot be null" ; exit 1; }
[[ -z "$GH_TOKEN" ]] && { echo "GH_TOKEN cannot be null" ; exit 1; }

cd $(dirname $0)
pwd

echo "Create Docs"
make document
echo "Publishing Docs..."

git config --global user.email "travis@travis-ci.org"
git config --global user.name "travis-ci"
git clone --quiet --branch=gh-pages https://${GH_TOKEN}@github.com/watson-developer-cloud/python-sdk.git gh-pages > /dev/null

pushd gh-pages
  # on tagged builds, $TRAVIS_BRANCH is the tag (e.g. v1.2.3), otherwise it's the branch name (e.g. master)
  rm -rf $TRAVIS_BRANCH
  cp -Rf ../_build/html/ $TRAVIS_BRANCH
  ../generate_index_html.sh > index.html

  git add -f .
  git commit -m "Docs for $TRAVIS_BRANCH ($TRAVIS_COMMIT)"
  git push -fq origin gh-pages > /dev/null
popd

echo -e "Published Docs for $TRAVIS_BRANCH to gh-pages.\n"

