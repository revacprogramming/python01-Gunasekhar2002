# Files

#filename = "dataset/mbox-short.txt"

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name:")
count=s=0;
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count+=1
        f=line.find('0')
        x=line[f:]
        s+=float(x)
averg=s/count
print('Average spam confidence:',averg)
        
  


