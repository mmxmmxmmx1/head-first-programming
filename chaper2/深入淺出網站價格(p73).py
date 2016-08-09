import urllib.request
import time
price=99.99
while price > 6:
 time.sleep(10)
 page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
 text=page.read().decode('utf-8')
 a=text.find('$')
 b=a+1
 c=a+5
 price=float(text[b:c])
 prices=text[b:c]
 times=time.strftime('%H:%M:%S')
print(" buy it! " + prices + " 現在時間: " + times  )

 
