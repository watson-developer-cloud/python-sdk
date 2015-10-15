#!/bin/bash

# Runs pylint only for Python 2.7.X
PYTHON_VERSION=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Python version: $PYTHON_VERSION"
if [ $PYTHON_VERSION = '2.7' ]; then
  pylint watson_developer_cloud --disable=F0401,E0611,E1004,C0111,I0011,I0012,W0704,W0142,W0212,W0232,W0613,W0702,R0201,W0614,R0914,R0912,R0915,R0913,R0904,R0801,C0301
fi
