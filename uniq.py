#!/bin/python3

import os
from IPy import IP, IPSet


def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024)
    return round(fsize,2)

def touniq(inFile, outFile):
    total = IPSet()
    for line in open(inFile):
        if "/" in line:
            total.add(IP(line.strip(), make_net=1))
        else:
            total.add(IP(line.strip()))

    blackip = open(outFile, 'w')
    num = 0
    for ip in total:
        num += ip.len()
        blackip.write(str(ip) + '\n')
    blackip.close()
    return num

if __name__ == '__main__':
    inFile = "ip"
    outFile = "blackip.txt"
    num = touniq(inFile, outFile)
    print("[+] Total: %d\n" % num)
    fileSize = get_FileSize(outFile)
    print("[+] FileSize: %dk\n" % fileSize)
