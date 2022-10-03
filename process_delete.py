#!C:/Python310/python.exe
import cgi, os

form = cgi.FieldStorage()
pageId = form['pageId'].value

os.remove('pages/'+pageId)
print('Location: index.py?')
print()