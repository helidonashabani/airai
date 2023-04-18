from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


from api.airai import API_BLUEPRINT

# Register all the blueprints, url_prefix is optional
app.register_blueprint(API_BLUEPRINT, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
