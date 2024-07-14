import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

'''
Task: write a Python program somewhat similar to http://www.py4e.com/code3/xml3.py. 
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and 
extract the comment counts from the XML data, compute the sum of the numbers in the file.
url: https://py4e-data.dr-chuck.net/comments_42.xml
'''

url = 'https://py4e-data.dr-chuck.net/comments_42.xml'
input = urllib.request.urlopen(url).read()
tree = ET.fromstring(input)

comment = tree.find('.//comment')
for item in comment:
    print(item.text)