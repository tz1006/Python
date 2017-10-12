#!/usr/bin/python
#_*_ coding:'utf-8' _*_

import requests
from bs4 import BeautifulSoup
from ghost import Ghost, Session
from datetime import datetime

##############################

kw = 'Embroidered Leather'

##############################
name = 'Last Frist'
email = 'abc@gmail.com'
tel = '(123) 456-7890'
address1 = '1333 E Alosta Ave'
address2 = ''
zip = '91702'
city = 'Azusa'
state = "\'CA\'"
card = '4336 6800 0397 3798'
cvv = '021'
month = "\'02\'"
year = "\'2019\'"
##############################
jackets = 'http://www.supremenewyork.com/shop/all/jackets'
skirts = 'http://www.supremenewyork.com/shop/all/shirts'
tops = 'http://www.supremenewyork.com/shop/all/tops_sweaters'
sweatshirts = 'http://www.supremenewyork.com/shop/all/sweatshirts'
pants = 'http://www.supremenewyork.com/shop/all/pants'
hats = 'http://www.supremenewyork.com/shop/all/hats'
bags = 'http://www.supremenewyork.com/shop/all/bags'
accessories = 'http://www.supremenewyork.com/shop/all/accessories'
sakte = 'http://www.supremenewyork.com/shop/all/skate'
##############################
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
host = 'www.supremenewyork.com'
ae = 'gzip, deflate, br'
al = 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
a = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
re = 'http://www.supremenewyork.com/shop'
ck = 'lastid=1507310046413; mp_mixpanel__c=0; __utma=74692624.319201636.1507274548.1507288133.1507306081.5; __utmc=74692624; __utmz=74692624.1507274548.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.319201636.1507274548; _gid=GA1.2.1580123961.1507274548; tohru=c1ae7f86-7ed0-4cd7-ba85-9c83938b0a1c; cart=1+item--48350%2C17801; _supreme_sess=Z1Q5LzQ3TW5VNlVYbHNSOGo4Qi8xRFlRN0taV0dJbFZuTkUrWUdCWkg0aHVOOXhrY3JmQlRhWXN2dlByY2kwaTlYclg4Tmg5SzhDdGQxb0M3QVB0N05ZSm1zZzZkK0VwUzlsZGpBLzlzQmhsRVpQSzZ0elZnSUljTnEyZmRPWmJDRmFpVW1CTkRaUkZaZVFJU3Y5QVA5disvWE5VZXhsOEtXZ1had2I1SmtNUEVUZGdXOGV0Tjk0YmhWYXFneVFOU2VpbzhGWVpqSnA5dkFxM1JQaDFNOHhIOHczSGgzTDNhaHBaQWlrVkdTUXJTY2wrZ1ZpbUZBcE1BNk9YeXNvcVBrZDNtQ2RRZXdiV1pybFJhc2VIcUczc3pJNlV6T0E1S1RHOG1qOHAyMFZIOERPUG9wMXUzOUdhODUvaGFsSEwzQXphcW91NWhuak9OM0FUSWhUdU5DMFo3SDFzL2ZoT09ac1JGcG9pZXNPcDlKS1hvV1p5N2FJNHdQM1FYODZtL2lmaERmenk5dWtVRjV0QWpYSFBKUHJGTTVqb2NVcWhyNDZqT0ZmNWsrVlVXeDN0KzRaTTlsSGNIZEhaenIvWDdrdmg3TTJqaWtzS0V6NEZpUVRXS3p3Q2xlY2RmWStSTkYwNjVhRXhKOXl2MkJpYlJLQ2liTDNvNkdKd3p1U2orcUIvc3lKVTRmT0c3L3RySUlEWWJYN24zNFlGQ1V4dGgzakQ5VnIrY09GRHI1WmFNek1YeVhNbVpZWmtaNVlhLS1PWXN5Q2ZvSGJVeGVqMnhYMEJBRmdBPT0%3D--26c925e04984f16a492adcb79e6c5f37cfc12697; pure_cart=%7B%2248350%22%3A1%2C%22cookie%22%3A%221%20item--48350%2C17801%22%2C%22total%22%3A%22%24668%22%7D; __utmb=74692624.16.10.1507306081; mp_c5c3c493b693d7f413d219e72ab974b2_mixpanel=%7B%22distinct_id%22%3A%20%2215ef09062b39-0ce82cb3458555-49546c-13c680-15ef09062b46c8%22%2C%22Store%20Location%22%3A%20%22US%20Web%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; _gat=1; __utmt=1'
##############################
header = {'Host':host, 'User-Agent':ua, 'Accept':a, 'Accept-Language':al, 'Accept_encoding':ae, 'Referer':re, 'Cookie':ck}
gh = Ghost()
se = Session(gh, user_agent=ua, wait_timeout=40, wait_callback=None, display=True, viewport_size=(800, 600), download_images=True)
##############################

