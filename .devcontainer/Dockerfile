# base image
FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

# install software
RUN apt-get update && \
    apt-get install -y build-essential cmake libssl-dev clang python3-pip sudo git

# add user
ARG UID=1000
ARG GID=1000
ARG USERNAME=user
RUN groupadd --gid $GID USERNAME
RUN useradd -m -s /bin/bash --uid $UID --gid $GID $USERNAME
RUN echo $USERNAME:$USERNAME | chpasswd
RUN gpasswd -a $USERNAME sudo
USER $USERNAME