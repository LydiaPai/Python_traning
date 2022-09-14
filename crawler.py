# 抓取 PTT 電影版的網頁原始碼 (HTML)
from urllib import request as req
url="https://www.ptt.cc/bbs/NBA/index.html"
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)