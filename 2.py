def int_to_binary(n):
    # Base case: if n is 0 or 1, return it as a string
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        # Recursive case: divide the number by 2 and concatenate the remainder
        return int_to_binary(n // 2) + str(n % 2)

# Example usage
number = int(input("Enter an integer: "))
binary = int_to_binary(number)
print(binary)


