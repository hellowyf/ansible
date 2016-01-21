#!/usr/bin/python
import commands
import sys
import os
import json
import ansible.runner
import re
from subprocess import call


def AnsibleRunner(hostlist,project,module_name,module_args):
    print "Ansible is Running......"
    print "module >>>>> \033[0;31m%s\033[0m \nargs >>>>> \033[0;31m%s\033[0m" %(module_name,module_args)
    results = ansible.runner.Runner(host_list=hostlist,pattern=project,module_name=module_name,module_args=module_args,forks=10).run()
    if results is None:
        print "Sorry! I havn't found hosts"
        sys.exit(1)
    print "UP *****************"
    for(hostname, result) in results['contacted'].items():
        if not 'failed' in result:
            if 'stdout' in result:
                print "\033[0;31m%s\033[0m >>> \033[0;31m%s\033[0m" % (hostname, result['stdout'])
            else:
                print "\033[0;31m%s\033[0m >>> success" % hostname
    print "FAILED *************"
    for(hostname, result) in results['contacted'].items():
        if 'failed' in result:
            print "\033[0;31m%s\033[0m >>> \033[0;31m%s\033[0m" % (hostname, result['msg'])
    print "DOWN ***************"
    for (hostname, result) in results['dark'].items():
        print "\033[0;31m%s\033[0m >>> \033[0;31m%s\033[0m" % (hostname, result)
    print "I have finish this job!"

def MakeDir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)

def Modify(file,idc):
    input = open(file)
    lines = input.readlines()
    input.close()

    output = open(file,'w')
    for line in lines:
        if not line:
            break
        if 'ENVIRONMENT' in line:
            replace = "define('ENVIRONMENT', '%s');" % idc
            temp = re.sub(".*ENVIRONMENT.*",replace,line)
            output.write(temp)
        else:
            output.write(line)
    output.close()

def GetMaxId(MyJson):
    MaxId = 0
    List = []
    for i in MyJson:
        List.append(int(i))
    MaxId=max(List)
    return MaxId
