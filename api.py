from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import homophone_finder
import data_parser

all_words = data_parser.create_dict(data_parser.open_dictionary())

app = Flask(__name__)
api = Api(app)


def abort_if_word_doesnt_exist(potential_word):
  if potential_word.upper() not in all_words.keys():
    abort(404, message="%s is not a known word" % potential_word)

parser = reqparse.RequestParser()
parser.add_argument('word', type=str, help= 'A word on which you would like puns.')
parser.add_argument('subject', type=str, help= 'A subject on which you would like puns.')

class Puns(Resource):
  def get(self, word, subject):
    abort_if_word_doesnt_exist(args['word'])
    abort_if_word_doesnt_exist(args['subject'])
    return homophone_finder.get_puns(args['word'], args['subject'])

api.add_resource(Puns, '/getapun')

if __name__ == '__main__':
    app.run(debug=True)
