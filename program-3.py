a = int(input("Enter a number: "))

if a==1 or a==2:
    print(1)
elif a%2==0:
    for i in range (1,(a*2)-2):
        if i%2!=0:
            print(i,end=" ")
else:
     print("else")
     for i in range (1,a*2):
        if i%2!=0:
            print(i,end=" ")
