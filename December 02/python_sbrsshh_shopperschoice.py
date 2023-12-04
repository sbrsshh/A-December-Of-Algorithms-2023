n = int(input("enter no. of items:"))
product= []
freq = []

for i in range (0,n):
    temp = int(input("enter product id:"))
    product.append(temp)

product = sorted(product)

freqen = {}
print(product)
for num in product:
    if num in freqen:
        freqen[num] += 1
    else:
        freqen[num] = 1

for i,j in freqen.items():
    freq.append(j)
    
print(freq)

