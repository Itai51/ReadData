#import re
import datetime as dt
from urllib.request import urlopen
#from bs4 import BeautifulSoup

f = open("server_data.csv", "w")
f.write(str(dt.datetime.now()))
f.write("\n")
x = 0

while x < 500:
    url = "http://140.102.1.33"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    for n in range(7):
        a = html.find("<p>"+str(n)) + 4
        b = html.find(str(n)+"</p>")
        f.write(html[a:b])
        f.write("\n")

    f.write("\n")
    x = x + 1
    
f.close()