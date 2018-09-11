import math
class calcu_Area :
    width = None
    height =None
    side = None
    base = None
    diagonal = None
    radius = None
    half = 1/2
    def __init__(self):
        self.width = 0
        self.height = 0
        self.side = 0
        self.base = 0
        self.diagonal = 0
        self.radius = 0

    def triangle (self) : # 3 เหลี่ยม
        area = self.half*(self.height*self.base)
        return area
    @property
    def triangle_side (self): # 3 เหลี่ยมด้านเท่า
        area = (math.sqrt(3)/4)*(self.side**2)
        return area
    def triangle_gable (self): # 3 เหลี่ยมหน้าจั่ว
        area = (self.base/4)*(((self.side**2)-(self.base**2))**(1/4))
        return area

    def squares(self): # 4 เหลี่ยมจัสตุรัส
        area = self.side**2
        return area
    def rectangle(self): # 4 เหลี่ยมผืนผ้า
        area =  self.width*self.height
        return area
    def parallelogram(self): # 4 เหลี่ยมด้านขนาน
        area = self.height*self.base
        return area

    def circle(self): #วงกลม
        area = math.pi*(self.radius**2)
        return area


def Triangle_1 (Height,Base):
    user = calcu_Area()
    user.height = Height
    user.base = Base
    return user.triangle()
def Triangle_2 (Side):
    user = calcu_Area()
    user.side = Side
    return user.triangle_side


def Triangle_3 (Side,Base):
    user = calcu_Area()
    user.Side = Side
    user.base = Base
    return user.triangle_gable()


def Squares (Side):
    user = calcu_Area()
    user.side = Side
    return user.squares()
def Rectangle (Width,Height):
    user = calcu_Area()
    user.width = Width
    user.height = Height
    return user.rectangle()
def Parallelogram(Height,Base):
    user = calcu_Area
    user.height = Height
    user.base = Base
    return user.parallelogram(user)
def Circle(Radius):
    user = calcu_Area
    user.radius = Radius
    return user.circle(user)


while(1):
    print('โปรแกรมคำนวณพื้นที่ \nเลือกพื้นที่ ที่ต้องการคำนวณ \nกด 0 เพื่อออก \n1.พื้นที่สามเหลี่ยม\n2.พื้นที่สามเหลี่ยมด้านเท่า \n3.พื้นที่สามเหลี่ยมหน้าจั่ว\n4.พื้นที่สี่เหลี่ยมจัตสุรัก\n5.พื้นที่สี่เหลี่ยมผืนผ้า \n6.พื้นที่สี่เหลี่ยมด้านขนาน \n7.พื้นที่วงกลม')
    menu = str(input())
    if menu == '0' :
        exit(0)
    elif menu == '1':
        Height = int(input('ความสูงของสามเหลี่ยม :'))
        Base = int(input('ความยาวของฐาน :'))
        print('พื้นที่มีขนาด = ',Triangle_1(Height,Base))
    elif menu == '2':
        Side = int(input('ความยาวด้าน :'))
        print('พื้นที่มีขนาด = ',Triangle_2(Side))
    elif menu == '3':
        Side = int(input('ความยาวด้าน :'))
        Base = int(input('ความยาวของฐาน :'))

        print('พื้นที่มีขนาด = ',Triangle_3(Side,Base))
    elif menu == '4':
        Side = int(input('ความยาวด้าน :'))
        print('พื้นที่มีขนาด = ',Squares(Side))
    elif menu =='5':
        Width = int(input('ความกว้าง :'))
        Height = int(input('ความสูง :'))
        print('พื้นที่มีขนาด = ',Rectangle(Width,Height))
    elif menu == '6':
        Height = int(input('ความสูง :'))
        Base = int(input('ความยาวของฐาน :'))
        print('พื้นที่มีขนาด = ',Parallelogram(Height,Base))
    elif menu == '7' :
        Radius = int(input('รัศมี :'))
        print('พื้นที่มีขนาด = ',(Circle(Radius)))
    else:
        print('Button Error ! \n ')