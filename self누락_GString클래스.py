#전역변수 
str = "Not Class Member"
#파이썬은 모호한 것보다는 명시적인 것이 좋다! 
class GString:
    def __init__(self):
        #인스턴스 멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(self.str)

#인스턴스 생성 
g = GString()
g.set("First Message")
g.print()
