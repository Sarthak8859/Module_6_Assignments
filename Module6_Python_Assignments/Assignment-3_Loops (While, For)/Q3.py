#Calculate the factorial of a number using a for loop.
# Prompt the user to enter a number
n = int(input("Enter a number to calculate its factorial: "))

# Initialize the factorial variable
factorial = 1

# Calculate the factorial using a for loop
for i in range(1, n + 1):
    factorial *= i

# Print the result
print(f"Factorial of {n} is: {factorial}")

