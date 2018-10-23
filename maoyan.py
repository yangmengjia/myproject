# -*-coding:utf-8 -*-

import requests
from lxml import etree
from requests.exceptions import RequestException
import json

def get_one_page(url):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      return response.text
    return response.status_code
  except RequestException:
    return None

def parse_one_page(html):
  html = html.replace(r'<!--', '"').replace(r'-->', '"')
  items = etree.HTML(html)
  content_list = items.xpath('//div[@class="hd"]/a[@class]/@href')
  # print(content_list)
  return content_list

def write_to_file(content):
  with open('result.txt','a',encoding='utf-8') as f:
    f.write(json.dumps(content,ensure_ascii=False) + '\n')
    f.close()

def main(start):
    url = 'https://movie.douban.com/top250?start=' + str(start) + '&filter='
    html = get_one_page(url)
  # print(html)
    for content in parse_one_page(html):
      # print(content)
      write_to_file(content)

if __name__ == '__main__':
  for i in range(6):
    main(start=i*25)

