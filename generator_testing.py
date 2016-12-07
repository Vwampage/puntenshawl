import data_parser



words_as_key = data_parser.create_dict(data_parser.open_dictionary())

def generator_test():
	num = 0
	while num < 100:
		yield num
		num += 1

print sum(generator_test())