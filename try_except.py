# Python code to illustrate 
# working of try() 

def div(x,y):
    try:
        res=x//y
        print("OK your answer is : ",res)
    except ZeroDivisionError:
        print("You are doing wrong")

divide(5,0)        
