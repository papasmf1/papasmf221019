# demoRE.py 
import re 

# print( dir(re) )

#정규표현식(특정한 규칙): [0-9] 숫자가 *(0~N번) th 
result = re.search("[0-9]*th", "35th")
print( result )
print( result.group() ) 
#매칭 오브젝트 
result = re.match("[0-9]*th", "35th")
print( result )
print( result.group() ) 

print("---search함수 사용---")
print( bool(re.search("apple", "this is apple")) )
print( bool(re.match("apple", "this is apple")) )

result = re.search("\d{4}", "올해는 2022년입니다.")
print( result.group() )
result = re.search("\d{5}", "우리 동네는 52100입니다.")
print( result.group() )
