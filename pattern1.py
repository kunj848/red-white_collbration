n = int(input("Enter rows: "))

for i in range(1, n * 2):

    if i <= n:
        star = i
    else:
        star = n * 2 - i

    space = 2 * (n - star)

    left = "*" * star
    middle = " " * space
    right = "*" * star

    print(left + middle + right)