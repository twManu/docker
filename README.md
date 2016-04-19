# docker
This is a project to build tvheadend 4.0.7. It is composed of a "build image" and a "runtime image".

The "build image" is auto-built by git hub through docker/tv407/build (Dockerfile). It contains the source code of tvheadend and libiconv which are not directly supported by Ubuntu packages. So the build image also plays the role of "source" volume when generating the "runtime image". The repository is manuchen/tv407build.

A temporary "runtime image" is manually built by gen407.sh when build/docker-compose.yml is invoked. The Dockerfile is
placed in tv407/build/image and a new evnironment is created to fulfill the runtime requirement. After the image is created, it installs the program from volume created by a container of "build image". Then the temporary "runtime instance" is exported and imported as the "runtime image". The repository is manuchen/tv407.

To run a tvheadend instance, just launch docker-compose.yml in directory tv407.
