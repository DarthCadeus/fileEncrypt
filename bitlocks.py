# -*- coding: utf-8 -*-

import seedAcquire
import math
# import support_lib

"""
what to solve
more efficient communication protocols
for example, FTP seems a good target
Let us concentrate on encryption of it
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

# def closeRatio(l1, l2, rat):
#     # O(n^2)... Sorry
#     cur_closest = 100000  # max
#     l1_close_index = 0
#     l2_close_index = 0
#     outer = 1
#     for i in range(0, len(l1)):
#         for j in range(0, len(l2)):
#             if (abs(float(l1[i])/float(l2[j]) - rat) < float(cur_closest)):
#                 cur_closest = abs(float(l1[i])/float(l2[j]) - rat)
#                 l1_close_index = i
#                 l2_close_index = j
#                 outer = 1
#             if(abs(float(l2[j])/float(l1[i]) - rat) < float(cur_closest)):
#                 cur_closest = abs(float(l2[j])/(l1[i]) - rat)
#                 l1_close_index = i
#                 l2_close_index = j
#                 outer = 2
#     return {
#     "closest": cur_closest,
#     "indices": [l1_close_index, l2_close_index],
#     "originals": [l1, l2],
#     "numbers": [l1[l1_close_index], l2[l2_close_index]],
#     "reference": outer
#     }

def 大小获取神器(length):
    return math.ceil(math.sqrt(length))

def encodePlain(name, colorbase="red"):
    f = open("demo.txt", "r")
    生的 = f.read()
    熟的 = ""
    随机数获取神器返回 = random(len(生的))
    from PIL import Image
    大小 = 大小获取神器(len(随机数获取神器返回))
    img = Image.new('RGB', (大小, 大小))
    图片数据 = []
    for i in 随机数获取神器返回:
        if colorbase == 'red':
            像素 = (int(i)*25, 0, 0)
        elif colorbase == "blue":
            像素 = (0, 0, int(i)*25)
        elif colorbase == "green":
            像素 = (0, int(i)*25, 0)
        图片数据.append(像素)
    img.putdata(图片数据)
    img.save('code.png')
    # 字母表神器 = support_lib.Alphabet()
    for 叶片位置 in range(0, len(生的)):
        叶片 = 生的[叶片位置]
        # 熟的 += 字母表神器.shift(随机数生成神器返回[叶片位置], 叶片)
        熟的 += chr(ord(叶片) + int(随机数获取神器返回[叶片位置]))
    return 熟的
    f.close()
print(encodePlain("demo.txt"))
