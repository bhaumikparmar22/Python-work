# even and odd number.
num = int(input("Enter A Number :"))

rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")


#find the greatest  of 3 numbers entered by the user.
a = int(input("Enter A First Number :"))
b = int(input("Enter A First Number :"))
c = int(input("Enter A First Number :"))

if(a >= b and a >= c):
    print("First Number Is Largest", a)
elif(b >= c):
    print("Second Number Is Largest", b)    
else:
    print("Third Number Is Largest", c)


#check if a number is a multiple of 7 or not.
x=int(input("Enter A Number: "))

if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")    
        


    
        


