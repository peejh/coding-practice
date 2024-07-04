# https://www.hackerrank.com/challenges/html-parser-part-2/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        category = "Multi" if len(data.split('\n')) > 1 else "Single"
        print(f">>> {category}-line Comment\n{data}")
    
    def handle_data(self, data):
        if data != '\n':
            print(f">>> Data\n{data}")
  
html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()