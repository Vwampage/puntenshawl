def open_dictionary():
	unparseddict = open('dictionary/cmudict.txt','r')
	return unparseddict



def create_dict(dictionary):
	words = {}
	for row in dictionary:
		word_tho = row.strip().split(" ")
		words[word_tho[0]] = word_tho[2:]
	return words

# everyword = create_dict(open_dictionary())

# for key in everyword:
# 	print key
# 	print everyword[key] 

