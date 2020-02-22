import numpy as np
import cv2


# 定义颜色字典(分别为黑、黄、绿、红、白、蓝、橙)
color = {'Black': (0, 0, 0), 'U': (0, 255, 255), 'R': (0, 255, 0),'F': (0, 0, 255), 'D': (255, 255, 255),
         'L': (255, 0, 0), 'B': (0, 97, 255) }

# 定义六个面左上角坐标
points = ((320, 90), (540, 310), (320, 310), (320, 530), (100, 310), (760, 310))

#六个面的顺序
sides = ['U', 'R', 'F', 'D', 'L', 'B']

# 返回魔方六个面的展开图
def DrawSixSides(str_condition, String):

    # 黑色背景
    img = np.zeros((820, 1080, 3), np.uint8)

    # 框（由两个矩形，一条直线构成）
    cv2.rectangle(img, (310, 80), (530, 740), color['D'], 1)
    cv2.rectangle(img, (90, 300), (970, 520), color['D'], 1)
    cv2.line(img, (750, 300), (750, 520), color['D'], 1)

    #六个面
    i = 0        # i为condition_str下标
    for point in points:
        star_x, star_y = point
        y = star_y
        while y < 210 + star_y :
            x = star_x
            while x < 210 + star_x :
                cv2.rectangle(img, (x, y), (x + 60, y + 60), color[str_condition[i]], -1) #每个色块大小60*60
                x += 70                           #色块所占空间70*70
                i += 1
            y += 70

    font1 = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, 'U', (395, 210), font1, 2, color['Black'], 3, lineType = cv2.LINE_AA)
    cv2.putText(img, 'F', (402, 432), font1, 2, color['Black'], 3, lineType = cv2.LINE_AA)
    cv2.putText(img, 'D', (398, 652), font1, 2, color['Black'], 3, lineType = cv2.LINE_AA)
    cv2.putText(img, 'L', (180, 432), font1, 2, color['Black'], 3, lineType = cv2.LINE_AA)
    cv2.putText(img, 'R', (620, 432), font1, 2, color['Black'], 3, lineType = cv2.LINE_AA)
    cv2.putText(img, 'B', (840, 432), font1, 2, color['Black'], 3, lineType = cv2.LINE_AA)

    font2 = cv2.FONT_HERSHEY_COMPLEX_SMALL

    for i in range(6):
        cv2.putText(img, sides[i] + ': ' + str_condition[9 * i: 9 * (i + 1)], (560, 80 + 40*i), font2, 2,
                    (255, 255, 255), 2, lineType=cv2.LINE_AA)

    cv2.putText(img, String, (600, 600), font2, 2, (255, 255, 255), 2, lineType=cv2.LINE_AA)

    return img

#在窗口中打印图片
def showImg(img):
    cv2.namedWindow('Cube', cv2.WINDOW_NORMAL)
    cv2.imshow('Cube', img)
    cv2.waitKey()