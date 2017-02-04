def main():
	fib = [0,1,1]
	i = 2
	sum = 0

	while(fib[i] < 4000000):
		i = (i+1)%3
		fib[i] = fib[((i-1)%3+3)%3] + fib[((i-2)%3+3)%3]
		if(fib[i] % 2 == 0):
			sum += fib[i]

	print sum

main()