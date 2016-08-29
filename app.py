from flask import Flask
import requests

MyApp = Flask(__name__)

@MyApp.route("/")
def hello():
	r = requests.get("http://www.cpad.gov.cn")
        r.encoding = r.apparent_encoding
        return r.text

if __name__ == "__main__":
	MyApp.run()
