from flask_restx import Resource

class HelloWorld(Resource):
    
    def get(self):
        return {"message": "Hello, World!"}