# demoRE.py 
import re 

# print( dir(re) )

#정규표현식(특정한 규칙)
result = re.search("[0-9]*th", "35th")
print( result )
print( result.group() ) 

result = re.match("[0-9]*th", "35th")
print( result )
print( result.group() ) 

