import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error


xml_data = '''
<configuration>
    <server>
        <host>localhost</host>
        <port>8080</port>
    </server>
    <database>
        <name>example_db</name>
        <user>admin</user>
        <password>admin123</password>
    </database>
</configuration>
'''
tree = ET.fromstring(xml_data)

# Extract server information
server_host = tree.find('./server/host').text
server_port = tree.find('./server/port').text
# Extract database information
db_name = tree.find('./database/name').text
db_user = tree.find('./database/user').text
db_pass = tree.find('./database/password').text

print(f'Server information: \nServer host: {server_host} \nServer port: {server_port}')
print('___________________\nDatabase info:')
print(f'Database name: {db_name} \nDB username: {db_user} \nDB password: {db_pass}')