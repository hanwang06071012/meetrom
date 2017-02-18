from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "hello world"


@app.route('/liuyi')
def call_name():
	return ("hello ,li yi ,hello .....")

if __name__  == '__main__':
	app.run(host='0.0.0.0',port=8000)
