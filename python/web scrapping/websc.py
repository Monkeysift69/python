import requests
from bs4 import BeautifulSoup

url="http://61.7.240.164:81/room65/r65.php/index1.php"
data=requests.get(url,headers={"User-Agent": "Mozilla/5.0"})
print(data.text)