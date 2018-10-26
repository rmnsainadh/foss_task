import random
a=["rock","paper","scissors"]
suma=0
sumb=0
i=1
while(i>=0):
    b=input()
    c=random.choice(a)
    print(c)
    if(b==c):
        print("tie no score")
    elif(b=="paper" and c=="rock"):
        print("user got points")
        suma=suma+5
    elif(b=="paper" and c=="scissors"):
        print("computer got points")
        sumb=sumb+5
    elif(b=="rock" and c=="scissors"):
        print("user got points")
        suma=suma+5
    elif(b=="rock" and c=="paper"):
        print("computer got points")
        sumb=sumb+5
    elif(b=="scissors" and c=="paper"):
        print("user got points")
        suma=suma+5
    elif(b=="scissors" and c=="rock"):
        print("computer got points")
        sumb=sumb+5
    if(suma==20 or sumb==20):
        break
if(suma>sumb):
    print(suma)
    print(" user won")
else:
    print(sumb)
    print(" computer won")
