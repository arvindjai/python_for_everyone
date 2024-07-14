import urllib.request
import xml.etree.ElementTree as ET

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