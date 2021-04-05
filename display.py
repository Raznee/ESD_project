import colorsys
import time
from sys import exit

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

import unicornhathd


#rpi hosts the webserver

def static_text(TEXT, SIZE, text_x = 0):
    FONT = ('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', SIZE)

    width, height = unicornhathd.get_shape()

    #misc parameters
    unicornhathd.rotation(0)
    unicornhathd.brightness(0.5)
    #text_x = 0
    text_y = 0

    font_file, font_size = FONT
    font = ImageFont.truetype(font_file, font_size)
    text_width, text_height = font.getsize(TEXT)

    text_width += width + text_x
    image = Image.new('RGB', (text_width, max(height, text_height)), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.text((text_x, text_y), TEXT, fill=(255, 255, 255), font=font)
    scroll = 0
    #scroll in range(text_width - width)
    for x in range(width):

        hue = (x + scroll) / float(text_width)

        br, bg, bb = [int(n * 255) for n in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]

        for y in range(height):

            pixel = image.getpixel((x + scroll, y))

            r, g, b = [float(n / 255.0) for n in pixel]

            r = int(br * r)
            g = int(bg * g)
            b = int(bb * b)
            s = int((r+g+b)/3)
            r = g = b = s
            unicornhathd.set_pixel(width - 1 - x, y, r, g, b)

    unicornhathd.show()

def scrolling_text(TEXT, SIZE, SCROLLING_SPEED = 0.05):
    FONT = ('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', SIZE)

    width, height = unicornhathd.get_shape()

    #misc parameters
    unicornhathd.rotation(0)
    unicornhathd.brightness(0.5)
    text_x = 0
    text_y = 0

    font_file, font_size = FONT
    font = ImageFont.truetype(font_file, font_size)
    text_width, text_height = font.getsize(TEXT)

    text_width += width + text_x
    image = Image.new('RGB', (text_width, max(height, text_height)), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.text((text_x, text_y), TEXT, fill=(255, 255, 255), font=font)

    for scroll in range(text_width - width):
        for x in range(width):

            hue = (x + scroll) / float(text_width)

            br, bg, bb = [int(n * 255) for n in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]

            for y in range(height):

                pixel = image.getpixel((x + scroll, y))

                r, g, b = [float(n / 255.0) for n in pixel]

                r = int(br * r)
                g = int(bg * g)
                b = int(bb * b)
                s = int((r+g+b)/3)
                r = g = b = s
                unicornhathd.set_pixel(width - 1 - x, y, r, g, b)

        unicornhathd.show()

        time.sleep(SCROLLING_SPEED)
"""        
while 1:
    #scrolling_text("lel", 16)
    for i in range(100):
        if i <10:
            a = 7
        else:
            a = 0
        static_text(str(i), 14, a)
        time.sleep(1)
unicornhathd.off()
"""