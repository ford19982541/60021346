L = [5,6,10,23,25,30,32,37,50,68]
val = len(L)
Order = []
if not val % 2 == 0 :
    Answer = (L[((val+1)//2)-1])
else:
    Order.append(((val+2)//2)-1)
    Order.append((val//2)-1)
    Answer = ((L[Order[0]]+L[Order[1]])//2)
print(Answer)

