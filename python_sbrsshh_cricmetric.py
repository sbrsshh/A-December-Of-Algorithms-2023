run =[]
total =0
highest =0
a =0

x = int(input("number of player :"))
n= x+1
for i in range(1,n):
    print("player", i, "score:")
    value = int(input())
    run.append(value)

for i in range(1,x):
    total += run[i]

print("total runs",total)
highest=max(run)

for i in range(1,x):
    if highest == run[i]:
        print("highest score index:",i)
