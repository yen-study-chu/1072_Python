import requests,re
regex = re.compile('http://[a-zA-Z./_]+')
url = 'http://www1.chu.edu.tw/p/412-1000-495.php?Lang=zh-tw'
html = requests.get(url)
a = regex.findall(html.text)
for i in a:
    print(i)
    
print(a)