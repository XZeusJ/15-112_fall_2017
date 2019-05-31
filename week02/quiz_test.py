import math

def ct1(x, y, z):
	print(x + y ** 2 - z * 2)
	print(100*int(y/x) + y/x)
	print(100*math.ceil(y/x) + y//x)
	y %= x + z
	return y
# print(ct1(2, 5, 7)) # hint: prints 4 values


def findDigit(n):
	move = 1
	while (0 < n):
		digit = n % 10
		print(digit)
		n //= 10
		move += 1
findDigit(11777372)