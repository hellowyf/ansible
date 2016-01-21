#!/usr/bin/python
import commands
import sys
import os
import json
import ansible.runner
import re
from package import MyAnsible
from subprocess import call

def GetVersion(project):
    command = "cat /data/MPP/test/%s/version.yml | grep tag | awk '{print $2}'" % project
    (status,output) =  commands.getstatusoutput(command)
    return output

#local rsync
def LocalSync(src,dest):
    MyAnsible.MakeDir(dest)
    cmd = "rsync -avc --exclude '.git' %s %s > /dev/null" % (src,dest)
    ret = call(cmd,shell=True)

HostList = './host.yml'
Project = "php-framework"
TestUrl = "/data/MPP/test/%s/" % Project
CodeBakUrl = "/data/MPP/code_bak/%s/%s/" % (Project,GetVersion(Project))
JsonUrl = "/data/MPP/code_bak/%s/version.json" %Project
AnsibleArgs = "src=%s dest=/data/www/%s/ checksum=yes rsync_opts=--no-motd,--exclude=.git archive=yes delete=yes" % (CodeBakUrl,Project)

#modify version.json
#if JsonUrl exist
if os.path.isfile(JsonUrl):
    with open(JsonUrl,'r') as file:
        Json = json.load(file)
        Max = MyAnsible.GetMaxId(Json)
#get last version , if last version == now version  warning
        if GetVersion(Project) == Json[str(Max)]['tag']:
            print "\033[0;31mSorry!The tag %s same as last time!Please check your version.yml\033[0m" %GetVersion(Project)
            exit(1)
        else:
            print "local rsync"
            LocalSync(TestUrl,CodeBakUrl)
            print "rsync online"
            MyAnsible.AnsibleRunner(HostList,Project,'synchronize',AnsibleArgs)
            MyAnsible.AnsibleRunner(HostList,Project,'shell','chown www:www /data/www -R')
            Json[str(Max+1)] = {'tag':GetVersion(Project),'url':CodeBakUrl}
            NewJson=json.dumps(Json,sort_keys=True,indent=2)
            with open(JsonUrl,'w') as file:
                file.write(NewJson)
else:
    print "local rsync"
    LocalSync(TestUrl,CodeBakUrl)
    print "rsync online"
    MyAnsible.AnsibleRunner(HostList,Project,'synchronize',AnsibleArgs)
    MyAnsible.AnsibleRunner(HostList,Project,'shell','chown www:www /data/www -R')
    NewJson = {"1":{"tag":GetVersion(Project),"url":CodeBakUrl}}
    with open(JsonUrl,'w') as file:
        JsonDump=json.dumps(NewJson,sort_keys=True,indent=2)
        file.write(JsonDump)
print "======================================"
print "The Code_Update job is done,Now version is \033[0;31m%s\033[0m" % GetVersion(Project)
