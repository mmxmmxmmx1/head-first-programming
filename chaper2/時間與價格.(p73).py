import urllib.request
import time
from time import gmtime, strftime
price=99.99
while price > 6:
 page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
 text=page.read().decode('utf-8')
 where=text.find('>$')
 start_of_price= where + 2
 end_of_price= where + 6
 price=float(text[start_of_price:end_of_price])
while price:
 time.sleep(5)  
 times=time.strftime("%H:%M:%S")
 print(text)
 print("價格:",price)
 print("時間:",times)
