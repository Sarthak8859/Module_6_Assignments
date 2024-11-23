#l Write a program to print multiplication tables from 1 to 5, but stop after the first table is printed for each number.
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    break
