from flask import Flask
from config import config
from flask_cors import CORS

#Routes
from  routes import Movie

app = Flask(__name__)
CORS(app, resources={"*": {"origins": "http://localhost:3000"}}) #Aqui le indico la dir host y puerto de la aplicaciones a acceder a esta api

def page_not_found(error):
    return "<h1>Page not found</h1>",404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Movie.main, url_prefix='/api/movies')

    # Error Handlers
    app.register_error_handler(404, page_not_found)
    app.run(port=5000)
