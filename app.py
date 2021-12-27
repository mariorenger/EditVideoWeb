from flask import Flask, render_template, request
import json

from controllers.upload_controller import *
from controllers.done_video_controller import *

app = Flask(__name__)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/static/resources/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/upload", methods=["GET", "POST"])
def uploader():
	controller = UploadController(request.files['file'], app.config['UPLOAD_FOLDER'])

	if request.method == "POST" :
		controller.post()
	else: 
		controller.get()

	return "True"

@app.route("/done-video", methods=["POST"])
def done_video(): 
	cnt = request.form['count']
	data = request.form['data']
	volume = int(request.form['volume']) # volume of all sub video
	
	controller = DoneVideoController(json.loads(data), volume)

	if request.method == "POST" :
		controller.get()
	else : 
		controller.post()
		
	return "True"

if __name__ == "__main__":
    app.run(debug = True,host='0.0.0.0')
