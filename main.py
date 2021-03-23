#print("hello")
#print("cheska")

import requests


# resp = requests.get("http://cordova.org/")
resp = requests.get("http://www.pagasa.dost.gov.ph")
#print(resp)

##200 = okay#
##python2.7
#print(resp.text)

data = ""
data = resp.text
#
print(data[0:10])

if(data[0:10] == "<!DOCTYPE "):
    print("hello")



