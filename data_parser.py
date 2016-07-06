import json
from pprint import pprint
from nltk.corpus import wordnet as wn


# class SemanticWord(object):
# 	def __init__(word, definition, defnition_graph, pronunciation)

#for i in $(cat /usr/share/dict/words); do python osx_dictionary_caller.py ${i}; done

def open_dictionary():
	unparseddict = []
	with open('dictionary/cmudict.txt','r') as f:
		for line in f.readlines():
			unparseddict.append(line)
	return unparseddict

def create_dict(dictionary):
	words = {}
	for row in dictionary:
		word_tho = row.strip().split(" ")
		if word_tho[0] != ';;;':
			words[word_tho[0]] = word_tho[2:]
	return words

def open_thesaurus():
	list_of_words = []
	with open('../resources_for_puntenshawl/MyThes-1.0/th_en_US_new.dat') as f:
		for line in f.readlines():
			list_of_words.append(line)
	return list_of_words

	#raw_thesaurus = open('../resources_for_puntenshawl/MyThes-1.0/th_en_US_new.dat')
	#return raw_thesaurus

def create_thesaurus(thesaurus):
	big_thesaurus = {}
	current_word = ''
	for row in thesaurus:
		#import pdb; pdb.set_trace()
		row_parts = row.strip().split('|')
		if row_parts[0][0] != '(':
			current_word = row_parts[0]
			big_thesaurus[current_word] = []
		else:
			big_thesaurus[current_word] = row_parts[1:]	
	return big_thesaurus

def open_osx_dictionary():
	everyword = []
	current_word = ''
	quotechar = "'"
	with open('../resources_for_puntenshawl/osxdictv2output.txt') as f:
		for line in f.readlines():
			if line[0] not in quotechar:
				pass
			if line[0].isalpha():
				lineparts = line.strip().split('|')
				print lineparts
	return everyword

def return_wordnet_definitions(word):
	definitions = []
	for synset in wn.synsets(word):
		if word in str(synset):
			#print synset.definition()
			definitions.append(synset.definition())
	return definitions

#print open_osx_dictionary()
#everyword = create_dict(open_dictionary())
#print everyword['POTATO']
# for key in everyword:
# 	print key
# 	print everyword[key] 


#lol reverse subject matter puns are hearing a sound in a word and usng that sound to find another word on the same subject and boom a pun.



#pprint(open_xml_dictionary())

#pprint(open_json_dictionary()["YIELD"])



#for every word in dictionary
#if it's in the Big Word List



