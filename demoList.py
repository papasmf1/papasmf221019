# demoList.py
strA = "python is very powerful"
print( strA[0] )
print( strA[0:6] )
print( strA[:6] )
print( strA[-1] )
print( strA[-3:] )
print( len(strA) )

print("---list연습---")
colors = ["red","blue","green"]
print( colors )
print( len(colors) )
print( colors[0] )
colors.append("white")
print( colors )
colors.insert(1, "yellow")
print( colors )
print( colors.index("red") )
colors += ["red"]
colors += "red"
print( colors )
colors.remove("blue")
print( colors )

print("---set---")
a = {1,2,3,3}
b = {3,4,5,5,6}
print(a)
print(b)
print( type(a) )
print( a.union(b) )
print( a.intersection(b) )

print("---tuple---")
tp = (1,2,3)
print( len(tp) )
#중단점(Break Point)
for item in tp:
    print(item)

#함수 정의
def calc(a,b):
    return a+b, a*b 

#호출
result = calc(5,6)
print(result)

print("id:%s, name:%s" % ("kim","김유신"))

print("---형식변환---")
a = list((1,2,3))
a.append(4)
print(a)

