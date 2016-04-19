#enable tftpd with ubuntu 14.10
#docker run -d -p 69:69/udp manuchen/tftpd
FROM ubuntu:14.04.4
MAINTAINER Manu Chen (manuchen@gmail.com)
RUN apt-get update
RUN apt-get install -y tftpd-hpa tftp-hpa
EXPOSE 69/udp
CMD ["service", "tftpd-hpa", "start"]