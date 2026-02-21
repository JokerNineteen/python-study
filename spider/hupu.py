import requests
from bs4 import BeautifulSoup
from lxml import etree
import csv

url = 'https://bbs.hupu.com/lol-1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0',
    'Host': 'bbs.hupu.com',
}

response = requests.get(url, headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title.string)
root = etree.HTML(response.text)
post = root.xpath('//div[@class="bbs-sl-web-post"]/ul/li//div[@class="post-title"]/a/text()')
href = root.xpath('//div[@class="bbs-sl-web-post"]/ul/li//div[@class="post-title"]/a/@href')
author = root.xpath('//div[@class="bbs-sl-web-post"]/ul/li//div[@class="post-auth"]/a/text()')
time = root.xpath('//div[@class="bbs-sl-web-post"]/ul/li//div[@class="post-time"]/text()')
print(type(href))
print(author)
print(time)

for i in post:
    print(i)

info = []
for i in range(len(post)):
    info.append([post[i], href[i], author[i], time[i]])

fieldNames = ['标题', '链接', '作者', '时间']
f = open('hupu.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(f)
writer.writerow(fieldNames)
writer.writerows(info)
f.close()