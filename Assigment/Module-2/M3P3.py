def fibonacci(n):
    fib_series = [0,1]
    for i in range(2,n):
        next_tern = fib_series[i-1] + fib_series[i-2]
        fib_series.append(next_tern)
    return fib_series

num_terms = int(input("Enter the number of Fibonacci terms :"))

fibonacci_series = fibonacci(num_terms)
print("Fibonacci series up to ",num_terms , "terms :",fibonacci_series)
