import requests

headers = {'content-type': 'application/html'}
r = requests.get("http://www.cpad.gov.cn")
r.encoding = r.apparent_encoding

print r.text.encode('utf8')
