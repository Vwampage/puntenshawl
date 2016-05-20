import json
from pprint import pprint
import xml.etree.ElementTree


# class SemanticWord(object):
# 	def __init__(word, definition, defnition_graph, pronunciation)



def open_dictionary():
	unparseddict = open('dictionary/cmudict.txt','r')
	return unparseddict

def create_dict(dictionary):
	words = {}
	for row in dictionary:
		word_tho = row.strip().split(" ")
		words[word_tho[0]] = word_tho[2:]
	return words

everyword = create_dict(open_dictionary())
print everyword['POTATO']
# for key in everyword:
# 	print key
# 	print everyword[key] 


#WTF KIND OF A DICTIONARY DOESN'T HAVE THE WORD POTATO???????
def open_json_dictionary():
	definitions = {}
	with open('dictionary/dictionary.json') as json_data:
		definitions = json.load(json_data)
		json_data.close()
	return definitions


#pprint(open_json_dictionary()["YIELD"])

