#Description : Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
#The function should just print the keys only.

for i in range(1,21):
    d={i:i*i}
    print(list(d.keys()))
