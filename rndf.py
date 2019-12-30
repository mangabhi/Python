#This program will cause error because its neither divisble by 5 nor 7
import random
resp = random.sample([i for i in range(0,10) if i%5==0 and i%7==0],3)
print(resp)
