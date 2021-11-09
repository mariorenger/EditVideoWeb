from flask import Flask, render_template, request
import flask

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug = True) 

