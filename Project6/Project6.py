import math

def squareOfSum(min , max):
	sum = 0

	for x in xrange(min, max+1):
		sum += x

	return sum*sum


def sumOfSquares(min , max):
	sum = 0

	for x in xrange(min, max+1):
		sum += (x*x)

	return sum

def main():
	
	print (squareOfSum(1,100) - sumOfSquares(1,100))

main()