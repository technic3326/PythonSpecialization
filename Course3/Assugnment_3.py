import urllib
from bs4 import BeautifulSoup

html_response = urllib.urlopen("http://python-data.dr-chuck.net/comments_245831.html").read()
soup = BeautifulSoup(html_response)

tags = soup('span')

num_list = list()
for tag in tags:
    print tag.contents[0]
    num_list.append(int(tag.contents[0]))

print sum(num_list)