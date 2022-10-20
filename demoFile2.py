# demoFile2.py
#파일 쓰기(유니코드로 쓰기와 읽기)
f = open("c:\\work2\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close() 

#파일 읽기 
f = open("c:\\work2\\demo.txt", "rt", encoding="utf-8")
print( f.read() )

f.close() 

