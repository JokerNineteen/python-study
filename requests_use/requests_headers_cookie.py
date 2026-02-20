import requests

url = 'https://github.com/exile-morganna'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/',
    'Cookie': '_octo=GH1.1.1616447148.1700864007; _device_id=9b0c5e4a2f3c8b9d9e5c6f7a8b9c0d1; user_session=eyJ1c2VyX2lkIjoxNjE2NDQ3MTQ4LCJ1c2VyX25hbWUiOiJleGlsZS1tb3JnYW5uYSIsInNlc3Npb25faWQiOiJmYjA4ODg0ODg5YjEwZDEyYjA4ODg0ODg5YjEwZDEyIiwic2lnbmF0dXJlIjoiZjkzMGRiM2E4ZDUxYjA4ODg0ODg5YjEwZDEyODg4NDg4OTg5'
}

response = requests.get(url,headers=headers)