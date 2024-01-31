import time
from datetime import datetime
from urllib.request import urlopen


t0 = time.time()
x = 0
name = str(datetime.now()).replace("-", "").replace(" ", "_").replace(":", "")[:13]
f = open("IMU_DATA/"+name+".csv", "w")
f.write(name)
f.write("\ntimestamp,index,AccelX,AccelY,AccelZ,GyroX,GyroY,GyroZ\n")

now = datetime.now()

if(now.minute >= 30):
    after30 = 1
else:
    after30 = 0

while(1):
    now = datetime.now()

    if((now.minute == 0 and after30) or (now.minute == 30 and not after30)):
        f.close()

        name = str(now).replace("-", "").replace(" ", "_").replace(":", "")[:13]
        f = open("IMU_DATA/"+name+".csv", "w")
        f.write(name)
        f.write("\ntimestamp,index,AccelX,AccelY,AccelZ,GyroX,GyroY,GyroZ\n")

        now = datetime.now()
        
        if(now.minute >= 30):
            after30 = 1
        else:
            after30 = 0

    url = "http://140.102.1.33"

    try:
        page = urlopen(url)
    except:
        html = "<p>error - no signal</p>"
        sample = 0
    else:
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        sample = 1
    
    f.write(str(now).replace(" ", "_"))
    f.write(",")
    a = html.find("<p>") + 3
    b = html.find("</p>")
    f.write(html[a:b])
    f.write("\n")

    if(sample):
        t = time.time()
        print(t)
        x += 1
        freq = x / (t-t0)
        print(freq)

f.close()