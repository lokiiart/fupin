from flask import Flask

MyApp = Flask(__name__)

@MyApp.route("/")
def hello():
	return "test"

if __name__ == "__main__":
	MyApp.run()
