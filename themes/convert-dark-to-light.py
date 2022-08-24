# Convert dark theme to light
# Copywrite: Andrew D'Amario, August 2022 

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
      if (red < 0x41 and green < 0x41) or (green < 0x41 and blue < 0x41) or (red < 0x41 and blue < 0x41):
        inc = 0xb0
        red += inc
        if red > 0xff: red = 0xff
        green += inc
        if green > 0xff: green = 0xff
        blue += inc
        if blue > 0xff: blue = 0xff
      elif red > 0x99 and green > 0x99 and blue > 0x99:
        dec = min(red, green, blue) - 0x44
        red -= dec
        # if red > 0xff: red = 0xff
        green -= dec
        # if green > 0xff: green = 0xff
        blue -= dec
        # if blue > 0xff: blue = 0xff
      elif red > 0xd8 or green > 0xd8 or blue > 0xd8:
        dec = 0x31
        red -= dec
        # if red > 0xff: red = 0xff
        green -= dec
        # if green > 0xff: green = 0xff
        blue -= dec
        # if blue > 0xff: blue = 0xff
      parts[i] = '#' + ('0' + hex(red)[2:4])[-2:] + ('0' + hex(green)[2:4])[-2:] + ('0' + hex(blue)[2:4])[-2:] + parts[i][7:]
  line = '"'.join(parts)
  light.write(line)
