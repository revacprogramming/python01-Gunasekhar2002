# Strings
str="X-DSPAM-Confidence:    0.8475"
n=str.find(':')
fstr=str[n+1:]
l=float(fstr)
if (l==0.8475):
   
    print(l)
else:
    print('not found')
