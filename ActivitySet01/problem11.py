# Tuples

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hcount={}
hlist=[]
for i in handle:
    wd=i.split()
    if len(wd)>1 and wd[0]=='From':
        hr=wd[5].split(':')
        hcount[hr[0]]=hcount.get(hr[0],0)+1
    else:
        continue
for k,v in hcount.items():
    hlist.append((k,v))
hlist.sort()
for k,v in hlist:
    print (k,v)

