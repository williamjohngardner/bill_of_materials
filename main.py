import requests

api_key = 'd04db0e7c57679c3f4247757fce82ecf',
user = 'bill@williamjohngardner.com'

url = "https://williamjohngardner.highrisehq.com/people.xml"
response = requests.get(url, auth=('d04db0e7c57679c3f4247757fce82ecf', 'X'))

print(response)
