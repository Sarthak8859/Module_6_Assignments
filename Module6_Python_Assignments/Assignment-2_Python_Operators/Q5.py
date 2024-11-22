#5. Check the Identity of Variables:
a = [1, 2, 3]
b = a

print(f"a is b: {a is b}")  # True
print(f"a == b: {a == b}")  # True

b = [1, 2, 3]
print(f"a is b: {a is b}")  # False
print(f"a == b: {a == b}")  # True
