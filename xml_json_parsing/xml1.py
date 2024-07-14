import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Arvind</name>
    <phone type="intl">
    +91978645312
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
print('Phone',tree.find('phone').text)
