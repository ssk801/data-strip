'''
tool to strip out conductivity values from csv files that are saved on an
SD card in a pH/conductivity controller

the values in each daily csv are averaged and appened to a new csv file
helpfully, the desired data is always in characters 21-26, starting on line 4

useful ideas for coding:
    opening, reading and writing from files
    using glob to return files in a path

sam karpiniec

02jul2020 v0.1 first version - does the job
07jul2020 v0.2 moved open cmds outside loop; added column titles
               added sorted() around filename list
10jan2022 v0.3 added line length check while parsing csv; should prevent blankline fail
'''

import glob
list=open('C:/tmp/avg_2021_q4.csv','a+')
list.write('filename,conductivity,\n')

for datafilez in sorted(glob.iglob('c:/tmp/test/*.CSV')):
    csv=open(datafilez,'r')
    print(datafilez)
    lines=csv.readlines()
    csv.close()

    values=[]

    #add each value to list, sliced from input data
    #skip if line length is 1 (i.e. blank line)
    #normal line length is 74
    for x in range(3,len(lines)):
        if len(lines[x])!=1:
            values.append(float(lines[x][20:26]))

    avg=sum(values)/len(values)

    list.write(datafilez[-10:]+',')
    list.write(str(avg)+'\n')

list.close()
