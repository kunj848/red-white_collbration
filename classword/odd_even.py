user_input = input("Enter a number (e.g. 10): ").strip()

parts = list(map(int, user_input.split()))

if len(parts) == 1:
    # From 1 to the entered number
    numbers = list(range(1, parts[0] + 1))
elif len(parts) == 2:
    # Between start and end
    start, end = parts[0], parts[1]
    numbers = list(range(start, end + 1))
else:
    numbers = parts

even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 != 0]

label = f"between {parts[0]} and {parts[1]}" if len(parts) == 2 else f"from 1 to {parts[0]}"
print(f"Even Numbers ({label}):", even)
print(f"Odd Numbers ({label}):", odd)

