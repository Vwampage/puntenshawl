import pronunciation_parser

all_words = pronunciation_parser.create_dict(pronunciation_parser.open_dictionary())

pun_on_this = "capable".upper()
print all_words[pun_on_this]

def match_sounds(input_word,compare_word):
	if len(all_words[input_word]) == len(all_words[compare_word]):
		sound_matches = 0
		for (sound1, sound2) in zip(all_words[input_word], all_words[compare_word]):
			if sound1 == sound2:
				sound_matches += 1
		#Making this >= and also multiplying the length by some factor like 0.6 works, but it's not scientifically rigorous enough for now.
		if sound_matches == len(all_words[pun_on_this]):
			return True
		else:
			return False
	else:
		return False

#This evaluates if all the sounds are present, aka for 'you're' it can make things of the form "You put the you're in mercurial"
def different_lengths(input_word,compare_word):
	matching_sounds = 0
	for sound in all_words[input_word]: 
		if sound in all_words[compare_word]:
			matching_sounds += 1
	if matching_sounds == len(all_words[input_word]):
		print len(all_words[input_word])
		print matching_sounds
		return True
	else:
		return False

def sublistExists(longerList, shorterList):
    return ''.join(map(str, shorterList)) in ''.join(map(str, longerList))


# def partial_sequence_comparison(input_word,compare_word):
#		Make tuples/ a dict for every sound in the pun-on-this word?
#		for every sound in the pun-on-this word
# 	If the compare-word contains a sound from pun-on-this figure out where that sound exists in the word
#		figure out how many more sounds are after the sound that matches
#		Figure out how much of that sequence matches
#		Add to the relevant dict for whatever matches?
#		
		
#Phoneme analog to levenstein distance
# try turning a sentence into a list of sounds and finding combinations of words that are *close* to those sounds
#THAT would be super interesting

#def compare_length(input_word,compare_word):

# for key in all_words:
# 	if match_sounds(pun_on_this,key):
# 		print key
# 	#print "More than 1/2 matching sounds in word:"
# 	if different_lengths(pun_on_this,key):
# 		print key

for key in all_words:
	for key2 in all_words:
		if len(all_words[key]) <= len(all_words[key2]):
			if sublistExists(all_words[key2],all_words[key]):
				print "You put the %s in %s!" % (key, key2)
			elif sublistExists(all_words[key],all_words[key2]):
				print "You put the %s in %s!" % (key2, key)


