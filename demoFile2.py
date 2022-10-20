# demoFile2.py
#파일 쓰기(유니코드로 쓰기와 읽기)
f = open("c:\\work2\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close() 

#파일 읽기 
f = open("c:\\work2\\demo.txt", "rt", encoding="utf-8")
#전체 문자열을 str로 리턴 
print( f.read() )

print( f.tell() )
#리셋(다시 처음으로 이동)
f.seek(0)
result = f.readlines()
print( result )
for item in result:
    #코드를 보정 
    print(item, end="")

print("---한줄씩 읽기---")
f.seek(0)
print( f.readline(), end="" )
print( f.readline(), end="" )

f.close() 

