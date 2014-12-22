"""
	RGB2YIQ: RGB to YIQ Pillow-based conversion program for Python 3.x
	Copyright (C) 2014	sm-programmer

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from PIL import Image
from struct import *
import sys

print("RGB2YIQ: RGB to YIQ Pillow-based conversion program for Python 3.x")
print("Copyright (C) 2014\tsm-programmer\n")

if len(sys.argv) == 1:
	print("This program is free software: you can redistribute it and/or modify")
	print("it under the terms of the GNU General Public License as published by")
	print("the Free Software Foundation, either version 3 of the License, or")
	print("(at your option) any later version.\n")
	print("This program is distributed in the hope that it will be useful,")
	print("but WITHOUT ANY WARRANTY; without even the implied warranty of")
	print("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the")
	print("GNU General Public License for more details.\n")
	print("You should have received a copy of the GNU General Public License")
	print("along with this program.  If not, see <http://www.gnu.org/licenses/>.\n")
	print("Usage:\n\tpython3 rgb2yiq <inimgfile>")
else:
	print("This program comes with ABSOLUTELY NO WARRANTY; for details type `rgb2yiq'.")
	print("This is free software, and you are welcome to redistribute it")
	print(" under certain conditions; type `rgb2yiq' for details.")
	useimg = sys.argv[1]

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
