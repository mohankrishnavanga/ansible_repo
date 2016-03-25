import boto
import boto.ec2
import boto.ec2.autoscale
import fileinput
import sys
import re
import subprocess

ec2 = boto.ec2.connect_to_region('ap-southeast-1')
inst = boto.ec2.autoscale.connect_to_region('ap-southeast-1')

grp = inst.get_all_groups(['ASG-1'])[0]
inst_ids  = [i.instance_id for i in grp.instances]

res = ec2.get_all_reservations(inst_ids)
str = ""
str1 = ""
for i in range(len(res)):
  subres = res[i].instances
#for i in range(len(subres)):
  subfam = subres[0]
  if i == 0:
   str = subfam.ip_address
  else: 
   str = str + "\n" + subfam.ip_address
#for i in range(len(subres)):
#  subfam = subres[i]
  if i == 0:
   str1 = subfam.ip_address
  else:
   str1 = str1 + "," + subfam.ip_address
print str
print str1

searchText = "[webservers]"
for line in fileinput.FileInput("ansible_repo/Autoscaling/inventory",inplace=1):
  if searchText in line:
 	 line = line.replace(searchText, searchText + "\n" + str)
  sys.stdout.write(line)

subprocess.call(['fab','-i','/home/centos/TestMKKey.pem','-H',str1,'test'])

