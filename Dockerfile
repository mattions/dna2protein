# dna2protein - dockerize the tool

# base image from python 2.7
FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

# If you have requirements.txt for installing the software, just uncomment the 
# following lines.

# ADD requirements.txt .
# RUN pip install -r requirements.txt

ADD . /code

# Ading the `code` directory to the path, so we can execute the script.
ENV PATH /code:$PATH