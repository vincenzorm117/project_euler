import math

def isPrime(prime):
	
	half = int(math.ceil(math.ceil(prime)))
	
	if(prime % 2 == 0):
		return False

	for i in xrange(3,half, 2):
		if( prime % i == 0):
			return False

	return True


def main():

	sum = 2

	for x in xrange(3,2000000,2):
		if(isPrime(x)):
			sum += x

	print sum

main()