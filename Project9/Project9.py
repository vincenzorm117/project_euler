def main():


	for x in xrange(1,1000):
		for y in xrange(x+1,1000):
			for z in xrange(y+1,1000):
				if( (x*x + y*y) == (z*z)):
					if ((x+y+z) == 1000 ):
						print "x: " + str(x) + " y: " + str(y) + " z: " + str(z)

main()