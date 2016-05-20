import pronunciation_parser

all_words = pronunciation_parser.create_dict(pronunciation_parser.open_dictionary())

pun_on_this = "substantial".upper()
print all_words[pun_on_this]

def match_sounds(input_word,compare_word):
	sound_matches = 0
	for (sound1, sound2) in zip(all_words[pun_on_this], all_words[key]):
		if sound1 == sound2:
			sound_matches += 1
	#Making this >= and also multiplying the length by some factor like 0.6 works, but it's not scientifically rigorous enough for now.
	if sound_matches == len(all_words[pun_on_this]):
		return True
	else:
		return False

#def compare_length(input_word,compare_word):


for key in all_words:
	if len(all_words[key]) == len(all_words[pun_on_this]):
		if match_sounds(pun_on_this,key):
			print key
	#elif len

