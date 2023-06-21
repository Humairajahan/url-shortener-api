FROM python:3.9

WORKDIR /codebase
 
COPY requirements.txt /codebase/requirements.txt

RUN pip install -r /codebase/requirements.txt

COPY ./app /codebase/app