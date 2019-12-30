#LSB
num=int(input("enter a number"))
if(num&1):
    print(num,"is a lsb set")
else:
    print(num,"is not lsb set")
    


#MSB
BITS=32
num=int(input("Enter a number: "))
msb = 1 << (BITS - 1);
if(num & msb):
        print("MSB is set", num);
else:
    
    printf("MSB of is unset (0).", num);
