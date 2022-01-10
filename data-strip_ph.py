'''
tool to strip out pH values from csv files that are saved on an
SD card in a pH/conductivity controller

this is adapted from data-strip, which was used to extract conductivity data
from the same csv data files

the desired data is always in characters 32-37, starting on line 4

useful ideas for coding:
    opening, reading and writing from files
    using glob to return files in a path

sam karpiniec

05oct2020 v0.1 first version adapted from conductivity program
10jan2022 v0.2 added line-length check before slicing data i.e. length of 1 is blankline
'''

import glob
import math

list=open('C:/tmp/pH_2021_q4.csv','a+')
list.write('filename,pH-avg,pH-conv-avg\n')

for datafilez in sorted(glob.iglob('c:/tmp/test/*.CSV')):
    csv=open(datafilez,'r')
    print(datafilez)
    lines=csv.readlines()
    csv.close()

    values=[]
    Hvalues=[]

    for x in range(3,len(lines)):
       if len(lines[x])!=1: 
            z=float(lines[x][31:37])
            values.append(z)
            Hvalues.append(10**((-1)*z))

    #print(values)
    #print(Hvalues)
    avg=sum(values)/len(values)
    Havg=math.log((sum(Hvalues)/len(Hvalues)),10)*(-1)

    print(avg,Havg)

    list.write(datafilez[-10:]+',')
    list.write(str(avg)+',')
    list.write(str(Havg)+'\n')

list.close()
