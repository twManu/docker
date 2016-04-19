#!/bin/bash

cd /mysrc/libiconv-1.13.1; make install
cd /mysrc/tv407; make install
cp /mysrc/tv407/build.linux/tvheadend /usr/local/bin


