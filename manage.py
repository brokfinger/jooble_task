from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from api.routes import EndpointOne, EndpointTwo

app = Flask(__name__)
api = Api(app)

# connect database (if not file, will create in project folder)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jooble.db'
db = SQLAlchemy(app)

api.add_resource(EndpointOne, '/one')
api.add_resource(EndpointTwo, '/two')


@app.errorhandler(404)
def not_found(error):
    return "404 error", 404


@app.errorhandler(400)
def bad_request(error):
    return "400 error", 400


@app.errorhandler(500)
def internal_server_error(error):
    return "500 error", 500


if __name__ == "__main__":
    # debug on, to see was wrong this project
    app.run(debug=True)
