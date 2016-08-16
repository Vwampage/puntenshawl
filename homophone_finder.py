import data_parser
from argparse import ArgumentParser
from pprint import pprint
from nltk.corpus import wordnet as wn

all_words = data_parser.create_dict(data_parser.open_dictionary())
thesaurus = data_parser.create_thesaurus(data_parser.open_thesaurus())
#wordnet = 

parser = ArgumentParser('Add arguments to find puns!')
parser.add_argument('-w', '--single-word', default='puppy', help='the word you would like puns on')
parser.add_argument('-s', '--subject', default='dog', help='the subject you would like to use')
args = parser.parse_args()

pun_on_this = args.single_word.upper()
print all_words[pun_on_this]

#takes in a word or sequence of words and returns a list of sequences of sounds
#maybe this should be a dictionary of words with a position indicator?
#also should deal with apostrophes
#should deal with alternate pronunciations
def parse_sounds(string_of_words):
	words_to_process = string_of_words.upper().strip().split(' ')
	dict_of_words = {}
	for i in words_to_process:
		if i in all_words.keys():
			dict_of_words[i] = [].append(all_words[i])
			if i + '(1)' in all_words.keys():
				dict_of_words[i] = [].append(all_words[i + '(1)'])
				if i + '(2)' in all_words.keys():
					dict_of_words[i] = [].append(all_words[i + '(2)'])
					if i + '(3)' in all_words.keys():
						dict_of_words[i] = [].append(all_words[i + '(3)'])





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
#Actually this one is pretty mediocre. I don't think it's really a good plan to keep using it for now.
def different_lengths(input_word,compare_word):
	matching_sounds = 0
	for sound in all_words[input_word]: 
		if sound in all_words[compare_word]:
			matching_sounds += 1
	if matching_sounds == len(all_words[input_word]):
		#print len(all_words[input_word])
		#print matching_sounds
		return True
	else:
		return False

def whichIsShorterLetters(word1,word2):
	if len(word1) < len(word2):
		return (word1, word2, len(word2)-len(word1))
	else:
		return (word2, word1, len(word1)-len(word2))

def whichIsShorterSounds(word1,word2):
	if len(all_words[word1]) < len(all_words[word2]):
			return (word1, word2, len(all_words[word2])-len(all_words[word1]))
	else:
		return (word2, word1, len(all_words[word1])-len(all_words[word2]))	

def isShortInLongLetters(shorterWord,longerWord):
	return shorterWord in longerWord

def isShortInLongSounds(shorterList,longerList):
	return ''.join(map(str, shorterList)) in ''.join(map(str, longerList))


def isWordInOtherWords(input_word,compare_word):
	sounds = whichIsShorterSounds(input_word, compare_word)
	letters = whichIsShorterLetters(input_word,compare_word)
	if isShortInLongSounds(all_words[sounds[0]], all_words[sounds[1]]) and not isShortInLongLetters(sounds[0], sounds[1]):
		return sounds
	elif isShortInLongLetters(letters[0], letters[1]) and not isShortInLongSounds(all_words[letters[0]], all_words[letters[1]]):
		return letters
	return False

def chop_up_sound_sequences(input_word):
	beginning_sounds = []
	ending_sounds = []
	word_sounds = all_words[input_word]
	for i in xrange(1,len(word_sounds)+1):
		beginning_sounds.append(word_sounds[:i])
		ending_sounds.append(word_sounds[-i:])
	return (beginning_sounds, ending_sounds)

#Another form of this: if most of one of the words exists within another word
#then definitely print a match. "C OO" in uncouth or whatnot.
#This would be very good for punning opportunities with just 
# a little bit of "these are similar enough" logic



def doBeginningEndingSoundsMatch(input_word, compare_word):
	matches = []
	# matches['beginnings'] = []
	# matches['endings'] = []
	sound_sorted = whichIsShorterSounds(input_word,compare_word)
	#comparison_sounds = chop_up_sound_sequences(sound_sorted[0])
	shorter_word = sound_sorted[0]
	longer_word = sound_sorted[1]
	max_length = len(all_words[shorter_word])
	for i in xrange(1,len(all_words[shorter_word])+1):
		shorter_word_sounds = {'beginning_sounds': all_words[shorter_word][:i], 'ending_sounds': all_words[shorter_word][-i:]}
		# shorter_word_sounds['beginning_sounds'] = all_words[shorter_word][:i]
		# shorter_word_sounds['ending_sounds'] = all_words[shorter_word][-i:]
		longer_word_sounds = {'beginning_sounds': all_words[longer_word][:i], 'ending_sounds': all_words[longer_word][-i:]}
		# longer_word_sounds['beginning_sounds'] = all_words[longer_word][:i]
		# longer_word_sounds['ending_sounds'] = all_words[longer_word][-i:]
		long_plus_short_str = longer_word + ' + ' + shorter_word
		short_plus_long_str = shorter_word + ' + ' + longer_word
		if i > len(all_words[shorter_word]) * 0.34:
			if (long_plus_short_str, shorter_word_sounds['beginning_sounds']) not in matches:
				if isShortInLongSounds(shorter_word_sounds['beginning_sounds'],longer_word_sounds['ending_sounds']):
					matches.append((long_plus_short_str, shorter_word_sounds['beginning_sounds'], i, len(all_words[shorter_word])))
					# and i > len(all_words[shorter_word])*0.25
			if (short_plus_long_str, shorter_word_sounds['beginning_sounds']) not in matches:
				if isShortInLongSounds(shorter_word_sounds['ending_sounds'],longer_word_sounds['beginning_sounds']):
					matches.append((short_plus_long_str, shorter_word_sounds['ending_sounds'], i, len(all_words[shorter_word])))
	return matches

