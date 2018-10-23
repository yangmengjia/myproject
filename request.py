# -*- utf-8 -*-
import requests


data = {
  'name':'yangmengjia',
  'age':20
}
response = requests.get('http://httpbin.org/get',params = data)
print(response.text)
