#Count the number of vowels in a string using a for loop.
string = "Hello, World!"
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels in '{string}': {count}")
