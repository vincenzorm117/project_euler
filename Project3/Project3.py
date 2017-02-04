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

	big = 600851475143

	half = 775147

	for x in xrange(half, 1, -1):
		if(big % x == 0):
			if(isPrime(x)):
				print x
				break

main()