def stock (type):
  global soup
  global stock_items
  global stock_list
  print ('\033[1;35mLoading the Website...\033[0m')
  stock_html = requests.get(type, headers = header,verify=False).content
  stock_soup = BeautifulSoup(stock_html, "html.parser")
  stock_items = stock_soup.select('.inner-article')
  stock_list = ['a']
  for i in range(len(stock_items)):
    globals()['name'+str(i)] = stock_items[i].text
    globals()['url'+str(i)] = "http://www.supremenewyork.com" + stock_items[i].p.find('a').get("href")
    stock_list.append(globals()['name'+str(i)])
  del stock_list[0]
  print ('\033[1;34m')
  for l in stock_list:
    print (l)
  print ('\033[0m')

def add (keyword, size):
  value = [stock_list.index(i) for i in stock_list if keyword in i]
  excute_name = globals()['name'+ str(value[0])]
  excute_url = globals()['url'+ str(value[0])]
  print (excute_name)
  print (excute_url)
  se.open(excute_url)
  se.evaluate("document.getElementById('s').selectedIndex = " + size + ';')
  se.show()
  se.evaluate("""document.querySelector('input[name="commit"]').click();""")
  se.sleep(0.5)
  print ('\033[1;35mSuccessfuly add ' + '\033[1;32m' + excute_name + '\033[1;35m to the cart!\033[0m')

def cart():
  cart_url = 'http://www.supremenewyork.com/shop/cart'
  se.open(cart_url)
  cart_html = se.content
  cart_soup = BeautifulSoup(cart_html, "html.parser")
  cart_items = cart_soup.select('tr')
  print ('-----------------------Cart List-----------------------')
  for i in range(len(cart_items)):
    globals()['item'+str(i)] = cart_items[i].select('.cart-description')[0].text
    globals()['price'+str(i)] = cart_items[i].select('.cart-price-span')[0].text
    print ('\033[1;35mItem: ' + '\033[1;34m' + globals()['item'+str(i)] + '\033[1;35m   Price: ' + '\033[1;31m' + globals()['price'+str(i)] + '\033[0m')
  print ('-------------------------End--------------------------')

def fill ():
  global checkout_url
  checkout_url = 'https://www.supremenewyork.com/checkout'
  se.open(checkout_url)
  se.show()
  fill_html = se.content
  fill_soup =  BeautifulSoup(fill_html, "html.parser")
  card_id = str(se.evaluate("document.getElementsByTagName('input')[12].id")[0])
  cvv_id = str(se.evaluate("document.getElementsByTagName('input')[13].id")[0])
  se.click("input[id=order_billing_name]", expect_loading=False)
  se.set_field_value("input[id=order_billing_name]", name)
  se.set_field_value("input[id=order_email]", email)
  se.click("input[id=order_tel]", expect_loading=False)
  se.set_field_value("input[id=order_tel]", tel)
  se.set_field_value("input[id=bo]", address1)
  se.set_field_value("input[id=oba3]", address2)
  se.set_field_value("input[id=order_billing_zip]", zip)
  se.set_field_value("input[id=order_billing_city]", city)
  se.set_field_value("input[id=" + card_id + "]", card)
  se.set_field_value("input[id=" + cvv_id + "]", cvv)
  se.evaluate("document.getElementById('order_billing_state').value=" + state)
  se.evaluate("document.getElementById('credit_card_month').value=" + month)
  se.evaluate("document.getElementById('credit_card_year').value=" + year)
  se.click(".has-checkbox > div:nth-child(2) > ins:nth-child(2)", expect_loading=False)
  print ('\033[1;35m Information Filled! Please click payment button and do Verification\033[0m')
  print ('''\033[1;35m
  Notice:
  Press Control + C to Intrrupt and Continue.
  If you see any information that is blank, don't make the payment!
  Then Use Commmand checkout() to make the purchase manually\033[0m
  ''')
  se.sleep(200)

def checkout ():
  se.open(checkout_url)
  se.sleep(200)

def confirm ():
  fill()
  # se.click("input.button", expect_loading=True)
  se.wait_for_page_loaded()
  filename = datetime.now()
  se.show()
  se.capture_to("./%s.png" % str(filename))

print ('''
stock(jackets)
add(kw, '0')
fill()
''')

import code
code.interact(banner = "", local = locals())

raw_input("Press <enter> To Quit!")
