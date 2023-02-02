# class Pokemon:
#     def __init__(self, owener, skills):
#
#         self.owner = owener
#         self.skills = skills.split('/')
#         print(f"포켓몬 객체 생성됨")
#
#     def info(self):
#         print(f'{self.owner} have a pokemon')
#         for skill in self.skills:
#             print(skill)
#
#     def attack(self, idx):
#         print(f'{self.skills[idx]}공격 시전!')
#
# class Pikachu(Pokemon):  #inheritance
#     def __init__(self,owner,skills):
#         super.__init__(owner,skills)
#         print(f"피카츄")
#
# class kobugi(Pokemon):
#     def __init__(self,owner,skills):
#         super().__init__(owner,skills)
#         print(f'꼬부기')
#         print(f"{self.name}")
#
# # pi1 = Pikachu('덴트','번개')
# # pi1.info()
#
# # p1 = Pokemon('피카츄','한지우','50만 볼트/100만 볼트/번개')
# # p2 = Pokemon('꼬부기','오바람',)
#
# k1 = kobugi('jiwoo','고속스핀/거품/몸통박치기/하이드로펌프')
# k1.attack(2)

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def get_area(self):
        print('면적을 출력합니다')

import math
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, x, y, width,length):
        super().__init__(x, y)
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

    def __repr__(self):
        return f'원의 좌표는 x:{c1.x} y: {c1.y} 면적은: {c1.get_area()}'

c1 = Circle(100,100,10.0)
c2 = Circle(50,50,2.0)
r1 = Rectangle(100,50,5,2)

print(r1)
print(c2.get_area())
print(r1.get_area())


class Cylinder(Circle):
    def __init__(self,x,y,radius,height):
        super().__init__(x,y,radius)
        self.hight = height

    def get_area(self):
        return super().get_area()*self.height

