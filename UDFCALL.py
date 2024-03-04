import UDF

while True:
    print("*"*50)
    print("1. oddeven")
    print("2. maxoftwo")
    print("3. maxofthree")
    print("4. fibonacci")
    print("5. prime")
    print("6. exit")
    print("*"*50)

    choice=int(input("enter choice:"))
    print("*"*50)

    if choice==1:
       a=int(input("enter value:"))
       print("*"*50)
       UDF.oddeven(a)
    elif choice==2:
        a=int(input("enter value:"))
        b=int(input("enter value:"))
        print("*"*50)
        UDF.maxoftwo(a,b)
    elif choice==3:
        a=int(input("enter value:"))
        b=int(input("enter value:"))
        c=int(input("enter value:"))
        print("*"*50)
        UDF.maxofthree(a,b,c)
    elif choice==4:
        a=int(input("enter value:"))
        print("*"*50)
        UDF.fibonacci(a)
    elif choice==5:
        a=int(input("enter value:"))
        print("*"*50)
        UDF.prime(a)
    elif choice==6:
        print("thank you for using servecies....")
        print("*"*50)
        break
    else:
        print("wrong choice please try again")
        print("*"*50)
        

               
    
