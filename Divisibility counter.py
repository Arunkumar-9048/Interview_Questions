# Program to count how many elements in a list are divisible by another list of numbers.
a = [1,2,8,9,12,46,76,82,15,20,30]
b= [1,2,3,4,5,6,7,8,9]
dic={}
count = 0

for i in b :
    for j in a:
        if j%i==0:
            count+=1
    dic[i] = count
    count=0

print(dic)
