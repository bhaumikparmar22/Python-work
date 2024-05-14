print (">>>>>>>>""Withe using temp variable""<<<<<<<<<<")
a =int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
temp = None

temp = a
a = b
b = temp

print("After the swaping value of a :",a)
print("After the swaping value of b :",b)

print (">>>>>>>>""Witheout using temp variable""<<<<<<<<<<")

a =int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))

a,b = b,a

print("After the swaping value of a :",a)
print("After the swaping value of b :",b)
