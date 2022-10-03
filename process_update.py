#!C:/Python310/python.exe
import cgi
import os

form = cgi.FieldStorage()

pageId = form['pageId'].value
title = form['title'].value
contents = form['contents'].value

file = open('./pages/'+pageId, 'w')
file.write(contents)
file.close()
os.rename('pages/'+pageId, 'pages/'+title)

print(f"Location: index.py?id={title}")
print()