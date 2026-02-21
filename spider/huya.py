# -*- coding: utf-8 -*-
import os

import requests
import json

from spider.hupu import response


# url = 'https://live.huya.com/liveHttpUI/getLiveList?iGid=1663&iPageNo=1&iPageSize=120'
#
# response = requests.get(url=url, headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0',
# })
#
# json_obj = json.loads(response.text)
#
# vlist = json_obj['vList']
# for v in vlist:
#     print(v['sNick'])
#     print(v['sAvatar180'])
def request_data(url,headers):
    response = requests.get(url=url, headers = headers)
    return json.loads(response.text)

def parse_data(json_obj):
    vlist = json_obj['vList']
    result_list = []
    for v in vlist:
        result_list.append({
            'name': v['sNick'],
            'avatar': v['sAvatar180']
        })
    return result_list

def save_data(result_list,user_path):
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    for result in result_list:
        img_url = result['avatar']
        response_img = requests.get(img_url)
        file_name = result['name'] + '.png'
        file_path = os.path.join(user_path,file_name)
        print(file_path)
        with open(file_path,'wb') as f:
            f.write(response_img.content)


if __name__ == '__main__':
    url = 'https://live.huya.com/liveHttpUI/getLiveList?iGid=1663&iPageNo=1&iPageSize=120'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0',
    }
    json_obj = request_data(url,headers)
    save_data(parse_data(json_obj),'E:/study/python/spider/huya')