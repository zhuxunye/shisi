#encoding=utf-8
from  socket import gethostbyname
import re
import os
#search domain list by sublist3r
def getSubDomain(domainName):
    print("Sucess!")

#get ip by hosts
def getIPByHosts(domainFileName):
    with open(domainFileName) as hostFile:
        for line in hostFile.readlines():
            try:
                host = gethostbyname(line.strip("\n"))
            except Exception as e:
                with open("ipError.txt","a+") as errorFile:
                    errorFile.writelines(line)
                print("\033[31m[-]  "+line.strip('\n') + " get ip error! \033[0m")
            else:
                with open("ipSucess.txt","a+") as successFile:
                    successFile.writelines(line.strip('\n') + "  " + host + "\n")
                with open("ipHost.txt","a+") as ipFile:
                    ipFile.writelines(host+"\n")
                print("\033[32m[+]  "+line.strip('\n') + " " + host + "\033[0m" )

#get C by host
def ip2C(hostFileName):
    ipFile = open(hostFileName)
    ipSet = set()
    lines = ipFile.readlines()
    for line in lines:
        ips = re.findall(r'\d+\.\d+?\.\d+?\.\d+?', line)
        for ip in ips:
            ipSet.add(ip)

    ipDocker = set()
    for ip in ipSet:
        ipDocker.add(re.findall(r'\d+?\.\d+?\.\d+?\.', ip)[0])
    iplist = list(ipDocker)
    iplist.sort()

    for i in range(len(iplist)):
        for j in range(255):
            ip = iplist[i]+j.__str__()
            status = os.system("ping -c 1 "+ip)
            if status == 0 :
                print("\033[32m[+]  online host " + ip + "\033[0m")
                with open("chost.txt","a+") as chostFile:
                    chostFile.writelines(ip+"\n")
            else :
                print("\033[31m[-]  connect error "+ ip + " get ip error! \033[0m")

    print(len(iplist))



if __name__ == '__main__':
    #getIPByHosts("test.txt")
    ip2C("ipHost.txt")



