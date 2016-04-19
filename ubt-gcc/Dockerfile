FROM ubuntu
MAINTAINER Manu Chen (manuchen@gmail.com)

ADD . /home/dummy
#ENV PROXY_HOST="10.1.1.60"
#ENV http_proxy="http://$PROXY_HOST:8080/"
#ENV https_proxy="https://$PROXY_HOST:8080/"
#ENV HTTP_PROXY="http://$PROXY_HOST:8080/"
#ENV HTTPS_PROXY="https://$PROXY_HOST:8080/"


#libgtest-dev cmake for gtest
#to support windows rdp
# xrdp and xfce4
#support cifs, use
#	> docker run -it --privileged
# in docker...no need to provide machine name
#	$ mount.cifs //62.11.20.107/d /opt -o username=manu

RUN apt-get update &&\
	apt-get install -y sudo gcc build-essential git-core\
	libgtest-dev cmake python vim cifs-utils man xrdp xfce4-terminal
	


#for easy access to driver d:
#RUN echo "alias lnd='mount.cifs //192.168.59.3/d /opt -o username=manu'" >>/root/.bashrc

RUN adduser --home /home/dummy --disabled-password --gecos '' dummy &&\
	adduser dummy sudo &&\
	chown -R dummy:dummy /home/dummy &&\
	chmod -R 774 /home/dummy &&\
	echo '%sudo ALL=(ALL) NOPASSWD:ALL' >/etc/sudoers

#for gtest
WORKDIR /usr/src/gtest
RUN cmake -E make_directory build &&\
	cmake -E chdir build cmake .. >>/dev/null &&\
	cmake --build build >>/dev/null &&\
	cp build/libgtest* /usr/local/lib/ &&\
	rm -rf build

#xfce4
RUN echo xfce4-session >/root/.xession
COPY startwm.sh /etc/xrdp/startwm.sh
COPY chpwd /tmp/chpwd
RUN passwd< /tmp/chpwd

EXPOSE 5900 3398
WORKDIR /root
USER root
CMD ["/bin/bash"]
