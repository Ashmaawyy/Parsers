# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 02:37:18 2020

@author: Al Ashmawy
"""
import xml.etree.ElementTree as ET
data = '''
<person>
<name>chuck</name>
<phone type = "iphone">+201152385059</phone>
<id>29808151204259</id>
<email hide = "yes"/>
</person>
'''
tree = ET.fromstring(data)
#print("Name: ", tree.find('name').text)
#print("Phone Number: ", tree.find('phone').text)
#print("ID: ", tree.find('id').text)
#print("Attrib.: ", tree.find('email').get('hide'))

###########################Multi-Tag########################

xml_input = '''
<stuff>
<users>
<user x = "2">
<name>Ali</name>
<phone type = "Iphone">+201152385059</phone>
<id>29808151204259</id>
<email hide = "yes"/>
</user>
<user x = "4">
<name>Omar</name>
<phone type = "Samsung">+201152385058</phone>
<id>29808151204258</id>
<email hide = "yes"/>
</user>
<user x = "5">
<name>Ahmed</name>
<phone type = "OPPO">+201152385057</phone>
<id>29808151204257</id>
<email hide = "yes"/>
</user>
</users>
</stuff>
'''
stuff = ET.fromstring(xml_input)
lst = stuff.findall('users/user')
print("Total Users: ",len(lst))
for item in lst:
    print("User Name: ", item.find('name').text)
    print("User ID: ", item.find('id').text)
    print("User Phone", item.find('phone').attrib)
    print("User Phone Number: ", item.find('phone').text)
################################Assignment#################################
import urllib
import re
from urllib.request import urlopen
url = "http://py4e-data.dr-chuck.net/comments_985010.xml"
xml = urlopen(url).read()
comments = ET.fromstring(xml)
lst = comments.findall('comments/comment')
summ = 0
for item in lst:
    summ = summ + int(item.find('count').text)
    print(summ)    












