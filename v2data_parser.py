import time

def open_dictionary():
	unparseddict = []
	with open('dictionary/cmudict.txt','r') as f:
		for line in f:
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
		if word[-1:] == ')':
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
			if word[-1:] == ')':
				dictionary[pronunciation].append(word[:-3])
			else:
				dictionary[pronunciation].append(word)
		elif word[-1:] == ')':
			dictionary[pronunciation] = []
			dictionary[pronunciation].append(word[:-3])
		else:
			dictionary[pronunciation] = []
			dictionary[pronunciation].append(word)
	return dictionary

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


def slide_together(input_word):
	matches = {}
	for phoneme_key in dict_by_phoneme:
		for pronunciation in dict_by_word[input_word]:
			word_length = 0
			compare_length = len(phoneme_key)
			input_length = len(pronunciation)
			if compare_length > input_length:
				word_length = compare_length
			else:
				word_length = input_length
			number_of_phonemes = word_length
			while number_of_phonemes >= 1:
				if phoneme_key[-number_of_phonemes:] == pronunciation[:number_of_phonemes]:
					for firstword in dict_by_phoneme[phoneme_key]:
						for secondword in dict_by_phoneme[pronunciation]:
							if (firstword, secondword) in matches:
								continue
							matches[(firstword, secondword)] = (firstword, secondword, number_of_phonemes, pronunciation[:number_of_phonemes])							
				number_of_phonemes += -1
			while number_of_phonemes >= 1:
				if pronunciation[-number_of_phonemes:] == phoneme_key[:number_of_phonemes]:
					for firstword in dict_by_phoneme[pronunciation]:
						for secondword in dict_by_phoneme[phoneme_key]:
							if (firstword, secondword) in matches:
								continue
							matches[(firstword, secondword)] = (firstword, secondword, number_of_phonemes, pronunciation[:number_of_phonemes])							
				number_of_phonemes += -1
	return matches

#You can't spell ___ without ____
#def cannot_spell_blank(input_word):
	
#String of words into a string of sounds



load_worddict_start = time.time()
dict_by_word = create_word_key_dict(open_dictionary())

word_dict_time = time.time() - load_worddict_start
phoneme_dict_start = time.time()

dict_by_phoneme = create_phoneme_key_dict(open_dictionary())

phoneme_dict_time = time.time() - phoneme_dict_start
blank_start = time.time()

blank_in_blank('HAIRY')

blank_end = time.time() - blank_start

slide_start = time.time()

matched_combination = slide_together('SCARY')
for i in matched_combination:
	print "%s + %s, matches on %s phonemes and those are %s" % matched_combination[i]


slide_end = time.time() - slide_start


print "word dictionary time: %s" % word_dict_time
print "phoneme dict time: %s" % phoneme_dict_time
print "blank in blank time: %s" % blank_end
print "slide together time: %s" % slide_end
# for i in dict_by_phoneme:
# 	print dict_by_phoneme[i]
# 	print i
# 	#last x items
# 	print i[-2:]
# 	#first x items
# 	print i[:2]



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

