#!/usr/bin/python
import os

dir = os.path.dirname(os.path.abspath(__file__))
nginxpath= dir + "/nginx/conf.d"

hostsFile = open("/etc/hosts", "a+");
lines = hostsFile.readlines()

for fileName in os.listdir('./workspace-www'):

    if fileName != 'default':
        fin = open(nginxpath + '/default.conf', "rt")
        fout = open(nginxpath + '/' + fileName +'.conf', "wt")

        for line in fin:
            fout.write(line.replace('default', fileName))
            
        fin.close()
        fout.close()

    entryExists = False
    for line in lines:
        if fileName + ".dev" in line:
            entryExists = True  
            
    if not entryExists:
        hostsFile.write("127.0.0.1 " + fileName + ".dev\n");
        

os.popen('docker exec  webserver /usr/bin/supervisorctl restart nginx')