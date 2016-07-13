import sys
from nltk.corpus import wordnet as wn
from argparse import ArgumentParser


parser = ArgumentParser('Add words to compare')
parser.add_argument('-a', '--first-word', default='puppy', help='The base comparison word')
parser.add_argument('-b', '--second-word', default='dog', help='The base comparison word')
args = parser.parse_args()


print args.first_word
print args.second_word


synsetsOne = []
synsetsTwo = []

for synset in wn.synsets(args.first_word):
	if args.first_word in str(synset):
		synsetsOne.append(synset)

for synset in wn.synsets(args.second_word):
	if args.second_word in str(synset):
		synsetsTwo.append(synset)


for wordOne in synsetsOne:
	for wordTwo in synsetsTwo:
		print wordOne, wordTwo
		print wordOne.definition()
		print wordTwo.definition()
		print wordOne.hypernyms(), wordTwo.hypernyms()
		print wordOne.path_similarity(wordTwo)		
		print
		print
# print wn.synsets('puppy')
# print wn.synsets('dog')

# print wn.path_similarity(args.first_word, args.second_word)
# print args.first_word.path_similarity(args.second_word)

all_words = []
with open('/usr/share/dict/words') as words:
	for line in words.readlines():
		all_words.append(line)



sample_text = """
I went to the mall today and I got to ride a pony. Riding the pony was super fun and we ran around the enclosure very quickly. Nobody messed with us because nobody messes with a pony.
"""



print sample_text.decode('UTF-8')
#print all_words

# for word in all_words:
# 	strip_word = word.strip()
# 	print strip_word
# 	for synset in wn.synsets(strip_word):
# 		if strip_word in str(synset):
# 			print synset.definition()


# for synset in wn.synsets('greeting'):	
# 	if 'greeting' in str(synset):
# 		print 'greeting'
# 		print type('greeting')
# 		print synset.definition()

# dog = wn.synset('dog.n.01')

# print dog.hypernyms()

# print wn('dog')