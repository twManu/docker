#!/bin/bash

cd /mysrc/libiconv-1.13.1
./configure; make; make install

cd /mysrc/tv
./configure --disable-avahi --disable-dvben50221 --disable-libav; make


