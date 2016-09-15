def generator_test():
	num = 0
	while num < 100:
		yield num
		num += 1

print sum(generator_test())