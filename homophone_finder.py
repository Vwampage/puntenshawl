import pronunciation_parser

all_words = pronunciation_parser.create_dict(pronunciation_parser.open_dictionary())

pun_on_this = "urine".upper()
print all_words[pun_on_this]

for key in all_words:
	if len(all_words[key]) == len(all_words[pun_on_this]):
		sound_matches = 0
		for (sound1, sound2) in zip(all_words[pun_on_this], all_words[key]):
			if sound1 == sound2:
				sound_matches += 1
		if sound_matches >= len(all_words[pun_on_this])*0.6:
			print key
