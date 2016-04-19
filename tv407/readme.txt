===== Overview =====
This is a project to build the Tvheadend application into a docker container. Both x86_64 and ARM 
architectures are supported. The latter, so far as I know, requires an ARM machine to run with.
The build machine should install python, docker and docker-compose in advance.


===== Build steps =====
There are a few stages to come out a Tvheadend container image:
0. prepared source
	a. libiconv
		- build/libiconv-1.13.1.tgz
		- from official site without modification
	b. Tvheadend
		- build/tv407.tgz
		- version 4.0.7 source from official site 
		- added with channel scan data (generated after tvheadend built under Ubuntu)
1. generate source volume for building tvheadend
	a. Dockerfile: build/Dockerfile
	b. command:
		$ cd build; docker build -t <sb>/tv407build .

#the following steps are completed with
#command:
#	$ ./gen407.sh
2. generate pre-tvheadend image
	- Compose file: build/docker-compose.yml
		+ Dockerfile: build/img/Dockerfile
		+ source volume: <sb>/tv407build as in step 1
	- the tvheadend is installed after this step

3. insert kernel module as <sb>/tv407
	a. Dockerfile: ./Dockerfile
	b. the container in step 2 is exported and then imported as an image
	c. kernel modules are inserted into image and TCP/port exported for Tvheadend 
