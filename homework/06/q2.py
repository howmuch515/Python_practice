import urllib.request
import re

html = ""
with urllib.request.urlopen('https://docs.python.jp/3/library/re.html') as response:
   html = response.read().decode('utf-8')

pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
for link in set(re.findall(pattern, html)):
    print(link)
