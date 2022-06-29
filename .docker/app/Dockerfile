ARG PYTHON_VERSION=3.10.5

FROM python:${PYTHON_VERSION}-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
