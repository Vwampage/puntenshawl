import json
from pprint import pprint
import xml.etree.ElementTree


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


#everyword = create_dict(open_dictionary())
#print everyword['POTATO']
# for key in everyword:
# 	print key
# 	print everyword[key] 


#lol reverse subject matter puns are hearing a sound in a word and usng that sound to find another word on the same subject and boom a pun.

#WTF KIND OF A DICTIONARY DOESN'T HAVE THE WORD POTATO???????
def open_json_dictionary():
	definitions = {}
	with open('dictionary/dictionary.json') as json_data:
		definitions = json.load(json_data)
		json_data.close()
	return definitions


def open_xml_dictionary():
	wiktionary = xml.etree.ElementTree.parse('/Volumes/Photodrive 6000/Wikipedia/wikidatawiki-20160501-pages-articles-multistream.xml').getroot()
	return wiktionary

#pprint(open_xml_dictionary())

#pprint(open_json_dictionary()["YIELD"])

