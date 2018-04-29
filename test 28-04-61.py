#อนุกรมเลขคณิต 0' จงหาค่า d
a= int(input())
b= int(input())
diga = a-b
digb = 9
ans = 1
tmp = ans* digb
while  :
    if not tmp == diga :
        ans += 1
    else :
        print(ans)


