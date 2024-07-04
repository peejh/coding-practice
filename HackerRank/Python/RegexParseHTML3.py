from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('->', attr, '>', val) for attr, val in attrs]
               
    def handle_startendtag(self, tag, attrs):
        print(tag)
        [print('->', attr, '>', val) for attr, val in attrs]

parser = MyHTMLParser()
N = int(input())
src = '\n'.join([input() for _ in range(N)])
parser.feed(src)