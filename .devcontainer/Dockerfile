# base image
FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

# install software
RUN apt-get update && \
    apt-get install -y build-essential cmake libssl-dev clang python3-pip sudo git iputils-ping net-tools python3-pip
## googletest
RUN git clone https://github.com/google/googletest.git -b release-1.11.0 \
    && cd googletest \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && sudo make install    # Install in /usr/local/ by default

# add user
ARG UID=1000
ARG GID=1000
ARG USERNAME=user
RUN groupadd --gid $GID USERNAME \
    && useradd -m -s /bin/bash --uid $UID --gid $GID $USERNAME \
    && echo $USERNAME:$USERNAME | chpasswd \
    && gpasswd -a $USERNAME sudo
USER $USERNAME