#Coursera - XML Parsing - Chapter 13

import xml.etree.ElementTree as ET
# triple quotes below make one long string in Python
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print (tree)
print (type(tree))
print('Name:', tree.find('name').text) # .text gets the attribute of that particular node - node would be line 7
print('Attr:', tree.find('email').get('hide')) #up to email gets the whole directory (get asks the attribute inside the hide attribute)
