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
			if similarity > 0.125:
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
Now the country is left to consider what the lasting consequences of the uprising will be. While Mr. Erdogan has fended off a coup, the most urgent question is this: Has he emerged even more powerful, or is he now a weakened leader who must accommodate his opponents? I went to the mall today and I got to ride a pony. Riding the pony was super fun and we ran around the enclosure very quickly. Nobody messed with us because nobody messes with a pony. From there I worked on the scoring sheet for Signal Hunt. My goal was to make something that would automatically score all of the bonuses, from have they scored one clue in every category, to if they've scored more than half of a whole category or a region there's some bonus in it for them. It was a lot of fun figuring out how to do conditional logic in a Google Sheet. I've actually never done that before so it was interesting to learn the syntax.
"""
#########################

#print sample_text.split(' ')
# text_list = sample_text.split(' ')

# synonyms = {}

# for index, i in enumerate(text_list):
# 	print index, i
# 	try:
# 		synonyms[(index, i.strip())] = thesaurus[i.strip()]
# 	except:
# 		synonyms[(index, i)] = [i]
# 		print "Key error %s" % i

# print synonyms
# # print subject_comparison('alcohol','cup')

# for i in sample_text.split(' '):
# 	subject_comparison(i, args.subject)

# for key in synonyms:
# 	for i in synonyms[key]:
# 		subject_comparison(i, args.subject)
###############################


# for i in wn.synsets(args.subject):
# 	while len(i.hyponyms()) > 0:
# 		print i.hyponyms()
# 		i

hyponyms = wn.synsets(args.subject)
print hyponyms
for i in hyponyms:
	print i.hyponyms
	if i not in hyponyms:
		hyponyms.append(i)
	for j in i.hyponyms():
		if j not in hyponyms:
			hyponyms.append(j)
print hyponyms

for i in sample_text.split():
	print i
	for j in wn.synsets(i):
		if j in hyponyms:
			print "%s can be substituted for %s!" % (j, i)

# current_level = wn.synsets(args.subject)

# for i in current_level:
# 	print i.hypernyms()
# 	for j in i.hypernyms():
# 		print j.hyponyms()
	

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