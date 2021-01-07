import glob
for filez in glob.iglob('c:/tmp/test/*'):
#    print(filez)
    la=open(filez,'r')
    print(la.readlines())
    la.close()
