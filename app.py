from flask import render_template, Flask, current_app
from flask_cors import CORS

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)

@app.route("/")
def index():
	return current_app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()
