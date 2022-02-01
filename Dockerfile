FROM python:3.8.5-slim-buster AS base

FROM base AS builder
ADD . /code
ADD requirements.txt .
WORKDIR /code/py
RUN pip install -r ../requirements.txt
RUN ls -l
CMD /bin/bash
# CMD python py/api/app.py
