one=1
while(1):
    a=input("Enter a number:")
    if(a == "done"):break
    try:
        b=int(a)
        if(one==1):
            max=min=a
            one+=1
        if(a>max):max=a
        if(a<min):min=a
    except:print("Invalid input")
if(one==1):print("no number input")
else:print("max number:",max,"\nmin number:",min)
