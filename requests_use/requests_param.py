import requests

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
}

# response = requests.get(url,headers)
#
# with open('baidu.html','w',encoding='utf-8') as f:
#     f.write(response.content.decode())

data = {
    'wd': '刘涛说我知道我的身材很曼妙'
}

response = requests.get(url,headers=headers,params=data)

with open('baidu1.html','w',encoding='utf-8') as f:
    f.write(response.content.decode())