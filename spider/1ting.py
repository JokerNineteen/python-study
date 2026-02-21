import json

import requests
from bs4 import BeautifulSoup
from lxml import etree
import csv

# url = 'https://www.1ting.com/song_n.html'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0',
# }
#
# response = requests.get(url, headers=headers)
#
# with open('1ting.html', 'w', encoding='utf-8', newline='') as fp:
#     fp.write(response.text)

def parse_data(html_string):
    root = etree.HTML(html)
    ul_list = root.xpath('//div[@class="songList"]/ul')
    song_list = []
    for ul in ul_list:
        li_list = ul.xpath('./li')
        for li in li_list:
            song_list.append({ 'name': li.xpath('./a/text()')[0], 'href': li.xpath('./a/@href')[0]})
    print(song_list)
    return song_list

def save_data(items):
    file_open = open('1ting.csv', 'w', encoding='utf-8', newline='')
    for item in items:
        json_string = json.dumps(item, ensure_ascii=False)
        file_open.write(json_string + '\n')
    file_open.close()

if __name__ == '__main__':
    with open('1ting.html', 'r', encoding='utf-8') as fp:
        html = fp.read()
    song_list = parse_data(html)

    save_data(song_list)

    for song in song_list:
        print(song)