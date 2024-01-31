import time
import datetime
from urllib.request import urlopen


t0 = time.time()
f_name = "000000startup_test"
f = open("DATA/"+f_name+".csv", "w")
f.write(f_name)
print(f_name)
f.write("\ntimestamp,index,AccelX,AccelY,AccelZ,GyroX,GyroY,GyroZ\n")

for x in range(500):
    now = datetime.datetime.now()

    url = "http://140.102.1.33"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    
    f.write(str(now).replace(" ", "_"))
    f.write(",")
    a = html.find("<p>") + 3
    b = html.find("</p>")
    f.write(html[a:b])
    f.write("\n")

    t = time.time()
    print(t)
    freq = (x+1) / (t-t0)
    print(freq)

f.close()

t0 = time.time()
x = 0
f_name = str(datetime.datetime.now()).replace(" ", "_").replace(":", "").replace(".", "")
f = open("DATA/"+f_name+".csv", "w")
f.write(f_name)
print(f_name)
f.write("\ntimestamp,index,AccelX,AccelY,AccelZ,GyroX,GyroY,GyroZ\n")

now = datetime.datetime.now()
print(str(now))

if(now.minute >= 30):
    after30 = 1
else:
    after30 = 0

while(1):
    now = datetime.datetime.now()

    if((now.minute == 0 and after30) or (now.minute == 30 and not after30)):
        f.close()

        f_name = str(now).replace(" ", "_").replace(":", "").replace(".", "")
        f = open("DATA/"+f_name+".csv", "w")
        f.write(f_name)
        print(f_name)
        f.write("\ntimestamp,index,AccelX,AccelY,AccelZ,GyroX,GyroY,GyroZ\n")

        now = datetime.datetime.now()
        print(str(now))
        
        if(now.minute >= 30):
            after30 = 1
        else:
            after30 = 0

    url = "http://140.102.1.33"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    
    f.write(str(now).replace(" ", "_"))
    f.write(",")
    a = html.find("<p>") + 3
    b = html.find("</p>")
    f.write(html[a:b])
    f.write("\n")

    t = time.time()
    print(t)
    x += 1
    freq = x / (t-t0)
    print(freq)

f.close()