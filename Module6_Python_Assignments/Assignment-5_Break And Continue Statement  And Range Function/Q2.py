#Write a program to iterate through a list and stop when encountering a specific element.
my_list = [1, 2, 3, 4, 5, 6]
specific_element = 4

for item in my_list:
    if item == specific_element:
        break
    print(item)
