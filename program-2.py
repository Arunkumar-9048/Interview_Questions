a = int(input("Enter a number: "))

if a==1:
    print(1)
else :
    for i in range (1,a*2):
        if i%2!=0:
            print(i,end=" ")