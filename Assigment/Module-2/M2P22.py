str = input("Enter the string :")

if len(str)%4 == 0:
    rev_str = str[::-1]
    print(rev_str)
    
else :
    print("Enter the valid string !!")
