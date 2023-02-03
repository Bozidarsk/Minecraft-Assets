from PIL import Image

img = Image.open("font.png")
pixels = img.load()

def SaveChar(x, y, c):
    _x = 0
    _y = 0
    char = Image.new("RGBA", (8, 8))

    while (_y < 8):
        _x = 0
        while (_x < 8):
            char.putpixel((_x, _y), pixels[x + _x, y + _y])
            _x += 1
        _y += 1
    char.save(hex(c) + ".png")

def main():
    x = 0
    y = 0
    c = 0x20
    while (y < 8 * 8):
        x = 0
        while (x < 8 * 16):
            SaveChar(x, y, c)
            c += 1
            x += 8
        y += 8

main()
