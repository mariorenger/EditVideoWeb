from sys import path
from flask import Flask, render_template, request
import os

from werkzeug.utils import send_from_directory
import handle_video
from video import *
import json 

app = Flask(__name__)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/static/uploads/'.format(PROJECT_HOME)
RESULT_FOLDER = '{}/static/result/'.format(PROJECT_HOME)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route('/get_time')
def get_time():
	divinfo = request.args.get('a', 0)
	# trong cái json thẻ div này nó có thuộc tính src
	# trong cái json thẻ div này nó có thuộc tính style:flex-grow hoặc flex-grow chính là tỉ lệ so với video gốc
	
	print(divinfo)
	return ("hello")

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
		
		rdata = json.loads(data)
		videopys = []

		for item in rdata: 
			st = int(item['startTime'])
			et = int(item['endTime'])
			path = item['pathVideo'].replace("http://127.0.0.1:5000/", "") # remove protocal and get relative path of video

			video = Video(st, et, path)
			videopy = video.finish_video()
			videopys.append(videopy)
		
		handle_video.mix(videopys, 'static/result/1.mp4')

	return "Success"

if __name__ == "__main__":
    app.run(debug = True) 

