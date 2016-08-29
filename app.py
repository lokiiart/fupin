from flask import Flask
import requests

MyApp = Flask(__name__)

@MyApp.route("/")
def hello():
	r = requests.get("http://www.cpad.gov.cn")
	return r.text.encode('utf8')

if __name__ == "__main__":
	MyApp.run()
