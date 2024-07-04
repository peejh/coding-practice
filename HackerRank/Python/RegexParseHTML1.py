# https://www.hackerrank.com/challenges/html-parser-part-1/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        [print('->', attr, '>', val) for attr, val in attrs]
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        [print('->', attr, '>', val) for attr, val in attrs]

parser = MyHTMLParser()
src = ''
for _ in range(int(input())):
    src += input()
parser.feed(src)