def findASubject(subject):
	hyponyms = wn.synsets(args.subject)
	# print hyponyms
	for i in hyponyms:
		# print i.hyponyms
		if i not in hyponyms:
			hyponyms.append(i)
		for j in i.hyponyms():
			if j not in hyponyms:
				hyponyms.append(j)
	return hyponyms

def synsetToWord(synset):
	return str(synset).split("'")[1].split('.')[0].replace('_',' ').upper()

#Split a word into every possible sequence of sounds
#Compare every sound sequence to every sound sequence in other words
#Compare words that have various amounts of combinations and various amounts of matching
#??????
#profit

# This needs to be able to deal with multiple words
def additiveFromSubject(subject,word):
	subject_words = findASubject(subject)
	matches = []
	for i in subject_words:
		#This deals with multiple words for now.
		if synsetToWord(i) in all_words.keys():
			#need a length thing in beginning and ending sounds matching	
			for i in doBeginningEndingSoundsMatch(pun_on_this,key):
				if len(i) > 0:
					matches.append(doBeginningEndingSoundsMatch(word,synsetToWord(i)))
	return matches
#Phoneme analog to levenstein distance
# try turning a sentence into a list of sounds and finding combinations of words that are *close* to those sounds
#THAT would be super interesting

#def compare_length(input_word,compare_word):
word_puns = {}
word_puns['homophones'] = []
word_puns['blank_in_blank'] = []
word_puns['additive_words'] = []
word_puns['additive_subject'] = []
homophones = []
# contains_component_sounds = []
blank_in_blank_puns = []
additive_words = []
additive_subject = []

for key in all_words:
	if match_sounds(pun_on_this,key):
		homophones.append(key)
		word_puns['homophones'].append(key)
	#print "More than 1/2 matching sounds in word:"
	# if different_lengths(pun_on_this,key):
	# 	contains_component_sounds.append(key)
	blankInBlank = isWordInOtherWords(pun_on_this,key)
	if blankInBlank:
		blank_in_blank_puns.append(blankInBlank)
		word_puns['blank_in_blank'].append(blankInBlank)
	for i in doBeginningEndingSoundsMatch(pun_on_this,key):
		if len(i) > 0:
			additive_words.append(i)
			word_puns['additive_words'].append(i)

additive_subject = additiveFromSubject(args.subject.upper(),pun_on_this)
word_puns['additive_subject'] = additive_subject

print "Pure Homophones of %s:"
for i in homophones:
	print i.lower()
# print "These words contain all the component sounds:"
# for i in contains_component_sounds:
# 	print i.lower()
print "Here are some puns of the form 'You put the ___ in ___!'"
for i in blank_in_blank_puns:
	print "You put the %s in %s!" % (i[0].lower(), i[1].lower())
for i in additive_words:
	print i

print word_puns



	# print i['beginnings']
	# print i['endings']
#print thesaurus[pun_on_this.lower()]
# print data_parser.return_wordnet_definitions(pun_on_this.lower())

# print chop_up_sound_sequences(pun_on_this)
# print all_words['LEMMIE']
# print all_words['WRINKLE']
# print doBeginningEndingSoundsMatch('LEMMIE', 'CANDLE')

# print additiveFromSubject(pun_on_this, args.subject.upper())

#OK So here is the subject section
#Lets try looking at a sentence and finding the
#most common subject already in it!
#That could be pretty cool.

# for i in findASubject(args.subject):
# 	print synsetToWord(i)

# for key in all_words:
# 	for i in doBeginningEndingSoundsMatch(pun_on_this,key):
# 		if len(i) > 0:
# 			print i

#pprint(thesaurus)


#Here you should also take into account letter sequence. If letter sequence matches AND sound DOES NOT match, then put it in. Could be funnier
#also maybe make a dictionary with tuples as the key to actually comb through because speed.

### THIS SECTION WOULD RENDER A FULL SET OF ___ IN ___ PUNS.
# blankInBlank = []
# for key in all_words:
# 	for key2 in all_words:
# 		if len(all_words[key]) < len(all_words[key2]):
# 			if key in key2:
# 				if not sublistExists(all_words[key2],all_words[key]):
# 					print "You put the %s in %s!" % (key, key2)
# 					if (key,key2) not in blankInBlank:
# 						blankInBlank.append((key,key2))
# 			if sublistExists(all_words[key2],all_words[key]):
# 				if key not in key2:
# 					print "You put the %s in %s!" % (key, key2)
# 					if (key,key2) not in blankInBlank:
# 						blankInBlank.append((key,key2))

