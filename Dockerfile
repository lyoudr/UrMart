FROM python:3.7-buster

ENV PYTHONUNBUFFERED=1

# create and copy work directory
WORKDIR /product
COPY src /product
COPY ./entrypoint.bash /product/entrypoint.bash

# See File in /product
RUN ls /product

# install dependencies
RUN pip install -r requirements.txt \
    && pip install redis

# install redis
RUN apt-get update \
    && apt-get install -y redis-server

EXPOSE 5000 6379

# For local use
ENTRYPOINT [ "bash", "/product/entrypoint.bash" ]
