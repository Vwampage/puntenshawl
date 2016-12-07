import data_parser



words_as_key = data_parser.create_dict(data_parser.open_dictionary())

def dict_by_sounds():
	keywords = {}
	for key in words_as_key.keys():
		if tuple(words_as_key[key]) not in keywords.keys():
			keywords[tuple(words_as_key[key])] = []
		# 	keywords[tuple(words_as_key[key])].append(key)
		# else:
		
		keywords[tuple(words_as_key[key])].append(key)
		# keywords[tuple(words_as_key[key])] = [].append(key)
	return keywords


sounds_as_key = dict_by_sounds()


print sounds_as_key
# print words_as_key

# print sounds_as_key[['S', 'EH1', 'L', 'K']]


