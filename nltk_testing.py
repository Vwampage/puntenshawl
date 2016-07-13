import sys
import data_parser
from nltk.corpus import wordnet as wn
from argparse import ArgumentParser


parser = ArgumentParser('Add words to compare')
parser.add_argument('-a', '--first-word', default='puppy', help='The base comparison word')
parser.add_argument('-b', '--second-word', default='dog', help='The base comparison word')
parser.add_argument('-s', '--subject', default='alcohol', help='Subject to make puns on.')
args = parser.parse_args()

thesaurus = data_parser.create_thesaurus(data_parser.open_thesaurus())
#print thesaurus
print args.first_word
print args.second_word

def subject_comparison(word,subject):
	synsetsSubject = []
	synsetsWord = []

	for synset in wn.synsets(subject):
		if subject in str(synset):
			synsetsSubject.append(synset)

	for synset in wn.synsets(word):
		if word in str(synset):
			synsetsWord.append(synset)

	for definitionSubject in synsetsSubject:
		for definitionWord in synsetsWord:
			similarity = definitionSubject.path_similarity(definitionWord)
			if similarity > 0.3:
				print word, subject
				# print definitionSubject.definition()
				# print definitionWord.definition()
				# print definitionSubject.hypernyms(), definitionWord.hypernyms()
				print similarity
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


print sample_text.split(' ')
text_list = sample_text.split(' ')

synonyms = {}

for index, i in enumerate(text_list):
	print index, i
	try:
		synonyms[(index, i.strip())] = thesaurus[i.strip()]
	except:
		synonyms[(index, i)] = [i]
		print "Key error %s" % i

print synonyms
# print subject_comparison('alcohol','cup')

for i in sample_text.split(' '):
	subject_comparison(i, args.subject)

for key in synonyms:
	for i in synonyms[key]:
		subject_comparison(i, args.subject)
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