"""
List of available methods of acquirement
1. time
2. date
3. cur_directory
4. roll_dice
"""
def time():
    from datetime import datetime
    # Chinese friendly coding
    时间=datetime.now().time() # time
    return int(str(时间).split(".")[1])

def date():
    from datetime import datetime as 日期获取神器
    # Chinese friendly coding mode activated
    # take that
    日期=日期获取神器.now().strftime('math.sqrt(%Y)+1%m**2-1%d/2;%H:%M:%S')
    import math
    return int(eval(日期.split(";")[0]))

def os_key():
    import os as 系统信息获取挂 # 实锤
    种子=1
    for 文件名 in 系统信息获取挂.listdir():
        for 字符 in 文件名:
            种子 *= ord(字符)
    return 种子

def roll_dice():
    # entirely random
    return 4
