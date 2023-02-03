from PIL import Image

def TrimHorizontal(inputFile, outputFile, width, height):
    try:
        img = Image.open(inputFile)
    except:
        print("File not found - '" + inputFile + "'.")
        return

    pixels = img.load()
    start = -1
    end = -1

    for x in range(0, width):
        if (start != -1):
            break
        for y in range(0, height):
            if (pixels[x, y] != (0, 0, 0, 0)):
                start = x
                break

    x = width - 1
    while (x >= 0):
        if (end != -1):
            break
        for y in range(0, height):
            if (pixels[x, y] != (0, 0, 0, 0)):
                end = x
                break
        x -= 1

    if (end - start + 1 == width):
    	print("Width is the same - '" + inputFile + "'.")
    img.crop((start, 0, end - start + 1, height)).save(outputFile)

def main():
    for c in range(0x20, 0x99 + 1):
        file = hex(c) + ".png"
        TrimHorizontal("..\\" + file, file, 8, 8)

main()
TrimHorizontal("..\\" + "0xb8.png", "0xb8.png", 8, 8)
TrimHorizontal("..\\" + "0xb9.png", "0xb9.png", 8, 8)