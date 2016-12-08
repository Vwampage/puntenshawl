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

def create_phoneme_key_dict(raw_dictionary):
	dictionary = {}
	for i in raw_dictionary:
		word_as_list = i.strip().split(' ')
		word = word_as_list[0]
		pronunciation = tuple(word_as_list[2:])
		if pronunciation in dictionary:
			if word[-1:] is ')':
				dictionary[pronunciation].append(word[:-3])
			else:
				dictionary[pronunciation].append(word)
		elif word[-1:] is ')':
			dictionary[pronunciation] = []
			dictionary[pronunciation].append(word[:-3])
		else:
			dictionary[pronunciation] = []
			dictionary[pronunciation].append(word)
	return dictionary


dict_by_word = create_word_key_dict(open_dictionary())
dict_by_phoneme = create_phoneme_key_dict(open_dictionary())


def compare_two_words_sounds(word1sounds, word2sounds):
	sounds1 = ' '.join(word1sounds)
	sounds2 = ' '.join(word2sounds)
	if sounds1 in sounds2:
		return (True, word1sounds, word2sounds)
	elif sounds2 in sounds1:
		return (True, word2sounds, word1sounds)
	return (False, (), ())

def blank_in_blank(input_word):
	#every pronunciation
	for phoneme_key in dict_by_phoneme:
		for pronunciation in dict_by_word[input_word]:
			result = compare_two_words_sounds(pronunciation, phoneme_key)
			if result[0]:
				print "Sound1: %s. Words: %s." % (result[1], dict_by_phoneme[result[1]])
				print "Sound2: %s. Words: %s." % (result[2], dict_by_phoneme[result[2]])
				for sound1word in dict_by_phoneme[result[1]]:
					for sound2word in dict_by_phoneme[result[2]]:
						print "You put the %s in %s!" % (sound1word, sound2word)



blank_in_blank('HAIRY')
print dict_by_word['HARRY']
print dict_by_word['HAIRY']
print dict_by_phoneme[('HH', 'EH1', 'R', 'IY0')]

# letters = ''

# for i in dict_by_word['SUBMARINE']:
# 	print i
# 	letters.join(map(str, list(i)))

# print letters 
# print '#######'

# hi = "potato"

# hi.join("cococo")

# print hi

# blank_in_blank('SUBMARINE')
# print dict_by_word['MARINE']
# print ''.join(map(str, dict_by_word['MARINE'][0]))
# print dict_by_word['SUBMARINE']
# print ''.join(map(str, dict_by_word['SUBMARINE'][1]))
# for i in dict_by_word:
# 	if len(dict_by_word[i]) > 1:
# 		print i
# 		print dict_by_word[i]
		
# for i in dict_by_phoneme:
# 	if len(dict_by_phoneme[i]) > 1:
# 		print i
# 		print dict_by_phoneme[i]

# print dict_by_word
# print "HELLO"
# for i in dict_by_word["YOU'RE"]:
# 	print i
# 	print dict_by_phoneme[i]

