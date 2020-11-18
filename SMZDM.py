import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re




def main():
    url=('https://wiki.smzdm.com/yundonghuwai/p')
    # find_url=re.compile(r'<a.*>"(.*?)"',re.S) # 商品url s 去重
    find_name=re.compile(r'target="_blank">"(.*)"</a></h5>') # 商品名称
    # find_tag=re.compile('')  # 商品标签
    # find_price=re.compile('') # 商品价格
    # askUrl(url)
    # print(res)
    for i in range(0,1):
        urls=url+str(i)
        html=askUrl(urls)
        # print(html)
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.findAll('div',class_="feed-content"):
            str_item=str(item)
            ite=re.findall(find_name,str_item)
            # name=re.findall(find_name,str_item)
            print(ite)


def askUrl(url):
    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
    respone=urllib.request.Request(url,headers=headers)
    html=urllib.request.urlopen(respone)
    htmld=html.read().decode("utf-8")
    return htmld



if __name__ == "__main__":
    main()