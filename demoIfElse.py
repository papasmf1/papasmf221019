# demoIfElse.py 
# if else만 - switch구문 
# 블럭 처리: ctrl + / 
# score = int(input("점수를 입력:"))
# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

#반복구문
value = 5 
while value > 0:
    print(value)
    value -= 1 

#딕셔너리
d = {"apple":100, "kiwi":200}
for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for k,v in d.items():
    print(k, v)

print("---break---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break 
    print("item:{0}".format(i))

print("---continue---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i % 2 == 1:
        continue 
    print("item:{0}".format(i))

#수열함수:규칙이 있는 숫자의 열 
print( list(range(10)) )
print( list(range(1,11)))
print( list(range(2000,2023)) )
#수동으로 반복경우 
for i in range(5):
    print(i)

print("---리스트 내장---")
lst = list(range(1,11))
print( lst )
print( [i**2 for i in lst if i > 5] )

