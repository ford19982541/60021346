import math

def inn():
    print('\t กรอกชื่อ')
    print('Name :')
    name = input()
    print('How old are you?:')
    oldd = input()
    print("Hello :",name);
    print("so you are",oldd,"years old.")

def print_name_age(name,age):
    print("Student Name :",name)
    print("Student Age :",age)

def sum_two_integers(integer_a,integer_b) :
    integer_c = integer_a + integer_b
    print(integer_c)

def sum_a_b(a, b):
    c = a + b
    return c


def cvt_alpha_to_hours(alpha):  # หา ชม. จาก องศา
    ratio = alpha / 360
    hours = ratio * 12
    return hours


def find_min_from_hour(hour):  # หานาทีจากเศษ ชม.
    remaining_hour = math.fmod(hour, 1)
    return remaining_hour * 60


def find_minalpha_from_min(min):  # หาองศาจากค่านาที
    return min / 60 * 360

#gg