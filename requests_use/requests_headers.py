import requests

url = 'https://www.baidu.com'
response = requests.get(url)

print(len(response.content.decode()))
print(response.content.decode())

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
}

response1 = requests.get(url,headers)

print(len(response1.content.decode()))
print(response1.content.decode())