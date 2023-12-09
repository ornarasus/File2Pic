from PIL import Image, ImageDraw
import os
import math
import argparse

parser = argparse.ArgumentParser(description='Encoding file (up to 2.5 GB) to picture')
parser.add_argument('file_path', type=str, help="Absolute/relative path to the file")
parser.add_argument('picture_name', type=str, help="ONLY picture's name")
parser.add_argument('-d','--decode', action='store_true', help='decoding file from picture')
args = parser.parse_args()

def encode():
    im = Image.new('RGBA', (1280, 720), (0, 0, 0, 0))
    size = os.path.getsize(args.file_path)
    f = open(args.file_path, "rb").read()
    draw = ImageDraw.Draw(im)
    for i in range(math.ceil(size/3)):
        x = i%1280
        y = i//1280
        g = f[i*3+1] if len(f) > i*3+1 else 0
        b = f[i*3+2] if len(f) > i*3+2 else 0
        draw.point((x, y), (f[i*3], g, b, 255))
    im.save(args.picture_name+".png", quality=100)

def decode():
    im = Image.open(args.picture_name+".png")
    size = im.size[0]*im.size[1]
    f = open(args.file_path, "wb")
    for i in range(size):
        x = i%im.size[0]
        y = i//im.size[0]
        if im.getpixel((x, y)) == (0, 0, 0, 0):
            break
        f.write(bytes(im.getpixel((x, y))[0:3]))
    f.close()

if args.decode:
    decode()
else:
    encode()
