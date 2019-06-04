from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/hi")
def index():

	params = request.args
	name = request.args.get("name")
	return render_template("index.html", name= name, age=1)

@app.route('/login', methods =['POST', 'GET'])
def login():
	if request.method == 'GET':
		return render_template("login.html")
	else:
		user, password = request.form.get("user"),request.form.get("pass")
		print(user,password)
		return "success"




if __name__ == "__main__":
	app.run(use_reloader = True)
