#!/usr/bin/env python

# Ported from:
# https://github.com/adafruit/Adafruit_Python_SSD1306/blob/master/examples/shapes.py

from ssd1306.oled.device import ssd1306, sh1106
from ssd1306.oled.render import canvas
from PIL import ImageFont
from time import sleep
import sys

device = ssd1306(port=1, address=0x3C)

def draw4symbols(text):
    if len(text) != 4:
        print("draw4symbols not used correcty")
    with canvas(device) as draw:
        padding = 2
        shape_width = 20
        top = padding
        bottom = device.height - padding - 1
        x = padding
        # Alternatively load a TTF font.
        # Some other nice fonts to try: http://www.dafont.com/bitmap.php
        font = ImageFont.truetype('Perfect DOS VGA 437.ttf', 55)
        draw.text((x, top),  text,  font=font, fill=255)

draw4symbols(str(sys.argv)[0])

