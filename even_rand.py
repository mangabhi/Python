#Description : Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

import random
resp = random.sample([i for i in range(0,11) if i%2==0],1 )
print(resp)
