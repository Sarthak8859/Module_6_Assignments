#Write a program to skip printing even numbers using a while loop.
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
