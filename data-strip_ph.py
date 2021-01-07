'''
tool to strip out pH values from csv files that are saved on an
SD card in a pH/conductivity controller

this is adapted from data-strip, which was used to extract conductivity data
from the same csv data files

the desired data is always in characters 32-37, starting on line 4

script fails if there are blank lines in a data csv
lacking an elegant solution, simply delete the blank lines then re-run

useful ideas for coding:
    opening, reading and writing from files
    using glob to return files in a path

sam karpiniec

05oct2020 v0.1 first version adapted from conductivity program
'''

import glob
import math

list=open('C:/tmp/pH_2020_q4.csv','a+')
list.write('filename,pH-avg,pH-conv-avg\n')

for datafilez in sorted(glob.iglob('c:/tmp/test/*.CSV')):
    csv=open(datafilez,'r')
    print(datafilez)
    lines=csv.readlines()
    csv.close()

    values=[]
    Hvalues=[]

    for x in range(3,len(lines)):
        z=float(lines[x][31:37])
        values.append(z)
        Hvalues.append(10**((-1)*z))

    print(values)
    print(Hvalues)
    avg=sum(values)/len(values)
    Havg=math.log((sum(Hvalues)/len(Hvalues)),10)*(-1)

    print(avg,Havg)

    list.write(datafilez[-10:]+',')
    list.write(str(avg)+',')
    list.write(str(Havg)+'\n')

list.close()
