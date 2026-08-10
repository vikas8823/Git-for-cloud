# 1. Square pattern
for i in range(5):
    print("* " * 5)

# 2. Right triangle pattern
for i in range(1, 6):
    print("* " * i)

# 3. Inverted right triangle
for i in range(5, 0, -1):
    print("* " * i)

# 4. Pyramid pattern
n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)

# 5. Number pattern
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()