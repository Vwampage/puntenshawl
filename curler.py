from requests import put, get
from argparse import ArgumentParser
import json

parser = ArgumentParser('Add arguments to find puns!')
parser.add_argument('-w', '--single_word', default='puppy', help='the word you would like puns on')
parser.add_argument('-s', '--subject', default='dog', help='the subject you would like to use')
args = parser.parse_args()

#puns = json.loads(get('http://localhost:5000/getapun/%s' % args.single_word).text)


def get_puns(word):
	return json.loads(get('http://localhost:5000/getapun/%s' % word).text)
