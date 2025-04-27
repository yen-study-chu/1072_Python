import requests

url = 'https://udn.com/news/index'
html = requests.get(url)
html.encoding="utf-8"
j = 0

htmllist = html.text.splitlines()

for row in htmllist:
    if "韓國瑜" in row: 
        j+=1
print("找到 "+ str(j) +" 次!")