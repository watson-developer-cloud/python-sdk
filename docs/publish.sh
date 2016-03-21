#!/bin/bash
# checking the build/job numbers allows it to only
# publish once even though we test against multiple python versions

cd $(dirname $0)

if [ "$TRAVIS_REPO_SLUG" == "watson-developer-cloud/python-sdk" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ] && [ "$TRAVIS_BRANCH" ] && [ "$TRAVIS_BUILD_NUMBER.1" == "$TRAVIS_JOB_NUMBER" ]; then

  echo "Create Docs"
  make document
  echo "Publishing Docs..."

  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "travis-ci"
  git clone --quiet --branch=gh-pages https://${GH_TOKEN}@github.com/watson-developer-cloud/python-sdk gh-pages > /dev/null

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

else

  echo -e "Not publishing docs for build $TRAVIS_BUILD_NUMBER ($TRAVIS_JOB_NUMBER) on branch $TRAVIS_BRANCH of repo $TRAVIS_REPO_SLUG"

fi
