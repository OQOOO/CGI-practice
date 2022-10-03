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
  <form action="process_create.py">
    <p><input type="text" name="title"><br></p>
    <p><textarea rows="5" name="contents"></textarea></p>
    <p><button>submit</button></p>
  </from action>
</body>
</html>
''')