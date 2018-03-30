val = 0
score_user1 = 0
score_user2 = 0
if val == 0:
    user_1 = int(input("User_1 please enter number. = "))
    if user_1 > 13 and user_1 < 1 :
        print('Excess numbers are re-filled.')
        val = 0
    elif score_user1 > 99 :
        print('You loss.\n User_2 Win.')
    else:
        score_user1 += user_1
        val = 1
elif val == 1 :
    user_2 = int(input("User_2 please enter number. = "))
    if user_2 > 13 and user_2 < 1 :
        print('Excess numbers are re-filled.')
        val = 0
    elif score_user2 > 99 :
        print('You loss.\n User_1 Win.')
    else:
        score_user2 += user_2
        val = 0