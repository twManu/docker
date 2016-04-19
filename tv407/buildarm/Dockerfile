FROM armbuild/ubuntu
MAINTAINER Manu Chen

# the build environment for tvheadend

RUN apt-get update && apt-get install -y gcc pkg-config python build-essential libssl-dev\
	libhdhomerun-dev liburiparser-dev libdbus-1-dev && mkdir /mysrc
ADD libiconv-1.13.1.tgz /mysrc
ADD tv407.tgz /mysrc
ADD install.sh /mysrc/install.sh

WORKDIR /mysrc/libiconv-1.13.1
RUN ./configure; make; make install

WORKDIR /mysrc/tv407
RUN ./configure --disable-avahi --disable-dvben50221 --disable-libav; make
VOLUME ["/mysrc"]

CMD ["/bin/true"]
