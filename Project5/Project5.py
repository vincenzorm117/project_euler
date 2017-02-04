def isPrime(prime):
	
	half = int(math.ceil(math.ceil(prime)))
	
	if(prime % 2 == 0):
		return False

	for i in xrange(3,half, 2):
		if( prime % i == 0):
			return False

	return True


def areFactors(set, val):
	
	for x in set:
		if(val == 1):
			return True
		if(val % x == 0):
			val /= x

	return False


def isolateFactors(set, val):
	factors = list()

	if(isPrime(val)):
		factors.append(val)
	else:
		if(areFactors(set, val)):
			for x in set:
				if(val == 1):
					break
				if(val % x == 0):
					factors.append(x)
					val /= x

	return factors



def smallestProductOfRange(min , max):
	
	right = list()
	left = list()

	for x in xrange(min,max+1):
		if(isPrime(x)):
			right.append(x)
		else:
			left.append(x)

		



def main():
	
	print isolateFactors([2,3,4] , 6)

main()