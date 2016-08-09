import older
tests=0
passed=0
for symbol in dir(older):
	attr=getattr(older,symbol)
	if(callable(attr) and attr.__name__.startswith('test_')):
		if attr():
			passed += 1
		tests += 1
print 'Number of tests executed : %d and Number of tests passed : %d' %(tests,passed)
