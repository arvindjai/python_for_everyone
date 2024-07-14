import urllib.request
import xml.etree.ElementTree as ET

'''
Task: write a Python program somewhat similar to http://www.py4e.com/code3/xml3.py. 
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and 
extract the comment counts from the XML data, compute the sum of the numbers in the file.
url: https://py4e-data.dr-chuck.net/comments_42.xml
'''

# URL: http://py4e-data.dr-chuck.net/comments_42.xml 
url = 'http://py4e-data.dr-chuck.net/comments_1949663.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    # Debug print the data :)
    print(result.text)
    nums.append(int(result.text))
print(nums)
print('Count:', len(nums))
print('Sum:', sum(nums))