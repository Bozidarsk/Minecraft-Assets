# How does it work?

## Make a .png file for every char
Combine ascii and enchantment language chars into one .png file. (with photoshop) <br>
This new file contains every char with a size of 8x8 pixels. <br>
Extract all chars individually and save each one separately. (make an 8x8 png for every char, with python) <br>
Because not every char is 8x8 it contains empy rows and/or columns, so you have to trim them. (with python) <br>

## Make a .svg file for every char
From [here](https://pixelied.com/convert/png-converter/png-to-svg) you can convert all png files to svg. <br>
But after this conversion it is still a bitmap. <br>
You can use a program like Inkscape to fix that. <br>
Using Inkscape:
- press Ctrl+A (to select the bitmap)
- press Alt+Shift+B (to open 'Trace Bitmap' window)
- select the 'Pixel art' mode
- click 'Apply'
- press Ctrl+S (to save it)

And repeat for every char.

## Make the .ttf file
Before you do this you will need to add an extra column after every svg, because when you start typing every char will be next to the previous one. <br>
To add this extra padding you can directly modify the .svg file (which is just xml) - increment the width attribute of &lt;svg&gt;.<br>
After that you can use [this](https://icomoon.io/app/#/select) to make a font from your svgs, but make sure that every char corresponds to its hex code.