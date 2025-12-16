import requests
from PIL import Image
from io import BytesIO


r = requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1txXfWlVt3L51daXBkH4smrrFTEu0ocAzfQ&s")

i = Image.open(BytesIO(r.content))
fp = open("image.jpg","wb")
i.save(fp)
fp.close()