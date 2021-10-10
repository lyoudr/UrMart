FROM python:3.7-buster

ENV PYTHONUNBUFFERED=1

# create and copy work directory
WORKDIR /product
COPY src /product
COPY ./entrypoint.bash /product/entrypoint.bash

# See File in /product
RUN ls /product

# install dependencies
RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT [ "bash", "entrypoint.bash"]
