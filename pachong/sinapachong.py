# coding=utf-8
# 获取到news.sina.com.cn/china/.
""" 
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import sys,os
import requests
import codecs
from datetime import datetime

#soup=BeautifulSoup(html_sample,'html.parser')
#for news in soup.select('news-item'):
res=requests.get('http://news.sina.com.cn/china/')
res.encoding="utf-8"

sinacontent=codecs.open("sinacontext.txt","w",'utf-8') #以utf-8编码形式只写形式打开文件
sinacontent.write(res.text) #将请求到的网页内容写入文件
sinacontent.close()#关闭文件

soup=BeautifulSoup(res.text,'html.parser')

for news in soup.select('.news-item'):
    if len(news.select('h2'))>0:
        h2=news.select('h2')[0].text
        time=news.select('.time')[0].text
        a=news.select('a')[0].text
        print(time,h2,a)

       
resItem=requests.get('http://news.sina.com.cn/c/nd/2017-07-15/doc-ifyiakur8987437.shtml')
resItem.encoding="utf-8"
#print(resItem.text)
soup1=BeautifulSoup(resItem.text,'html.parser')
#获取新闻标题
newstitle=soup1.select('#artibodyTitle')[0].text 
#获取新闻时间
timesource=soup1.select('.time-source')[0].contents[0].strip()  #时间字符串

#字符串转换成时间strptime,时间转换成字符串dt.strftime()
dt=datetime.strptime(timesource,'%Y年%m月%d日%H:%M')

#获取新闻来源
newsource=soup1.select('.time-source span a')[0].text

#获取新闻正文内容
newscontent=soup1.select('artibody p')
#newscontent=soup1.select('artibody p')[:-1] #去除最后一个p

#除去标签,strip去除空格

article=[]
for p in soup1.select('#artibody p')[:-1]:
    article.append(p.text.strip())
#print(article)
' '.join(article)  #将字典凭借成为一个字符串
"""
#改写上面方法
#article=' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
"""
print('.........................')
print(article)

#取得编辑名称
editor=soup1.select('.article-editor')[0].text.lstrip('责任编辑：') #只包含一个元素
print(editor)

#取出评论数
comments=requests.get("http://comment5.news.sina.com.cn/page/info?version=1&\
                  format=js&channel=gn&newsid=comos-fyiakur8987437&group=&compress=0\
                  &ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=loader_1500196063888_87110656")
comments.encoding='utf-8'
import json

#count=soup1.select('.commandCount1')[0].text.lstrip('责任编辑：')

#取得评论数与评论内容
jd=json.loads(comments.text.strip('var data='))
counts=jd['result']['count']['total']
print('评论数：',counts)

#获取新闻id：
newsurl='http://news.sina.com.cn/c/nd/2017-07-15/doc-ifyiakur8987437.shtml'
newsid=newsurl.split('/')[-1].rstrip('.shtml').lstrip('doc-i')
print('新闻id：',newsid)

#如何取得新闻编号
import re
newid=re.search('doc-i(.+).shtml',newsurl)
print('新闻编号',newid.group(1))
"""  
from datetime import datetime
import requests
from bs4 import BeautifulSoup

#将抓取内信息方法整理成一函式
def getNewDetail(newsurl):
    result={}
    res=requests.get(newsurl)
    #设置编码为utf-8
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    result['title']=soup.select('#artibodyTitle')[0].text #获取标题
    result['newssource']=soup.select('.time-source span a')[0].text #获取来源
    timesource=soup.select('.time-source')[0].contents[0].strip() #获取时间
    result['dt']=datetime.strptime(timesource,'%Y年%m月%d日%H:%M') #格式化时间
    result['article']=' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    result['editor']=soup.select('.article-editor')[0].text.lstrip('责任编辑：')
    result['comments']=getCommentCount(newsurl)
    return result 
    
if __name__=='__main__':
    newsInfo=getNewDetail('http://news.sina.com.cn/c/nd/2017-07-15/doc-ifyiakur8987437.shtml')
    print(newsInfo)




 