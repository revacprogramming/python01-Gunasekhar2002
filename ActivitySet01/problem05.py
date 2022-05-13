#functions to compute pay
def computepay(h,r):
    if (h==40):
        pay=hrs
    elif (h>=40):
        pay=40*r+(h-40)*r*1.5
        return pay
hrs=input('enter hours:')   
h=float(hrs)
rate=input('enter hours:')
r=float(rate)
pay=computepay(h,r)
print('Pay',pay)