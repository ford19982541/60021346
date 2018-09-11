#อนุกรมเลขคณิต 0' จงหาค่า d
'''
n= int(input())
data = []
nu = 0
a = 0
b = 0
c = 0
d = 0
f = 0
while nu < n :
    m = str(input())
    data.append(m)
    nu += 1
for i in range (len(data)):
    if "a" == data[i] or data[i]== "A":
        a += 1
    elif "b" == data[i] or data[i] == "B":
        b += 1
    elif "c" == data[i] or data[i] == "C":
        c += 1
    elif "d" == data[i] or data[i]  == "D":
        d += 1
    elif "f" == data[i] or data[i] == "F":
        f += 1

print(a,b,c,d,f)
'''
n = int(input())
even = 0
odd = 0
while  n>=1 :
    if n%2 == 0 :
        even += n
    elif n%2 != 0 :
        odd += n
    n = int(input())
print(even)
print(odd)


