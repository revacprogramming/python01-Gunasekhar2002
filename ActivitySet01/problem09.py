# Lists


fname = input("Enter file name:")
fh = open(fname)
lst=[]
for line in fh:
    L=line.split()
    for i in L:
        if i not in lst:
            lst.append(i)
            
lst.sort()
print(lst)