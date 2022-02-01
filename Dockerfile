FROM python:3.8.5-slim-buster AS base

FROM base AS builder
ADD . /code
ADD requirements.txt .
WORKDIR /code
RUN pip install -r ../requirements.txt
RUN ls -l
CMD python py/api/app.py
