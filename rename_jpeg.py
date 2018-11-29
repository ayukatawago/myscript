#! /usr/bin/env python3

from PIL import Image
import datetime
import glob
import os
import re

files = glob.glob('*')

for filename in files:
    name, ext = os.path.splitext(filename)
    if ext == ".JPG" or ext == ".jpg":
        print(filename)
        img = Image.open(filename)
        if img._getexif():
            t = None
            for key, value in img._getexif().items():
                if key == 36867:
                    t = datetime.datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
                if key == 271:
                    if "Sony" in value:
                        option = "Sony"
                    elif "NIKON" in value:
                        option = "Nikon"
                    else:
                        option = value
            if t == None:
                print("### skip rename for %s" % filename)
                continue

            newname = "%04d%02d%02d_%02d%02d%02d" % (t.year, t.month, t.day, t.hour, t.minute, t.second)
            name = newname
            i = 1
            while True:
                if os.path.exists(name + ".jpg"):
                    name = newname + "_" + str(i)
                    i += 1
                else:
                    print("rename as :" + name + ".jpg")
                    os.rename(filename, name + ".jpg")
                    break
        else:
            print("### skip rename for %s" % filename)
    elif ext == ".png":
        print(filename)
        img = Image.open(filename)
        newname = filename.replace(ext, ".jpg")
        img.save(newname)
