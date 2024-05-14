def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get user input for the number
user_input = int(input("Enter a number: "))

# Check if the input is non-negative
if user_input < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and display the factorial
    factorial_result = calculate_factorial(user_input)
    print(f"The factorial of {user_input} is: {factorial_result}")
