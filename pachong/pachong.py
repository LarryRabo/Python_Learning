from bs4 import BeautifulSoup
from html.parser import HTMLParser


html_sample='<html>\
<body>\
<h1 id="title">hello world</h1>\
<a href="#" class="link">this is link1</a>\
<a href="# link2" class="link">this is link2</a>\
</body>\
</html>'

soup=BeautifulSoup(html_sample,'html.parser')
print(type(soup))
print(soup.text)

print('_________1__________')
#使用select找出含h1标签的元素
soup1=BeautifulSoup(html_sample,'html.parser')
header=soup1.select('h1')
print(header)
print(header[0])
print(header[0].text) #把h1中间的content

print('_________2__________')
#使用select找出含a标签的元素
al='<a href="#" class="link">this is link1</a>\
<a href="# link2" class="link">this is link2</a>'
soup2=BeautifulSoup(al,'html.parser')
alink2=soup2.select('a')
for link in alink2:
    print(link)

print('_________3__________')
#使用select找出所有class为link的元素（class前面需要加上）
l='<a href="#" class="link">this is link1</a>\
<a href="# link2" class="link">this is link2</a>'

soup3=BeautifulSoup(l,'html.parser')
for link3 in soup3.select( '.link'):
    print(link3) 
    
print('_________4__________')
#使用select找出所有id为title的元素
h="<h1 id='title'>hello world</h1>"
soup4=BeautifulSoup(h,'html.parser')
alink4=soup4.select('#title')
print(alink4) 

print('__________5_________')
#使用select找出所有a tag的href链接
hr='<a href="# link2" class="link">this is link2</a>'
soup5=BeautifulSoup(hr,'html.parser')
alink5=soup5.select('a')
for link in alink5:
    print(link['href'])
    print(link['class'])
    
    

    
    

    