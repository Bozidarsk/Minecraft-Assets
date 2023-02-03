from PIL import Image

i = 0
size = 48
srcImage = Image.open("src.png")
srcPixels = srcImage.load()

def SaveIcon(startX, startY):
	dstImg = Image.open("48x48.png")
	dstPixels = dstImg.load()
	global i
	x = 0
	y = 0

	while (y < size):
		x = 0
		while (x < size):
			if (srcPixels[x + startX, y + startY] == (139, 139, 139, 255)):
				dstPixels[x, y] = (0, 0, 0, 0)
			else:
				dstPixels[x, y] = srcPixels[x + startX, y + startY]
			x += 1
		y += 1

	dstImg.save("dst\\" + str(i) + ".png")
	i += 1

def main():
	x = 0
	y = 0
	while (y < srcImage.height):
		x = 0
		while (x < srcImage.width):
			SaveIcon(x, y)
			x += size + 6
		y += size + 6

main()