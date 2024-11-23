#Generate a multiplication table using nested loops.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end=" ")
    print()

