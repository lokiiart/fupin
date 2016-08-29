import requests

r = requests.get("http://www.cpad.gov.cn")

print r.text.encode('utf8')
