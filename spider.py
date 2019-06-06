import requests
#进程池
from multiprocessing import Pool
import time


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
        def userInfo(self,url):
            self.url = url
            respoense = requests.get(url=self.url, headers=self.headers)
            # 将获取到的数据转化为soup对象
            soup = BeautifulSoup(respoense.text, 'lxml')
            if soup.find('span', itemprop="gender"):
                userSex = soup.find('span', itemprop="gender").get_text()
            else:
                userSex = "NULL"
            print("用户的性别是:  %s" % (userSex))


        def getTieZiInfo(self,pagenum):
            # 中间写上代码块
            headers=self.headers
            self.pagenum=pagenum

            #需要转换为str
            URL="https://bbs.hupu.com/bxj-"+str(self.pagenum)
            respoense=requests.get(url=URL,headers=headers)
#将获取到的数据转化为soup对象
            soup = BeautifulSoup(respoense.text, 'lxml')
# 找到所有的a标签，特征是 class_="truetit"
   #     print(soup.find_all('a',class_="truetit"))
#结果是一个列表  (实际上就是Tag列表）
    #    print(type(soup.find_all('a',class_="truetit")))
            for p in soup.find_all('a',class_="truetit"):
                print("-----------------开始---华丽的分割线-----------")
# 获取a标签的内容
                print("帖子的内容如下:   ")
#获取帖子的内容
                postInformation=p.get_text()
                print(postInformation)
                parentInfo=p.parent
                if parentInfo.find("span",class_="light_r"):
                    # print(parentInfo.find("span",class_="light_r").a["title"])
#获取热门回帖,没有就为0
                    light_r=parentInfo.find("span", class_="light_r").a["title"]
                    print("帖子目前的热度为: %s"%(light_r))
                else:
                    light_r=0
#获取作者的信息--名字
                grandPaInfo=parentInfo.parent
                userName=grandPaInfo.find("div",class_="author box").a.get_text()
                print("用户的名字是: %s"%(userName))
#获取用户的主页
                userUrl=grandPaInfo.find("div",class_="author box").a['href']
                print("%s的主页地址是:   %s  "%(userName,userUrl))
                self.userInfo(userUrl)
            print("-----------------第%s页爬取结束--------"%(i))


if __name__ == '__main__':
    AAA=hupubxj_spider()
    #输入的是字符串必须要转换为int 后续需要range使用
    pageNum=int(input("请输入您想要爬去的步行街的页数： "))
    p = Pool(4)
    startTime = time.time()
    for i in range(pageNum):
        p.apply_async(AAA.getTieZiInfo,args=(i,))
    p.close()
    p.join()
    stopTime = time.time()
    print('Running time: %0.2f Seconds' % (stopTime - startTime))

