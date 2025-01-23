def fibonacci(n):
   
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Get input from the user
term = int(input("Enter the number of terms for the Fibonacci series:"))

# Print the Fibonacci series
print("Fibonacci Series:")
for i in range(term):
    print(fibonacci(i), end=" ")