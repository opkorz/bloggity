FROM ubuntu:trusty

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update

RUN apt-get -y install software-properties-common
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update
RUN apt-get -y install nginx
RUN apt-get -y install dnsmasq

CMD ["nginx"]