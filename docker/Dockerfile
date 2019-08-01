#Import Python base image 
FROM python:3-slim

#Install Git
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#Clone SDK repo to app directory
RUN git clone https://github.com/watson-developer-cloud/python-sdk.git

#Install the SDK
RUN pip install --upgrade ibm-watson

# #Set working directory to python-sdk
WORKDIR /python-sdk

#Install test dependencies and run tests to verify installation.
RUN pip install -r requirements-dev.txt

#Run tests to verify installation
CMD ["py.test","test"]


