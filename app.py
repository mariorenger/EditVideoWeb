from flask import Flask, render_template, request
import os

app = Flask(__name__)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/static/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

if __name__ == "__main__":
    app.run(debug = True) 

