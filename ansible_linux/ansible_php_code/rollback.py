#!/usr/bin/python
import commands
import os
import sys
import json
import ansible.runner
from package import MyAnsible

HostList = './host.yml'
Project = sys.argv[1]
IDC = "aws"
JsonUrl = "/data/MPP/code_bak/%s/version.json" %Project

if os.path.exists(JsonUrl):
    with open(JsonUrl,'r') as file:
        Json = json.load(file)
        NowVersionId = MyAnsible.GetMaxId(Json)
        LastVersionId = NowVersionId-1
        if LastVersionId <= 0:
            print "\033[0;31mNo more history version to rolling back!\033[0m"
            sys.exit()
        while LastVersionId > 0:
            if str(LastVersionId) in Json:
                NowVersionUrl = Json[str(NowVersionId)]['url']
                LastVersionUrl = Json[str(LastVersionId)]['url']
                command = "cat /data/MPP/code_bak/%s/%s/version.yml" % (Project,Json[str(LastVersionId)]['tag'])
                (status,output) =  commands.getstatusoutput(command)
                print "The last version message is:\n \033[0;31m%s\033[0m" % output
                if os.path.exists(LastVersionUrl):
                    AnsibleArgs = "src=%s dest=/data/www/%s/ rsync_opts=--no-motd,--exclude=version checksum=yes archive=yes delete=yes" % (LastVersionUrl,Project)
                    MyAnsible.AnsibleRunner(HostList,Project,'synchronize',AnsibleArgs)
                    MyAnsible.AnsibleRunner(HostList,Project,'shell','chown www:www /data/www -R')
                    print  "Delete useless version \033[0;31m%s\033[0m!" %Json[str(NowVersionId)]['tag']
                    command = "rm -rf %s" % NowVersionUrl
                    (status,output) =  commands.getstatusoutput(command)
                    del Json[str(NowVersionId)]
                    NewJson=json.dumps(Json,sort_keys=True,indent=2)
                    with open(JsonUrl,'w') as file:
                        file.write(NewJson)
                    sys.exit()
                else:
                    print "Sorry!The last version \033[0;31m%s not exist!\033[0m" %Json[str(LastVersionId)]['tag']
                    del Json[str(LastVersionId)]
                    NewJson=json.dumps(Json,sort_keys=True,indent=2)
                    with open(JsonUrl,'w') as file:
                        file.write(NewJson)
                    sys.exit()
            else:
                LastVersionId = LastVersionId - 1
                continue
else:
    print "\033[0;31mSorry,I havn't find version.json file!\033[0m"

