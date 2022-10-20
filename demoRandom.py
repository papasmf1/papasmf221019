# demoRandom.py 
import random

print( random.random() )
print( random.random() )

#리스트 컴프리헨션(리스트 내장)
print( [random.randrange(20) for i in range(10)] )
print( [random.randrange(20) for i in range(10)] )

print("---샘플링---")
print( random.sample(range(20), 10) )
print( random.sample(range(20), 10) )

import math 
#올림연산(4를 리턴)
print( math.ceil(3.14) )
#내림연산(3을 리턴)
print( math.floor(3.14) )
#반올림
print( round(1.674, 2) )


