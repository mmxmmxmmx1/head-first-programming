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


print("咖啡價格查詢 ")
x=input("折扣價格Y，原始價格按任意鍵: ")

if x =="Y":
 price=99.99  
 while price > 5.5 :
   price=coffee_one()  
   print(price)
 print("buy ")

else :  
  print(coffee_one()) 
