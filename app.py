from sys import path
from flask import Flask, render_template, request
import os

from werkzeug.utils import send_from_directory
import handle_video
from video import *
import json 

app = Flask(__name__)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/static/resources/uploads/'.format(PROJECT_HOME)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")
    
# create folder upload if not exists
def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath

@app.route("/upload", methods=["POST"])
def uploader():
	if request.method == "POST" :
		file = request.files["file"]
		
		create_new_folder(app.config['UPLOAD_FOLDER'])
		saved_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
		file.save(saved_path)

	return "Success"

@app.route("/done-video", methods=["POST"])
def done_video(): 
	if request.method == "POST" :
		cnt = request.form['count']
		data = request.form['data']
		volume = int(request.form['volume']) # volume of all sub video

		rdata = json.loads(data)
		videopys = []

		for item in rdata: 
			st = float(item['startTime'])
			et = float(item['endTime'])
			path = item['pathVideo'].replace("http://127.0.0.1:5000/", "") # remove protocal and get relative path of video

			video = Video(st, et, path, volume)
			videopy = video.finish_video()
			videopys.append(videopy)
		
		handle_video.mix(videopys, 'static/resources/result/1.mp4')

	return "Success"	

if __name__ == "__main__":
    app.run(debug = True) 

