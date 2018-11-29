#! /usr/bin/env python3
import os
import re


def check_format1(file):
        pattern = r"([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)-(.+).jpg"
        match = re.compile(pattern).match(file)
        if match:
                new = match.group(1) + match.group(2) + match.group(3) + "_" + match.group(4) + ".jpg"
                print("rename " + file + " -> " + new)
                os.rename(file, new)
                return True
        else:
                return False


files = os.listdir(".")

for f in files:
        if (os.path.isdir(f)):
                continue
        if not check_format1(f):
                print("## skip " + f)
