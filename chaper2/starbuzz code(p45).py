import urllib.request

page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
text = page.read().decode("utf-8")

price=text[232:238]
print("coffee beans price:="+price)
