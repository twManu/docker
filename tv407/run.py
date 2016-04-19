#!/share/CACHEDEV1_DATA/.qpkg/container-station/bin/python
#to be executed at directory where
#   `pwd`/firmware and `pwd`/modules will be created for container install

import os, sys, re

VER_TUP=('3.12.6-SMP-mod_unload', '3.10.20-al-2.5.3_sa-SMP-mod_unload-ARMv7-p2v8',\
 '3.19.8-SMP-mod_unload')

CWD=os.path.abspath(os.path.realpath(__file__))
CWD=os.path.dirname(CWD)
#rc file
RC=CWD+'/modules/run.sh'
if not os.path.isfile(RC):
	print RC+' is not exists'
	os.sys.exit(-1)
	
cmd='export LIB_MODULE='+CWD+'/modules; '
cmd+='export VERMAGIC=3.10.20-al-2.5.3_sa-SMP-mod_unload-ARMv7-p2v8; '
cmd+=RC+' start'

os.system(cmd)
os.system('rm -rf hts; mkdir -p hts')
cmd='docker run -d -v /root/Videos -v hts:/root/.hts '
cmd+='-p 9981:9981 -p 9982:9982 --privileged '
cmd+='manuchen/tvheadend_arm'

print cmd
if len(sys.argv) is 1:
	os.system(cmd)
