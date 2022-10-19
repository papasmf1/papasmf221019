#부모 클래스
class Person:
    #초기화 메서드 
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
    def working(self):
        print("작업중")
    def coding(self):
        print("코딩중")

#자식 클래스 
class Student(Person):
    #상속 받은 초기화 메서드를 덮어쓰기(override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모 초기화 메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속 받아서 재정의(override)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID {1})".format(
            self.subject, self.studentID))          

#인스턴스 생성 
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "201122")
#object클래스에 구현된 요소들 
p.printInfo()
s.printInfo()
s.working()
s.coding()

