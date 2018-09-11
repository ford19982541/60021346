# 5.8
'''
s = input()
hid1 = s.find('h')+1
hid = s.find('h')
h = s.rfind('h')-1
print(s[:hid1]+s[h:hid:-1]+s[h+1:])
# answer 5.8 ########################################
s = input()
first_pos, last_pos = s.find('h') + 1, s.rfind('h')
left, middle, right = s[:first_pos], s[first_pos:last_pos], s[last_pos:]
print(left + middle[::-1] + right)'''
##################################################n
'''# 6.3
number = int(input())
n = 1
i = 0
max_1 = 0
while i <=number:
    i = 2**n
    if max_1 <= i:
        max_1 = i
        n += 1
print(n-2, max_1-(2**(n-2)))
# answer 6.3 ########################################
x = int(input())
n = 1
while 2 ** n <= x:
  n += 1
print(n - 1, 2 ** (n - 1))'''
###################################################
'''6.E
a = int(input())
value = 1
max_value = 1
while not a == 0:
  pre , a = a, int(input())
  if pre == a:
    value +=1
  else:
    value +=0
    max_value = max(value,max_value)
print(max_value)
##################################################################
'''
'''
l = [ int(x) for x in input().split()  ]
l2 = []
for i in range(1,len(l)) :
    if l[i]%2 == 0:
        l2[0].append(l[i])
print (' '.join([str(x) for x in l2 ]))'''

a = [int(s) for s in input().split()]
print(max(a),a.index(max(a)))