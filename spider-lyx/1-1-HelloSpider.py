import lxml.html
import requests

url = 'https://www.python.org/dev/peps/pep-0020/'
xpath = '//*[@id="the-zen-of-python"]/pre/text()'
res = requests.get(url)
ht = lxml.html.fromstring(res.text)
text_list = ht.xpath(xpath)
print('Hello,\n'+''.join(text_list))

# 上述代码无法提取到文本
# 原因: pre标签里面添加了一个空的span标签，导致pre标签里的文本无法提取

from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, 'html.parser')
pre_tags = soup.find_all('pre')
for pre in pre_tags:
    txt = ''.join(pre.find_all(string=True, recursive=False))
    print(txt)
