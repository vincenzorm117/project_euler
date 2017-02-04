def isPalindrome(pal):
	siz = len(pal)

	for i in xrange(0,int(siz/2)+1):
		if(pal[i] != pal[siz-i-1]):
			return False

	return True


def findPal():

	nums = list()

	for x in xrange(999, 99, -1):
		for y in xrange(999, 99, -1):
			

			pal = str(x*y)
			if(isPalindrome(pal)):
				nums.append(int(pal))

	return nums
def main():

	nums = findPal()
	big = 0

	for x in nums:
		if(x > big):
			big = x

	print big

main()