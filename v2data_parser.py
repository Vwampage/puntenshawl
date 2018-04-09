import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--word", help = "This is the word to generate sound relationships for.", type = str, default = "hello")

args = parser.parse_args()

PUN_WORD = args.word.upper()

#This method pulls the CMU Pronouncing Dictionary in and sends it off to be parsed. 
def open_dictionary():
	unparseddict = []
	with open('dictionary/cmudict.txt','r') as f:
		for line in f:
			#This filters out the comments which all start with that sequence)
			if line.startswith(';;;'):
				continue
			unparseddict.append(line)
	return unparseddict

#This creates a dict object with the english word as the key
#and all pronunciations as a tuple for that key.
def create_word_key_dict(raw_dictionary):
	dictionary = {}
	for i in raw_dictionary:
		word_as_list = i.strip().split(' ')
		word = word_as_list[0]
		pronunciation = tuple(word_as_list[2:])
		#This removes the (1), (2), or (3) that exist for words for which there are
		#alternate pronunciations such as 'transport' which has one pronunciation with
		#AO1 and another with AO0.
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

#This creates a dict object with the pronunciation as a key
#and all words that have that pronunciation as a tuple for that key.
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

#This takes two words' sounds, concatenates the list of sounds into one string,
#and figures out if the sounds from one word exist in enother word.
#It returns immediately upon finding a match because while Paul may
#exist in metropolitan metropolitan will not exist in Paul.
def compare_two_words_sounds(word1sounds, word2sounds):
	sounds1 = ' '.join(word1sounds)
	sounds2 = ' '.join(word2sounds)
	if sounds1 in sounds2:
		return (True, word1sounds, word2sounds)
	elif sounds2 in sounds1:
		return (True, word2sounds, word1sounds)
	return (False, (), ())

#If a word's sounds exist in another word it works well for this
#joke construction.
def blank_in_blank(input_word):
	#The nested loops are to deal with every pronunciation.
	for phoneme_key in dict_by_phoneme:
		for pronunciation in dict_by_word[input_word]:
			result = compare_two_words_sounds(pronunciation, phoneme_key)
			if result[0]:
				print "Sound1: %s. Words: %s." % (result[1], dict_by_phoneme[result[1]])
				print "Sound2: %s. Words: %s." % (result[2], dict_by_phoneme[result[2]])
				for sound1word in dict_by_phoneme[result[1]]:
					for sound2word in dict_by_phoneme[result[2]]:
						print "You put the %s in %s!" % (sound1word, sound2word)


#This is the more computationally expensive comparison. It checks if words
#have similar beginning and ending sounds such that they could be pronounced one
#going right into the other. For instance, 'jock' and 'occupancy' overlap in the
#"ock" sound they share, which is represented in the CMU Pronouncing Dictionary as 'AA1', 'K'.
def slide_together(input_word):
	matches = {}
	for phoneme_key in dict_by_phoneme:
		for pronunciation in dict_by_word[input_word]:
			word_length = 0
			compare_length = len(phoneme_key)
			input_length = len(pronunciation)
			#This comparison is so that the script only iterates for the length of the shorter of the words
			#rather than looking for a long word within a short word.
			if compare_length > input_length:
				word_length = compare_length
			else:
				word_length = input_length
			number_of_phonemes = word_length
			#The whole shenaniganry below is because while comparing the *sounds* is pretty easy, there are
			#potentially a lot of words that have those sounds. So this has to go through all the word combinations.
			#I know, I also don't like the nested for loops. That should probably abstract that into a separate
			#method at some point.
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

if __name__ == "__main__":
	#The timers are to measure performance for the time being.
	load_worddict_start = time.time()
	dict_by_word = create_word_key_dict(open_dictionary())

	word_dict_time = time.time() - load_worddict_start
	phoneme_dict_start = time.time()

	dict_by_phoneme = create_phoneme_key_dict(open_dictionary())
	if PUN_WORD in dict_by_word:
		phoneme_dict_time = time.time() - phoneme_dict_start
		blank_start = time.time()

		blank_in_blank(PUN_WORD)

		blank_end = time.time() - blank_start

		slide_start = time.time()

		matched_combination = slide_together(PUN_WORD)
		for i in matched_combination:
			print "%s + %s, matches on %s phonemes and those are %s" % matched_combination[i]

		slide_end = time.time() - slide_start

		print "word dictionary time: %s" % word_dict_time
		print "phoneme dict time: %s" % phoneme_dict_time
		print "blank in blank time: %s" % blank_end
		print "slide together time: %s" % slide_end
	else:
		print "Apologies, Puntenshawl does not know how to pronounce %s." % PUN_WORD

