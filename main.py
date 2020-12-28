import requests
from bs4 import BeautifulSoup
import json
import time

#debug用
def wait_enter():
    input()

#用来检查字符串中是否含有一组词汇中的某个或者多个
def have_either(words, string):
    b = False
    for w in words:
        if w in string:
            b = True
            return b
    return b

#用来输出结果
def flash(d):
    with open('data.json', 'w') as outfile:
        json.dump(d, indent=2, ensure_ascii=False, fp=outfile)
    # print(json.dumps(d, indent=2, ensure_ascii=False))

#检索价格范围，当前为5W～8W
ran = (50000, 80000)
#当前页码，从第一页开始爬
page_num = 1
#存放商品的列表
goods = []
#不希望标题和描述信息中含有的词汇（这里因为不想买数字版的，所以加入了关于数字版的词汇）
bad_words = ['デジタル', 'digital', 'Digital', 'CFI-1000B01', 'Degital', 'デシダル', 'ディスクドライブ非搭載']
#希望标题和描述信息中含有的词汇
good_words = ['PS5', 'ps5', 'プレイステーション5', 'プレステ5', 'PlayStation5']

#主循环，不断更新最新信息，可以用ctrl+c来关闭程序
while True:
    print(f'page num: {page_num}')
    url = f'https://fril.jp/s?max={ran[1]}&min={ran[0]}&order=desc&page={page_num}&query=PS5&sort=sell_price&transaction=selling'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('div', class_='item')
    
    if len(items) == 0:
        print(len(goods))
        
        page_num = 1
        goods = []
        continue
    page_num += 1
    for item in items:
        item_info = {}
        item_title = item.find("span", attrs={'itemprop': 'name'}).contents[0]
        
        if not have_either(bad_words, item_title):
            if have_either(good_words, item_title):
                item_url = item.find('a', class_='link_search_image')['href']
                sub_soup = BeautifulSoup(requests.get(item_url).text, 'html.parser')
                bbreak=False
                try:
                    item_ps = sub_soup.find('div', class_='item__description').find_all('p')
                    for p in item_ps:
                        if have_either(bad_words, p.text):
                            bbreak = True
                            break
                        if not have_either(good_words, p.text):
                            bbreak = True
                            break
                    if bbreak is True:
                        continue
                except:
                    pass
                item_price = item.find('span', attrs={'itemprop': 'price'})['data-content']
                item_info['title'] = item_title
                item_info['price'] = item_price
                item_info['url'] = item_url

                goods.append(item_info)
                flash(goods)  
    # time.sleep(0.5)
