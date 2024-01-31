import math as m
import numpy as np

x = -10

for x in np.linspace(-2, 2, 11):
	try:
		y = m.sin(x) / x
	except:
		print("undefined")
	else:
		print(y)

	x += 0.1