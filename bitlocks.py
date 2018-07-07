# -*- coding: utf-8 -*-

import seedAcquire
import math
# import support_lib

"""
Data Encyrption + Image generator
Yeah!
"""

def random(length):
    seed = seedAcquire.time()
    rands = ""
    while len(rands) < length:
        rands += str(seed)
        n = str(seed ** 2)
        seed = int(n[1:len(n)-1])
    return rands

def factor(num):
    f = []
    for i in range(1, int(math.sqrt(num))):
        if num % i == 0:
            f.append(i)
    return f

def get_size(length):
    return math.ceil(math.sqrt(length))

def encodePlain(name, colorbase="red"):
    f = open("demo.txt", "r")
    raw = f.read()
    processed = ""
    rand_res = random(len(raw))
    from PIL import Image
    size = get_size(len(rand_res))
    img = Image.new('RGB', (size, size))
    img_dat = []
    for i in rand_res:
        if colorbase == 'red':
            pixel = (int(i)*25, 0, 0)
        elif colorbase == "blue":
            pixel = (0, 0, int(i)*25)
        elif colorbase == "green":
            pixel = (0, int(i)*25, 0)
        img_dat.append(pixel)
    img.putdata(img_dat)
    img.save('code.png')
    for i in range(0, len(raw)):
        itm = raw[i]
        processed += chr(ord(itm) + int(rand_res[i]))
    return processed
    f.close()
print(encodePlain("demo.txt"))
