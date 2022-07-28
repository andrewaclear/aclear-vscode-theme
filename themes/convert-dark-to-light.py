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
      if red < 0x41 or green < 0x41 or blue < 0x41:
        red += 0xbb
        if red > 0xff: red = 0xff
        green += 0xbb
        if green > 0xff: green = 0xff
        blue += 0xbb
        if blue > 0xff: blue = 0xff
      elif red > 0xd8 or green > 0xd8 or blue > 0xd8:
        red -= 0x30
        # if red > 0xff: red = 0xff
        green -= 0x30
        # if green > 0xff: green = 0xff
        blue -= 0x30
        # if blue > 0xff: blue = 0xff
      parts[i] = '#' + hex(red)[2:4] + hex(green)[2:4] + hex(blue)[2:4] + parts[i][7:]
  line = '"'.join(parts)
  light.write(line)