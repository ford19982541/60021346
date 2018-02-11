#1. ให้เขียนโปรแกรมเพื่อรับค่าตัวเลข 3 จำนวนจากนั้นให้หาค่าที่มีค่าน้อยที่สุดในสามจำนวนนั้น
'''
a = int(input())
b = int(input())
c = int(input())
abc = [a,b,c]
print(min(abc))'''
#2. ให้เขียนโปรแกรมเพื่อรับค่าตัวเลขจำนวนเต็ม ไปเรื่อยๆ จนกว่าผู้ใช้จะผู้ใช้จะพิมพ์ค่า 0 จากนั้นให้แสดงผลรวมของเลขจำนวนที่ผู้ใช้พิมพ์
'''
a = int(input())
sum = 0
while not a == 0:
    sum += a
    a = int(input())
print(sum)'''
#3.ให้เขียนโปรแกรมเพื่อรับค่าเลขจำนวนเต็มบวก 1 จำนวน (n) จากนั้นจะต้องรับค่าอีกจำนวน n ค่า จากนั้นให้หาผลบวกของตัวเลขคี่จากเลขทั้ง n จำนวนนั้น
'''
a = int(input())
sum = 0
for i in range(a):
    a = int(input())
    if not a % 2 == 0:
        sum += a
print(sum)'''
#ให้ L เป็นลำดับของเลขจำนวนเต็ม จำนวน n ตัว ให้หาลำดับของเลขที่มีค่าใกล้กับค่าเฉลี่ยมากที่สุด
'''
L = [1,2,3,4,5,6,7,8,9]
val = len(L)
avgofL = sum(L)/val
close_val = []
for i in L:
    close_val.append(abs(i-avgofL))
ans = L.index(min(close_val)+avgofL)
print(ans)
'''

#ให้ L เป็นลำดับของเลขจำนวนเต็มจำนวน n ตัวให้หาตำแหน่งของตัวเลขที่มีค่าที่มากที่สุดที่น้อยกว่าค่าเฉลี่ย
'''
L = [569,981,782,739,150,301,416,125,68,847]
val = len(L)
close_val = 0
avgofL = sum(L)/val
for i in L:
    if i < avgofL and close_val < i:
        close_val = i
print(L.index(close_val))
'''
#ให้ L เป็นลำดับของเลขจำนวนเต็มจำนวน n ตัว
#ให้หาตำแหน่งเริ่มต้นของตัวเลข (ตั้งแต่ตำแหน่ง 0 ถึง n-3)
#  ที่มีเลขในลำดับถัดไปอีก 2 ลำดับ (รวมตัวเอง) ทั้งหมด 3 จำนวน เรียงจากน้อยไปหามาก
#เช่น 1,2,1,2,1,2,3,1,2,1
#ตอบ ตำแหน่งที่ 4 เพราะ ตำแหน่งที่ 4 มีค่าเป็น 1 และตำแหน่งที่ 5,6 มีค่าเป็น 2,3 ตามลำดับทำให้
#1,2,3 เป็นเลขที่เรียงกันจากน้อยไปหามากตำแหน่งแรก
'''
L = [1,2,1,2,1,2,3,1,2,1]
val =len(L)
Order = 'none'
for i in range(val-3) :
    if L[i]<L[i+1]<L[i+2] :
        Order =  i
print(Order)
'''
#จงเขียนเกมที่มีผู้เล่นสองคน ผู้เล่นจะสลับกันกรอกข้อมูลตัวเลขจำนวนเต็ม ที่มีค่า 1 จนถึง 13 
#ผู้เล่นคนใดกรอกตัวเลขแล้วทำให้ผลรวมของตัวเลขทั้งหมดมีค่ามากกว่า 99 จะถือว่าผู้เล่นคนดังกล่าวแพ้
#ให้นิสิตเขียนโปรแกรมเพื่อพัฒนาเกมดังกล่าว

while(1):
    select_input = (input('''******* Welcome to 99 bombs. *******
******* Please select number to continue. *******
    1. Start game.
    2. Read the rules of play.
    0. Exit.'''))
    if select_input == '1' :
        score = 0
        while not score > 99:
            ply_1 = int(input('Player 1 please enter number. : '))
            if ply_1 <1 or ply_1 >13 :
                ply_1 =int(input('Fill in the numbers,Please fill in again. :'))
            score += ply_1
            if score > 99:
                print('Game Over')
                print('Player 2 Win !!')
            elif score == 99:
                print('You are the winer.')
            ply_2 = int(input('Player 2 please enter number. : '))
            if ply_2 <1 or ply_1 >13 :
                ply_2 =int(input('Fill in the numbers,Please fill in again. :'))
            score += ply_2
            if score > 99:
                print('Game Over')
                print('Player 1 Win !!')
            elif score == 99:
                print('You are the winer.')
    elif select_input == '2' :
        print('''
              -Rules.........
    -With two players, The player will
alternately fill in the integer numbers
1 through 13.Any player entering a number 
makes the total of all numbers greater
than 99. It is considered that the player loses.''')
        
    elif select_input == '0' :
        exit(0)

