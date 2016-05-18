unparseddict = open('dictionary/cmudict.txt','r')

words = {}
for row in unparseddict:
	word_tho = row.strip().split(" ")
	words[word_tho[0]] = word_tho[2:]

for key in words:
	print key
	print words[key] 
