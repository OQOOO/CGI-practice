#!C:/Python310/python.exe
import cgi

form = cgi.FieldStorage()
title = form['title'].value
contents = form['contents'].value

file = open('./pages/'+title, 'w')
file.write(contents)
file.close()

print(f"Location: index.py?id={title}")
print()