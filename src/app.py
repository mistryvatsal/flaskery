from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'hello world'}

api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(debug=True)