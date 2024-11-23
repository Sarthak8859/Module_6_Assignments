#Write a program to skip printing even numbers from 1 to 10.
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
