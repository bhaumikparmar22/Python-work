str = input("Enter the string : ")

if len(str) >= 3:
        # Check if the string already ends with 'ing'
        if str.endswith('ing'):
            new_str = str + 'ly'
        else:
            new_str = str + 'ing'
else:
        # If the length is less than 3, leave it unchanged
        print("Enter the valid string!!")
        new_str = str
        
print(new_str)
