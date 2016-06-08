from nltk.corpus import wordnet as wn

for synset in wn.synsets('dog'):
	print synset
	if 'dog' in str(synset):
		print synset.definition()


dog = wn.synset('dog.n.01')

print dog.hypernyms()

print wn('dog')