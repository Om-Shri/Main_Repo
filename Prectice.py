import requests

url = " "
r = requests.get("URL")

fp = open("file.exe","wb")
fp.write(r.content)
fp.close()