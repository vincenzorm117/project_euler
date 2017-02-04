import math

def isPrime(prime):
	
	half = int(math.ceil(math.ceil(prime)))
	
	if(prime == 2):
		return True
		
	if(prime % 2 == 0):
		return False

	for i in xrange(3,half, 2):
		if( prime % i == 0):
			return False

	return True


def main():
	count = 0
	val = 1

	while(count < 10001):
		val += 1
		
		if(isPrime(val)):
			count += 1
			print str(count) + ":" + str(val)

main()