from fabric.api import *
env.user="centos"

def test():
	#Adding the user remoteAdmin
	sudo('if id -u "remoteAdmin" >/dev/null; then echo "user exists"; else echo "user doesnot exist"; echo "Creating user remoteAdmin"; useradd remoteAdmin; echo -e "remoteAdmin:Welcome@1234" | chpasswd; echo "remoteAdmin ALL=(ALL) ALL" | tee -a /etc/sudoers; sed -i "s/Defaults    requiretty/#Defaults    requiretty/g" /etc/sudoers; sed -i "s/PasswordAuthentication no/PasswordAuthentication yes/g" /etc/ssh/sshd_config;fi')
	sudo('service sshd restart',pty=False)

#	sudo('useradd remoteAdmin')
#	sudo('echo -e "remoteAdmin:Welcome@1234" | chpasswd')
#	sudo('echo "remoteAdmin	ALL=(ALL) ALL" | tee -a /etc/sudoers')
#	sudo('sed -i "s/Defaults    requiretty/#Defaults    requiretty/g" /etc/ssh/sshd_config')
#	sudo('sed -i "s/PasswordAuthentication no/PasswordAuthentication yes/g" /etc/ssh/sshd_config')
#	sudo('service sshd restart')
	

	#our local 'localdirectory'
	#put('scripts','/home/remoteAdmin/mynewfolder')
