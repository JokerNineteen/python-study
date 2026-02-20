import requests

url = 'https://www.baidu.com'
response = requests.get(url)

# print(response.encoding)
# response.encoding = "utf-8"
# print(response.text)
#
# print(response.encoding)
#
# print(response.content)
#
# print(response.content.decode())

# print(response.url)
# print(response.status_code)
# print(response.request.headers)
# print(response.headers)

print(response.cookies)