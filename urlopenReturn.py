from urllib.request import urlopen

url = 'file:///C:/Users/itais/U-HAIFA/SNAPIR%20IMU/ReadData/test.html'

while(1):
	try:
		page = urlopen(url, timeout=0.009)
		html_bytes = page.read()
		html = html_bytes.decode("utf-8")
		print(html)
	except:
		print("ERROR!")