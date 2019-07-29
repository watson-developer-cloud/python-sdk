#Import python runtime with desired python version
FROM python:3-slim

#Install Git
RUN apt-get update && \
    apt-get install -y git

#Clone SDK repo to app directory
RUN git clone https://github.com/watson-developer-cloud/python-sdk.git

#Set working directory to python-sdk
WORKDIR /python-sdk

#Pip install dependencies for SDK
RUN pip install --editable .
RUN pip install -r requirements-dev.txt

#Run tests to validate installation
CMD [ "py.test" , "test" ]


