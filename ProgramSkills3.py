def printhead(headstring):
    print("**************************************************************************************************************")
    print(printString.center(96,'*'))
    print("**************************************************************************************************************")

#4.1.如何读写csv数据
printString = '4.1.如何读写csv数据'
printhead(printString)
import requests
import json
import csv
from bs4 import BeautifulSoup

books = []
def book_name(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find(class_="grid-16-8 clearfix").find(class_="indent").find_all('table')

    for i in items:
        book = []
        title = i.find(class_="pl2").find('a')
        book.append('《' + title.text.replace(' ', '').replace('\n', '') + '》')

        star = i.find(class_="star clearfix").find(class_="rating_nums")
        book.append(star.text + '分')

        try:
            brief = i.find(class_="quote").find(class_="inq")
        except AttributeError:
            book.append('”暂无简介“')
        else:
            book.append(brief.text)

        link = i.find(class_="pl2").find('a')['href']
        book.append(link)

        global books
        books.append(book)

        print(book)

    try:
        next = soup.find(class_="paginator").find(class_="next").find('a')['href']
    # 翻到最后一页
    except TypeError:
        return 0
    else:
        return next


next = 'https://book.douban.com/top250?start=0&filter='
count = 0

while next != 0:
    count += 1
    next = book_name(next)
    print('-----------以上是第' + str(count) + '页的内容-----------')

csv_file = open('D:/top250_books.csv', 'w', newline='', encoding='utf-8')
w = csv.writer(csv_file)
w.writerow(['书名', '评分', '简介', '链接'])
for b in books:
    w.writerow(b)
