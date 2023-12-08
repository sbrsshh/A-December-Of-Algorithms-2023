x=[]
sum=0
average=0
total=0
n=int(input("enter the number of thieves  :"))
for i in range(0,n):
    a=int(input("amount theft :"))
    x.append(a)
    sum+=a
average = sum/n
print("Average amount stolen:",average)
for i in range(0,n):
    if(x[i] >= average):
        total += x[i]
print("Sum of elements greater than or equal to the average:",total)
