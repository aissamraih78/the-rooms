import urllib.request
import os

url = 'https://catbox.moe/user/api.php'
file_path = r'C:\Users\Alone\Desktop\syntaxcraft_product_demo.mp4'

boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
with open(file_path, 'rb') as f:
    file_bytes = f.read()

part1 = (
    f'--{boundary}\r\n'
    f'Content-Disposition: form-data; name="reqtype"\r\n\r\n'
    f'fileupload\r\n'
    f'--{boundary}\r\n'
    f'Content-Disposition: form-data; name="fileToUpload"; filename="syntaxcraft_product_demo.mp4"\r\n'
    f'Content-Type: video/mp4\r\n\r\n'
).encode('utf-8')

part2 = f'\r\n--{boundary}--\r\n'.encode('utf-8')
data = part1 + file_bytes + part2

req = urllib.request.Request(
    url,
    data=data,
    headers={
        'Content-Type': f'multipart/form-data; boundary={boundary}',
        'User-Agent': 'Mozilla/5.0'
    }
)

try:
    with urllib.request.urlopen(req, timeout=90) as resp:
        result = resp.read().decode('utf-8').strip()
        print('SUCCESS_URL:' + result)
except Exception as e:
    print('ERROR:', e)

