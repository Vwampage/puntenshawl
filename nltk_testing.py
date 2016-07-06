import sys
from nltk.corpus import wordnet as wn

all_words = []
with open('/usr/share/dict/words') as words:
	for line in words.readlines():
		all_words.append(line)

#print all_words

for word in all_words:
	print word
	for synset in wn.synsets(word.lower()):
		#print synset
		if word.lower() in str(synset):
			print synset.definition()


# dog = wn.synset('dog.n.01')

# print dog.hypernyms()

# print wn('dog')