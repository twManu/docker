#!/share/CACHEDEV1_DATA/.qpkg/container-station/bin/python
#to be executed at directory where
#   `pwd`/firmware and `pwd`/modules will be created for container install

import os, sys, re, subprocess, argparse


class cTVHE(object):
	VER_TUP=('3.12.6-SMP-mod_unload'\
		, '3.10.20-al-2.5.3_sa-SMP-mod_unload-ARMv7-p2v8'\
		, '3.19.8-SMP-mod_unload')
	SYS_FW='/lib/firmware'     #mount point as well
	SYS_MOD='/lib/modules'
	MOUNT_RC='/app_dir'
	#local directory name
	MY_FW='firmware'
	MY_MOD='modules'
	
	#Out : _kver - a.b.c or a.b of 'uname -r' if successful
	#              None if fail to match
	#      _arch
	#      _magic - one of VER_TUP or None
	def _getKverArch(self):
		#kver
		p=subprocess.Popen(['uname -r'], stdout=subprocess.PIPE, shell=True)
		kver=p.stdout.read().strip()
		matchObj=re.match(r'.*?(\d+)\.(\d+)\.(\d+)', kver)
		if matchObj:
			kver=matchObj.group(1)+'.'+matchObj.group(2)+'.'+matchObj.group(3)
		else:
			matchObj=re.match(r'.*?(\d+)\.(\d+)', line)
			if matchObj:
				kver=matchObj.group(1)+'.'+matchObj.group(2)
			else: kver=None
		#arch
		p=subprocess.Popen(['uname -m'], stdout=subprocess.PIPE, shell=True)
		arch=p.stdout.read().strip()
		if re.match(r'arm', arch):
			arch='arm'
		#magic
		guessMagic=None
		if kver:
			for verStr in self.VER_TUP:
				if kver in verStr:
					guessMagic=verStr
					break
		self._kver=kver
		self._arch=arch
		self._magic=guessMagic


	def __init__(self):
		#abs of cur dir
		self._curDir=os.path.abspath(os.path.realpath(__file__))
		self._curDir=os.path.dirname(self._curDir)
		self._myfw=self._curDir+'/'+self.MY_FW
		self._mymod=self._curDir+'/'+self.MY_MOD
		#kernel ver and arch
		self._getKverArch()


	def install(self, dbg=False):
		if os.path.exists(self._myfw):
			ans=raw_input(self._myfw+' exists, do you like to continue ?')
		if not re.match(r'y', ans, re.I):
			os.sys.exit(-1)
		os.system('rm -rf '+self._myfw+' '+self._mymod)
		os.system('mkdir -p '+self._myfw+' '+self._mymod)
		if os.path.exists(self.SYS_FW):
			if not os.path.islink(self.SYS_FW):
				print self.SYS_FW+' exists but it is not a link'
				os.sys.exit(-1)
			print self.SYS_FW+' exists, to be removed'
		os.system('rm -f '+self.SYS_FW)
		os.system('ln -s '+self._myfw+' '+self.SYS_FW)
		cmd='docker run -it --rm '
		cmd+='-v '+self._myfw+':'+self.SYS_FW+' '
		cmd+='-v '+self._mymod+':'+self.SYS_MOD+' '
		cmd+='-v '+self._mymod+':'+self.MOUNT_RC+' '        #RC copy to modules dir
		cmd+='-e "LIB_FIRMWARE='+self.SYS_FW+'" '
		cmd+='-e "LIB_MODULE='+self.SYS_MOD+'" '
		cmd+='-e "APP_DIR='+self.MOUNT_RC+'" '
		cmd+='-e "VERMAGIC='+self._magic+'" manuchen/tvheadend'
		if self._arch == 'arm': cmd+='_arm'
		cmd+=' /bin/bash /usr/local/bin/myinstall install'
		if dbg:	print cmd
		else: os.system(cmd)

	def run(self, dbg=False):
		#rc file
		rcFile=self._mymod+'/run.sh'
		if not os.path.isfile(rcFile):
			print rcFile+' is not exists'
			os.sys.exit(-1)
		cmd='export LIB_MODULE='+self._mymod+'; '
		cmd+='export VERMAGIC='+self._magic+'; '
		cmd+=rcFile+' start'
		
		cmd2='docker run -d -v /root/Videos -v hts:/root/.hts '
		cmd2+='-p 9981:9981 -p 9982:9982 --privileged manuchen/tvheadend'
		if self._arch == 'arm': cmd2+='_arm'
		if dbg:
			print cmd
			print cmd2
		else:
			os.system(cmd)
			os.system('rm -rf hts; mkdir -p hts')
			os.system(cmd2)

if __name__ == '__main__':
	def check_param():
		parser = argparse.ArgumentParser()
		parser.add_argument('-i', action='store_true', dest='doInstall', default=False,
			help='to install')
		parser.add_argument('-r', action='store_true', dest='doRun', default=False,
			help='to run')
		parser.add_argument('-d', action='store_true', dest='dbg', default=False,
			help='debug only, no execution')
		arg=parser.parse_args()
		return arg

	arg=check_param()
	tvheadend=cTVHE()
	if arg.doInstall:
		tvheadend.install(arg.dbg)
	elif arg.doRun:
		tvheadend.run(arg.dbg)

