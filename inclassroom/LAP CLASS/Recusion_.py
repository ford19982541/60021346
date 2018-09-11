def sum_number(number):
    if number == 0:
        return 0
    else:
        return number+sum_number(number-1)
    
def print_number(number):
    start = 50
    if number == 0 :
        return 0
    else:
        print(start-(number-1))
        return(print_number(number-1))

def digit(n):
      if n < 10:
          return 1
      else:
          print(1+digit(n/10))
          return 1 + digit(n/10)