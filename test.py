import boto
import boto.ec2
import boto.ec2.autoscale
import fileinput
import sys
import re
import subprocess

#Variables
playbook1 = 'webserver.yml'
playbook2 = ''
playbook3 = ''

ec2 = boto.ec2.connect_to_region('ap-southeast-1')
inst = boto.ec2.autoscale.connect_to_region('ap-southeast-1')

grp = inst.get_all_groups(['ASG-1'])[0]
inst_ids  = [i.instance_id for i in grp.instances]

res = ec2.get_all_reservations(inst_ids)
str = ""
str1 = ""

if len(res) != 1:
 for i in range(len(res)):
  subres = res[i].instances
#for i in range(len(subres)):
  subfam = subres[0]
  if str == "":
   if subfam.state == "running":
      str = subfam.ip_address
  else:
   if subfam.state == "running":
    str = str + "\n" + subfam.ip_address
#for i in range(len(subres)):
#  subfam = subres[i]
  if str1 == "":
   if subfam.state == "running":
    str1 = subfam.ip_address
  else:
   if subfam.state == "running":
    str1 = str1 + "," + subfam.ip_address
else:
 subres = res[0].instances
 for i in range(len(subres)):
  subfam = subres[i]
  if str == "":
   if subfam.state == "running":
    str = subfam.ip_address
  else:
   if subfam.state == "running":
    str = str + "\n" + subfam.ip_address
  if str1 == "":
    if subfam.state == "running":
     str1 = subfam.ip_address
  else:
   if subfam.state == "running":
    str1 = str1 + "," + subfam.ip_address

print str
print str1
