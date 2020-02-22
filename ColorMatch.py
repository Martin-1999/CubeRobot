#一张图的颜色序列
def getOneCondition(img):
    s=''
    y=45
    while y <270:
        x=45
        while x < 270:
            b, g, r = img[y, x]
            # #每个色块的 b,g,r
            # print(tellColor(b, g, r))
            # print(b, g, r)
            s += tellColor(b, g, r)
            x += 90
        y+=90
    return s


# 六张图的颜色序列
def getSixCondition(imgs):
    str_condition = ''
    for img in imgs:
        s =getOneCondition(img)
        str_condition += s
    return str_condition


# 根据图像r/g/b分辨颜色
def tellColor(b, g, r):
    if abs(int(b) - int(g)) < 20 and abs(int(b) - int(r)) < 20 and abs(int(g) - int(r)) < 20:
        return 'D'
    elif g > b and g > r:
        if r < 85:
            return 'R'
        else:
            return 'U'
    elif b > g and b > r:
        return 'L'
    elif abs(int(b) - int(g)) < 20 :
        return 'F'
    else:
        return 'B'