def sum_of_digits(n):
    """sum of digits of given number"""
    sod = 0
    while n != 0:
        sod += n % 10
        n //= 10
    return sod

# largest sum of digits
largest = 0

# for loop to get a and b
for a in range(90, 100):
    for b in range(90, 100):
        sod = sum_of_digits(a**b)
        if sod > largest:
            largest = sod

# printing the largest sum of digits
print(largest)
