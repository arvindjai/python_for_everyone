import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Arvind</name>
        </user>
        <user x="5">
            <id>002</id>
            <name>vindy</name>
        </user>
        <user x="7">
            <id>004</id>
            <name>root</name>
        </user>
    </users>
</stuff>'''

tree = ET.fromstring(data)
lst = tree.findall('users/user')
for item in lst:
    print('name:', item.find('name').text)
    print('id:', item.find('id').text)
    print('Attr:', item.get('x'))
    print('__________')