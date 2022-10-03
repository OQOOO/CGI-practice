#!C:/Python310/python.exe
import sys, codecs, cgi
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-type: text/html; charset=utf-8\r\n")

form = cgi.FieldStorage()
title = pageId = form["id"].value
contents = open('pages/'+pageId, 'r').read()

print(f'''
  <form action="process_update.py" method="post">
    <input type="hidden" name="pageId" value="{pageId}">
    <p><input type="text" name="title" value="{title}"></p>
    <p><textarea rows="5" name="contents">{contents}</textarea></p>
    <p><button>submit</button></p>
  </from>''')