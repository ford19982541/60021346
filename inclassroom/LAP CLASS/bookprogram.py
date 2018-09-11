class reDate :
    day = None
    month = None
    year = None

    def __init__ (self):
        self.day = 0
        self.month = 0
        self.year = 0

    def calDay (self):
        if self.month == 1 and self.month == 3 and self.month == 5 and self.month == 7:
            if self.day > 31:
                return self.day-31
            else:
                return self.day
        elif self.month == 8 and self.month == 10 and self.month == 12:
            if self.day > 31:
                newDay = self.day-31
                return newDay
            else:
                return self.day

        elif self.month == 4 and self.month == 6 and self.month == 9 and self.month == 11:
            if self.day >30 :
                newDay = self.day - 30
                return newDay
            else:
                return self.day

        elif self.month == 2:
            if self.year %4 == 0:
                if self.day > 29:
                    newDay = self.day - 29
                    return newDay
                else:
                    return self.day
            else :
                if self.day > 28:
                    newDay = self.day - 28
                    return newDay
                else:
                    return self.day

    def calMonth(self):
        if self.month == 1 and self.month == 3 and self.month == 5 and self.month == 7:
            if self.day > 31 :
                newMonth = self.month + 1
                return newMonth
            else:
                return self.month
        elif self.month == 8 and self.month == 10:
            if self.day > 31 :
                newMonth = self.month + 1
                return newMonth
            else:
                return self.month

        elif self.month == 4 and self.month == 6 and self.month == 9 and self.month == 11:
            if self.day > 30 :
                newMonth = self.month + 1
                return newMonth
            else:
                return self.month

        elif self.month == 12 :
            if self.day > 31 :
                newMonth = 1
                return newMonth
            else:
                return self.month
        elif self.month == 2 :
            if self.year %4 == 0 :
                if self.day >29:
                    newMonth = self.month +1
                    return newMonth
                else:
                    return self.month
            else:
                if self.day >28 :
                    newMonth = self.month + 1
                    return newMonth
                else:
                    return self.month

    def calYear (self):
        if self.month == 12 :
            if self.day > 31 :
                newYear = self.year + 1
                return newYear
            else:
                return self.year
        else:
            return self.year

def day(d,m,y):
    dateSent = reDate()
    dateSent.day = d + 7
    dateSent.month = m
    dateSent.year = y
    return dateSent.calDay()

def month(d,m,y):
    dateSent = reDate()
    dateSent.day = d + 7
    dateSent.month = m
    dateSent.year = y
    return dateSent.calMonth()

def year(d,m,y):
    dateSent = reDate()
    dateSent.day = d + 7
    dateSent.month = m
    dateSent.year = y
    return dateSent.calYear()

def mateDate(date):
    newdate = date.split("/")
    Day = int(newdate[0])
    Moth = int(newdate[1])
    Year = int(newdate[2])

    sentday = (day(Day,Moth,Year))
    sentMonth = (month(Day,Moth,Year))
    sentYear = (year(Day,Moth,Year))
    return sentday,sentMonth,sentYear




book = 0
l = []
data = []
val = int(input('จำนวนหนังสือที่ยืม :'))
for i in range (val):
    print("BOOK :",i)
    bookId = int(input("BOOK ID :"))
    bookTitle = str(input('BOOK TITLE :'))
    dateBorrow = str(input('DATE BORROW :'))  # คำนวณวันส่งคืน
    print(mateDate(dateBorrow))

    # data.append(l)
    # book += 1



print(l)
print(data)



