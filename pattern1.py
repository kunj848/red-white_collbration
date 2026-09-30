n = int(input("Enter rows: "))

print("\n✨ Butterfly Pattern ✨\n")

for i in range(1, n * 2):

    if i <= n:
        star = i
    else:
        star = n * 2 - i

    space = 2 * (n - star)

    print("*" * star + " " * space + "*" * star)