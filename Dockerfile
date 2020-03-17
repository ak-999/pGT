FROM python:3.6
USER root
WORKDIR /home/username

RUN apt-get update
RUN apt-get install -y vim
RUN pip install requests==2.18.4 click==6.7

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
