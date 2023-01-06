import time
import os
import random
from PIL import Image, ImageDraw

hidden = "Hidden.png"
source_A = "A.png"
source_B = "B.png"

# patterns (format: hidden image pixel (b/w), source a pixel (b/w)1, source b pixel (b/w)2)
# values go top left, top right, bottom left, bottom right (2x2)
bb1b2 = (((1,0,0,0),(0,1,0,0)), ((0,1,0,0),(1,0,0,0)), ((0,0,0,1),(0,0,1,0)), ((0,0,1,0),(0,0,0,1)))
bb1w2 = (((0,1,0,0),(1,0,1,0)), ((1,0,0,0),(0,1,0,1)), ((0,0,0,1),(0,1,1,0)), ((0,1,0,0),(1,0,0,1)))
bw1b2 = (((0,1,1,0), (0,0,0,1)), ((1,0,0,1), (0,1,0,0)))
bw1w2 = (((0,1,1,0), (1,0,0,1)), ((1,0,0,1), (0,1,1,0)), ((1,0,1,0), (0,1,0,1)), ((0,1,0,1), (1,0,1,0)))

wb1b2 = (((0,0,1,0), (0,0,1,0)), ((0,0,0,1), (0,0,0,1)))
wb1w2 = (((0,0,1,0), (0,1,1,0)), ((0,0,0,1), (1,0,0,1)))
ww1b2 = (((0,1,1,0), (0,0,1,0)), ((1,0,0,1), (0,0,0,1)))
ww1w2 = (((0,1,1,0), (1,0,1,0)), ((1,0,0,1), (0,1,0,1)), ((0,1,0,1), (1,0,0,1)), ((1,0,1,0), (0,1,1,0)))

with Image.open(hidden) as img:
  jpg_img = img.convert("1")
  jpg_img.save("hidden.png", quality=95)
  
with Image.open(source_A) as img:
  jpg_img = img.convert("1")
  jpg_img.save("source_A.png", quality=95)
  
with Image.open(source_B) as img:
  jpg_img = img.convert("1")
  jpg_img.save("source_B.png", quality=95)

old_A = Image.open("source_A.png")
old_B = Image.open("source_B.png")
old_hd = Image.open("hidden.png")

# A = old_A.crop((225, 175, 475, 475))
A = old_A

width, height = A.size
B = old_B.crop((0, 0, width, height))
hd = old_hd.crop((0, 0, width, height))

print(A.size[0], " ", A.size[1])
print(B.size[0], " ", B.size[1])
print(hd.size[0], " ", hd.size[1])
time.sleep(3)

print(f"{width * 2}x{height * 2}")

out_img_A = Image.new("1", (width * 2, height * 2))
out_img_B = Image.new("1", (width * 2, height * 2))
draw_A = ImageDraw.Draw(out_img_A)
draw_B = ImageDraw.Draw(out_img_B)

for x in range(0, width):
  for y in range(0, height):
    A_pxl = A.getpixel((x, y))
    hd_pxl = hd.getpixel((x, y))
    if (x+5>=B.size[0] or y+10>=B.size[1]):
      B_pxl = B.getpixel((width-1, height-1))
    else:
      B_pxl = B.getpixel((x+5, y+10))

    pat = ()

    if (hd_pxl == 0):
      if (A_pxl == 0):
        if (B_pxl == 0):
          pat = bb1b2
        elif (B_pxl == 255):
          pat = bb1w2
      elif (A_pxl == 255):
        if (B_pxl == 0):
          pat = bw1b2
        elif (B_pxl == 255):
          pat = bw1w2
    elif (hd_pxl == 255):
      if (A_pxl == 0):
        if (B_pxl == 0):
          pat = wb1b2
        elif (B_pxl == 255):
          pat = wb1w2
      elif (A_pxl == 255):
        if (B_pxl == 0):
          pat = ww1b2
        elif (B_pxl == 255):
          pat = ww1w2

    pat = random.choice(pat)
    A_pat = pat[0]
    B_pat = pat[1]
    
    print(A_pat, "  ", B_pat, x, " ", y, " ", A_pxl, " ", B_pxl, " ", hd_pxl, end="\n")
    
    draw_A.point((x*2, y*2), A_pat[0])
    draw_A.point((x*2+1, y*2), A_pat[1])
    draw_A.point((x*2, y*2+1), A_pat[2])
    draw_A.point((x*2+1, y*2+1), A_pat[3])
    
    draw_B.point((x*2, y*2), B_pat[0])
    draw_B.point((x*2+1, y*2), B_pat[1])
    draw_B.point((x*2, y*2+1), B_pat[2])
    draw_B.point((x*2+1, y*2+1), B_pat[3])

    #time.sleep(0.1)

out_img_A.save("A.png")
out_img_B.save("B.png")