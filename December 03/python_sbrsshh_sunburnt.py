n=int(input("enter the num :"))
highest=0
view=0
h=[]

for i in range(0,n):
    x=int(input("enter its height  :"))
    h.append(x)

for i in h:
    if i>highest:
        highest= i
        view+=1

print("view from no. building :",view)