# Loops & Iterators

large=0
small=0 
while True:
    num = input("Enter a number:")
    if num == "done": 
        break;
    try:
        num = int(num)
        if large==0 or large< num: 
            large = num
        elif small==0 or small>num: 
            small= num
    except:
        print("Invalid input")
        

print ("Maximum is",large)
print ("Minimum is",small)