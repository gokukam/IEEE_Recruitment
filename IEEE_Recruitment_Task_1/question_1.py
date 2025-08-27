# Accepting number of rows for pattern
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    spc = n - i  # Padding with spaces to make pattern

    # Using str duplication to print pattern
    print(" " * spc + "*" * i)
