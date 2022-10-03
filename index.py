#!C:/Python310/python.exe
import sys
import codecs
import cgi, os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-type: text/html; charset=utf-8\r\n")

# html 세탁
import html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

# 파일 링크 생성
files = os.listdir('./pages')
linkList = ''
for file in files:
  linkList += f'<li><a href="index.py?id={file}">{file}</a></li>'



form = cgi.FieldStorage()
if 'id' in form:
  title = pageId = form['id'].value
  contents = open('pages/'+pageId, 'r').read()
  update = f'<a href="update.py?id={pageId}">update</a>'
  delete =f''' 
  <form action="process_delete.py" method="post">
    <input type="hidden" name="pageId" value="{pageId}">
    <input type="submit" value="delete">
  </form>'''
else:
  title = 'indexPage'
  contents = 'welcome'
  update = ''
  delete = ''


print(f'''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1> 
  <ol>
   {linkList}
  </ol>
  <a href="create.py">create</a>
  {update}
  {delete}
  <h2>{title}</h2>

  <p>{contents}</p>
</body>
</html>
''')