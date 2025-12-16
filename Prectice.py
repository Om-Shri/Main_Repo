import requests
from tqdm import tqdm

url = "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-713.exe"
r = requests.get(url,stream=True)
totalexpectedbytes = int(r.headers["Content-Length"])
bytesreceived = 0
progress_bar = tqdm(total = totalexpectedbytes,unit = "B",unit_scale=True)
with open("Winrar.exe","wb") as f:
    for  chunk in r.iter_content(chunk_size = 128):
        progress_bar.update(128)
        f.write(chunk)
        bytesreceived += 128
progress_bar.close()

