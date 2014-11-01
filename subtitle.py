import string
import re
import os
from math import floor
import _winreg
import sys
 
assTime = re.compile('^\d+:\d+:\d+\.\d+')
 
def assStringToTime(strr):
    t = strr.split(':')
    time = 0
    time += int(t[0]) * 3600
    time += int(t[1]) * 60
    time += float(t[2])
    return time
 
def assTimeToString(time):
    sec = floor(time)
    part = str(int((time - sec) * 100))
    if len(part) < 2:
        part = '0' + part
    h = str(int(sec // 3600))
    sec %= 3600
    m = str(int(sec // 60))
    if len(m) < 2:
        m = '0' + m
    sec = str(int(sec%60))
    if len(sec) < 2:
        sec = '0' + sec
    strr = h +':'+ m +':'+ sec + '.' + part
    return strr
 
def processAssLine(line,offset):
    li = line.split(',')
    if len(li) >= 3:
        if assTime.match(li[1]):
            tt1 = assStringToTime(li[1]) + offset
            li[1] = assTimeToString(tt1)
        if assTime.match(li[2]):
            tt2 = assStringToTime(li[2]) + offset
            li[2] = assTimeToString(tt2)
    return ','.join(li)
i = 1
frame = 0
rate = 23.976
filedest = ""
while i < len(sys.argv):
    if sys.argv[i].startswith('--'):
        option = sys.argv[i][2:]
        if option == 'version':
            print 'Version 1.0.0'
            sys.exit()
        elif option == 'help':
            print '''\
Options:
  --version : Prints the version number
  --help    : Display this help
Arguments:
  -i        [Full Path of the ASS subfile]
  -f        [frame]
  -r	    [frame rate]
  '''
            sys.exit()
    elif sys.argv[i].startswith('-'):
        option = sys.argv[i][1:]
        if option == 'f': #number of frames
            frame = int(sys.argv[i+1])
            i+=1
        elif option == 'r':
            rate = float(sys.argv[i+1])
            i+=1
        elif option == 'i':
            inputfile = sys.argv[i+1]
            i+=1
    i+=1
if inputfile != "":    
    filenames = inputfile.split("\\")
    filename = filenames[len(filenames) - 1]
    

if frame == 0:
    offset = 0
else:
    offset = float(frame)/rate
 
f = open(inputfile, 'r')
t = open(os.path.dirname(inputfile)+"new."+filename,'w')
for line in f.readlines():
    ans = processAssLine(line,offset)
    t.write(ans)
 
f.close()
t.close()
