input_string = input("Enter the string :")

# Find the index of 'not' and 'poor'
index_not = input_string.find('not')
index_poor = input_string.find('poor')

# Check if 'not' appears before 'poor' and both are present
if index_not != -1 and index_poor != -1 and index_not < index_poor:
     # Replace the 'not'...'poor' substring with 'good'
     result_string = input_string[:index_not] + 'good' + input_string[index_poor + 4:]
else:
    # If 'not' doesn't follow 'poor' or one of them is not present, return the original string
    print("Enter the valid string!!")
    result_string = input_string
    
print(result_string)
