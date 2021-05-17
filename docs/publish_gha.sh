#!/bin/bash
# checking the build/job numbers allows it to only
# publish once even though we test against multiple python versions

[[ -z "$GHA_BRANCH" ]] && { echo "GHA_BRANCH cannot be null" ; exit 1; }
[[ -z "$GH_TOKEN" ]] && { echo "GH_TOKEN cannot be null" ; exit 1; }

cd $(dirname $0)
pwd

echo "Create Docs"
make document
echo "Publishing Docs..."

git config --global user.email "watdevex@us.ibm.com"
git config --global user.name "watdevex"
git clone --quiet --branch=gh-pages https://${GH_TOKEN}@github.com/watson-developer-cloud/python-sdk.git gh-pages > /dev/null

pushd gh-pages
  # on tagged builds, $GHA_BRANCH is the tag (e.g. v1.2.3), otherwise it's the branch name (e.g. master)
  rm -rf $GHA_BRANCH
  cp -Rf ../_build/html/ $GHA_BRANCH
  ../generate_index_html.sh > index.html

  git add -f .
  git commit -m "Docs for $GHA_BRANCH ($GHA_COMMIT)"
  git push -fq origin gh-pages > /dev/null
popd

echo -e "Published Docs for $GHA_BRANCH to gh-pages.\n"

