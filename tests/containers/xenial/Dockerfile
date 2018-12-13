FROM ubuntu:16.04
LABEL Author="Marcus Tiengo"
LABEL Name=ubuntu-systemd

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install systemd dbus python3 iproute2 debconf && \
    apt-get -y install sudo openssh-client curl htop vim gnupg software-properties-common apt-transport-https && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3 1 && \
    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/*
RUN /bin/systemctl set-default multi-user.target

CMD ["/sbin/init"]