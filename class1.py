# class1.py
#1)클래스형식 정의
class Person:
    #초기화 메서드(첫번째 인자는 자기 자신-self)
    def __init__(self):
        #인스턴스 멤버 변수
        self.name = "default name"
    #인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person() 
p1.name = "전우치"
p2.name = "이순신"
p1.print()
p2.print() 

#런타임시에 추가
Person.title = "new title"
print( p1.title )
print( p2.title )
print( Person.title )