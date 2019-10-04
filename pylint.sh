#!/bin/bash

# Runs pylint only for Python 3.7
PYTHON_VERSION=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Python version: $PYTHON_VERSION"
if [ $PYTHON_VERSION = '3.7' ]; then
  pylint ibm_watson test examples
fi
