import urllib
from bs4 import BeautifulSoup

input_url = raw_input("Enter the Url:")
input_repeat = raw_input("Enter the Count:")
input_position = raw_input("Enter the position:")

repeat = int(input_repeat)
position = int(input_position)

count = 0
while count <= repeat:
    href_list = list()
    count = count + 1
    html_response = urllib.urlopen(input_url).read()
    soup = BeautifulSoup(html_response)
    tags = soup('a')
    for tag in tags:
        href_list.append(tag.get('href',None))
    print input_url
    input_url = href_list[position-1] 