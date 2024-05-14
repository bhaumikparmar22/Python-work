string1 = input("Enater the 1st string : ")
string2 = input("Enter the 2th string : ")

swapped_string1 = string2[:2] + string1[2:]
swapped_string2 = string1[:2] + string2[2:]

print(swapped_string1,"",swapped_string2)
