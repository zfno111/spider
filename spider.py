import requests

import lxml
from lxml import etree
from bs4 import BeautifulSoup

#定义虎扑步行街爬虫类
class hupubxj_spider():
        def __init__(self):
            #定义好headers,方便后续直接调用
           self.headers={
           "authority": "bbs.hupu.com",
           "method": "GET",
           "accept": "text / html, application / xhtml + xml, application / xml",
           "accept - encoding": "gzip, deflate, br",
           "accept - language": "zh - CN, zh",
           "user - agent": "Mozilla/5.0"" (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            }
        def getTieZiName(self,pagenum):
            headers=self.headers
            self.pagenum=pagenum
            for i in (1,self.pagenum):
                print(i)
                #需要转换为str
                URL="https://bbs.hupu.com/bxj-"+str(i)
                respoense=requests.get(url=URL,headers=headers)
#将获取到的数据转化为soup对象
                soup = BeautifulSoup(respoense.text, 'lxml')
# 找到所有的a标签，特征是 class_="truetit"
       #     print(soup.find_all('a',class_="truetit"))
#结果是一个列表  (实际上就是Tag列表）
        #    print(type(soup.find_all('a',class_="truetit")))
                for p in soup.find_all('a',class_="truetit"):
# 便利获取每个数据 利用get_text方法
                    print(p.get_text())
                print("-----------------第%s页爬取结束--------"%(i))


AAA=hupubxj_spider()
#输入的是字符串必须要转换为int 后续需要range使用
pageNum=int(input("请输入您想要爬去的步行街的页数： "))
AAA.getTieZiName(pageNum)
