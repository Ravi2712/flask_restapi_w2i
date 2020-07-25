from flask import Flask
from flask_cors import CORS
from flask_restful import reqparse, Api, Resource

from words_to_integer import wordsToInteger

class RestTest(Resource):

	def get(self):
		return {"msg": "Hello World!"}

class WordToInger(Resource):

	def get(self):

		parser = reqparse.RequestParser()
		parser.add_argument('word_text', location='form', required=True)
		args = parser.parse_args()
		user_requested_word = args['word_text']

		magical_number = wordsToInteger(user_requested_word)

		return {"status": "OK", "number": magical_number} # JSON response

##
## Flask app
##
app = Flask(__name__)
CORS(app)
api = Api(app)

##
## Actually setup the Api resource routing here
##
api.add_resource(RestTest, '/')
api.add_resource(WordToInger, '/word-to-integer')

if __name__ == '__main__':
	app.run(debug=True)