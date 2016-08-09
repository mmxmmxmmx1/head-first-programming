import twitter
import urllib.request
import time

def coffee_one():
  time.sleep(2)  
  page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
  text=page.read().decode('utf-8')
  a=text.find('$')
  b=a+1
  c=a+5
  price=float(text[b:c])
  return (price)
coffee_one()

x=input("折扣價格Y，原始價格按任意鍵: ")

if x =="Y":
 price=99.99  
 while price > 5.5 :
   price=coffee_one()  
 print("buy ")

else:
 print(coffee_one())

api = twitter.Api(consumer_key='kBSyDaW8EKMjfRo3IVyNMVyd0',
                      consumer_secret='cvP1WeYie1IX1FMIZmKJVbc8Knnvcc5rNQqdpSBw0XVaWW01uA',
                      access_token_key='470755805-FaSeuJoWyhcK3Ok5SicuP70BDCG7yuAogNuB6tMy',
                      access_token_secret='uvDAS4HVoknyfhxxZL15sNOVKB86saugIxlTyKpubVuDA')

status = api.PostUpdate(str(coffee_one()))
