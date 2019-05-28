def rc1(n):
    if ((not isinstance(n, int)) or (n > 100)): return False
    total = 0
    while (n > 0):
        total = 10*total + n%10
        n //= 10
    return total

print(rc1(96))