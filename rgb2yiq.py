"""
	RGB2YIQ
	Version: 1.0
	December 1st, 2014
	
	For Python 3
"""
from PIL import Image
from struct import *
import sys

if len(sys.argv) > 1:
	useimg = sys.argv[1]
else:
	useimg = input("\nWrite input image file:\n")

try:
	img = Image.open(useimg)
	print("\nName:", useimg)
	print("Format:", img.format)
	print("Size:", img.size[0], "X", img.size[1])
	print("Colour model:", img.mode, "\n")
	img_rgb = img.convert('RGB')
	try:
		target = open(useimg + ".yiq", "wb")
		target.write("YIQ1".encode('utf-8'))
		target.write(pack('LL', img.size[0], img.size[1]))
		target.write("DATA".encode('utf-8'))
		pix = img_rgb.load()
		for y in range(0, img.size[1]):
			for x in range(0, img.size[0]):
				r, g, b = pix[x, y]
				r /= 255
				g /= 255
				b /= 255
				fY = r * 0.30 + g * 0.59 + b * 0.11
				fI = r * 0.599 - g * 0.2773 - b * 0.3217
				fQ = r * 0.213 - g * 0.5251 + b * 0.3121
				target.write(pack('bbb', round(fY*100), round(fI*100), round(fQ*100)))

		target.close()
	except:
		print("Can't create output file!")
except:
	print(useimg, ": image not found")
