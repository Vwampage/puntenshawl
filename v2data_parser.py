def open_dictionary():
	unparseddict = []
	with open('dictionary/cmudict.txt','r') as f:
		for line in f.readlines():
			#should just do dictionary parsing here
			if line.startswith(';;;'):
				continue
			unparseddict.append(line)
	return unparseddict


def create_word_key_dict(raw_dictionary):
	dictionary = {}
	for i in raw_dictionary:
		word_as_list = i.strip().split(' ')
		word = word_as_list[0]
		pronunciation = tuple(word_as_list[2:])
		if word[-1:] is ')':
			if word[:-3] in dictionary:
				dictionary[word[:-3]].append(pronunciation)
			else:
				dictionary[word[:-3]] = []
				dictionary[word[:-3]].append(pronunciation)
		else:
			if word in dictionary:
				dictionary[word].append(pronunciation)
			else:
				dictionary[word] = []
				dictionary[word].append(pronunciation)
	return dictionary

def create_phoneme2_key_dict(raw_dictionary):
	dictionary = {}
	for i in raw_dictionary:
		word_as_list = i.strip().split(' ')
		word = word_as_list[0]
		pronunciation = tuple(word_as_list[2:])
		if pronunciation in dictionary:
			if word[-1:] is ')':
				dictionary[pronunciation].append(word[:-3])
				dictionary[pronunciation].append(word)
		elif word[-1:] is ')':
			dictionary[pronunciation] = []
			dictionary[pronunciation].append(word[:-3])
		else:
			dictionary[pronunciation] = []
			dictionary[pronunciation].append(word)
	return dictionary


dict_by_word = create_word_key_dict(open_dictionary())
dict_by_phoneme = create_phoneme2_key_dict(open_dictionary())

for i in dict_by_word:
	if len(dict_by_word[i]) > 1:
		print i
		print dict_by_word[i]
		
for i in dict_by_phoneme:
	if len(dict_by_phoneme[i]) > 1:
		print i
		print dict_by_phoneme[i]

# print dict_by_word
print "HELLO"
for i in dict_by_word["YOU'RE"]:
	print i
	print dict_by_phoneme[i]



