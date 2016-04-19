# android build enviornment
#
#

# Pull base image.
FROM ubuntu:14.04.4

MAINTAINER Manu Chen (manuchen@gmail.com)

# Set the env variable DEBIAN_FRONTEND to noninteractive to get
# apt-get working without error output.
ENV DEBIAN_FRONTEND noninteractive
USER root
# Update underlying ubuntu image and all necessary packages.
RUN apt-get update && apt-get upgrade -y &&\
    apt-get install -y bison g++-multilib git gperf libxml2-utils make zip openjdk-7-jdk

ENV USE_CCACHE=1
# Define default command.
CMD ["/bin/bash"]


