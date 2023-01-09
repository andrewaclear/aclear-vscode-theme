# Convert dark theme to light
# by Andrew D'Amario, © August 2022 

from statistics import mean, median
from sys import stderr


darkFilename = "aclear-dark.json"
lightFilename = "aclear-light.json"

dark = open(darkFilename, "r")
light = open(lightFilename, "w")

for line in dark:
  parts = line.split('"')
  # print(parts)
  for i in range(len(parts)):
    if len(parts[i]) > 0 and parts[i][0] == '#' and parts[i][7:] == '':
      red = int(parts[i][1:3], 16)
      green = int(parts[i][3:5], 16)
      blue = int(parts[i][5:7], 16)
      
      s = red + green + blue
      k = [red, green, blue]
      m = int(median(k))
      max_diff = max(k)-min(k)
      diff = abs((-m)%0xff-m)
      if (s > 0x55*3):
        if (max_diff > 0x22):
          # colours
          diff = 0x2e
        else:
          # whites, greys -> black
          diff = int(diff/1.2)
        red = max(red-diff, 0x00)
        green = max(green-diff, 0x00)
        blue = max(blue-diff, 0x00)        
      else:
        # blacks -> whites, greys
        red = min(red+diff, 0xf0)
        green = min(green+diff, 0xf0)
        blue = min(blue+diff, 0xf0)

      parts[i] = '#' + ('0' + hex(red)[2:4])[-2:] + ('0' + hex(green)[2:4])[-2:] + ('0' + hex(blue)[2:4])[-2:] + parts[i][7:]
  line = '"'.join(parts)
  light.write(line)
