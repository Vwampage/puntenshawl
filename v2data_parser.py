def open_dictionary():
	unparseddict = []
	with open('dictionary/cmudict.txt','r') as f:
		for line in f.readlines():
			#should just do dictionary parsing here
			unparseddict.append(line)
	return unparseddict


def create_dicts(raw_dictionary):
	dictionary = {}
	for i in raw_dictionary:
		word_as_list = i.strip().split(' ')
		if '(' not in word_as_list[0]:
			dictionary[word_as_list[0]] = []
			dictionary[word_as_list[0]].append(word_as_list[2:])
		elif word_as_list[0][0] is '(':
			dictionary[word_as_list[0]] = []
			dictionary[word_as_list[0]].append(word_as_list[2:])
		else:
			dictionary[word_as_list[0][:-3]].append(word_as_list[2:])
	return dictionary

print create_dicts(open_dictionary())["YOU"]

