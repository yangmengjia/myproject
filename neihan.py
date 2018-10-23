# -*- coding:utf-8 -*-

import re
import urllib
import urllib.request
import requests
from lxml import etree

class Spider:
  def __init__(self):
    self.page = 0
    self.switch = True

  def loadpage(self):
    url =  "http://maoyan.com/board/4?offset=" + str(self.page * 10)
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    response = requests.get(url)
    print(response)
    response.encoding = 'utf8'
    #获取每页HTML源码字符串
    html = response.text
    # print(html)
    print(html)
    #创建正则表达式规则对象，匹配每页里的段子内容。
    #pattern = re.compile('//<p\sclass="name">\s<a\shref="/films/\d"\stitle="(.*)">',re.S)
    pipei = etree.HTML(html)

    content_list = pipei.xpath('//p[@class="name"]/a')

    #将正则匹配对象应用到HTML的源码字符串里，并findall()返回这个页面所有段子的一个列表。
    #content_list = pattern.findall(str(html))
    for content in content_list:
        print(content)
  #   self.dealpage(content_list)
  #
  # def dealpage(self,content_list):
  #   for item in content_list:
  #     item = item.replace("<p>","").replace("</p>", "").replace("<a"," ")
  #     self.writepage(item)
  #
  # def writepage(self,item):
  #   print("正在写入数据......")
  #   with open("jiandan.txt",a) as f:
  #     f.write(item)
  #
  # def control(self):
  #   """控制爬虫运行"""
  #   while self.switch:
  #     self.loadpage()
  #     command = input("如果继续爬取，请按回车（退出输入quit)")
  #     if command == "quit":
  #        self.switch = False
  #     self.page += 1
  #   print("谢谢使用！")

if __name__ == "__main__":
  jiandanpage = Spider()
  jiandanpage.loadpage()
  # jiandanpage.control()
