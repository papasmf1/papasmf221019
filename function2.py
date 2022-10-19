# function2.py 
#함수 정의
def change(x):
    x[0] = "H"
#함수 호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출후:", wordlist)
#약간의 변경
#함수 정의
def change(x):
    #전체를 복사하도록 함(Deep copy)
    x1 = x[:]
    x1[0] = "H"
    print("함수내부:", x1)
#함수 호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출후:", wordlist)

print("--전역변수 지역변수---")
x = 2 
def func1(a):
    return a+x 
#호출
print( func1(1) )

def func2(a):
    x = 5 
    return a+x 
#호출 
print( func2(1) )

#디버깅 연습 예제
def intersect(preslist, postlist):
    #교집합 글자를 담기위한 리스트
    result = []
    #H(0)|A(1)|M(2)
    for x in preslist:
        #특정 글자가 postlist에 있고 x가 result에 없으면(True and True) 
        if x in postlist and x not in result:
            result.append(x)
    return result 
#호출
print( intersect("HAM","SPAM"))

#기본값 명시
def times(a=10,b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드 인자
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL 

#호출
print( connectURI("ycampus.com", "80") )
print( connectURI(port="8080", server="ycampus.com") )

#가변인자(입력 파라메터가 갯수가 가변적)
def union(*ar):
    result = []
    #HAM(0) | EGG(1)
    for item in ar:
        #H(0) | A(1) | M(2)
         for x in item:
            #특정 글자가 result에 없으면
            if x not in result:
                result.append(x)
    return result  

#호출
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )

