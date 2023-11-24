#!/usr/bin/env python
fontsize = 22


import socket
myip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

from gpiozero import CPUTemperature
cpu = CPUTemperature()
temp = cpu.temperature

from inky import InkyPHAT

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.RED)

from PIL import Image, ImageFont, ImageDraw

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne

font = ImageFont.truetype(FredokaOne, fontsize)

# message = "Hello, World!"
import time
message1 = datetime = time.strftime("%-d.%-m. %-H:%M")
message2 = "IP: " + myip
message3 = "CPU temp: " + str(round(temp,1)) + " °C"

print (message1)
print (message2)
print (message3)

draw.text((10, 0), message1, inky_display.BLACK, font)
draw.text((10, fontsize), message2, inky_display.RED, font)
draw.text((10, fontsize*2), message3, inky_display.RED, font)

inky_display.set_image(img)
inky_display.show()

