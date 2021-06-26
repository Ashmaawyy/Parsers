# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 04:15:41 2020

@author: Al Ashmawy
"""

import json
data = '''
{
 "name" : "Chuck",
 "phone" : {
     "type" : "Intel",
     "number" : "+201152385059"
     },
 "email" : {
     "hide" : "yes"
     }
 }
'''
#info = json.loads(data)
#print('Name: ',info["name"])
#print('Phone Number: ',info["phone"]["number"],"Phone Type: ",info["phone"]["type"])
#print('Hide: ',info["email"]["hide"])

############################Listed Dictionaries#############################
data_2 = '''
[
 { "id" : "29808151204259" ,
   "x" : "2" ,
   "name" : "Ali" ,
  } ,
 { "id" : "29808151204258" ,
  "x" : "3" ,
  "name" : "Omar"
  }
 ]
'''
info = json.loads(data_2)
print("Total Users: ",len(info))
for item in info:
    print('Name: ',item["name"])
    print('ID',item["id"])
    print('Attribute',item["x"])

################################Task############################


import urllib
import re
from urllib.request import urlopen
url = "http://py4e-data.dr-chuck.net/comments_985011.json"
json_data = urlopen(url).read()
lst = json.loads(json_data)
#lst = comments.findall('comments/comment')
summ = 0
#print(len(lst))
#print(type(lst))
#print(lst["note"])
for item in lst["comments"]:
    #print(item["count"])
    summ = summ + int(item["count"])
print(summ)



