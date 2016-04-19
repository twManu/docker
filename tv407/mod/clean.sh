#!/bin/sh

find . \-name "*.o" \-exec rm \-f {} \;
find . \-name "*.ko" \-exec rm \-f {} \;
find . \-name ".*.cmd" \-exec rm \-f {} \;
find . \-name vmlinux \-exec rm \-f {} \;
find . \-name vmlinux.bin \-exec rm \-f {} \;
find . \-name setup.bin \-exec rm \-f {} \;
find . \-name setup.elf \-exec rm \-f {} \;


