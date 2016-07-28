import requests
from xml.etree import ElementTree


api_key = 'd04db0e7c57679c3f4247757fce82ecf',
user = 'bill@williamjohngardner.com'

url = "https://williamjohngardner.highrisehq.com/companies.xml"
response = requests.get(url, auth=('c8b5caeec4d60694480e0a47ff92e8d1', 'X'))
response.encoding = 'xml'
for item in response:
    print(response.text)
