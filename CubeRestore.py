import cv2
import sys
import CubeExpansion
import Controller
import CubeSolve
import CubeTrans
import ColorMatch

# 读入两张顶角图片
Cube_URF = cv2.imread('Cube_URF.jpg')
Cube_DLB = cv2.imread('Cube_DLB.jpg')

# 两张图还原成六个面
imgs = CubeTrans.Two2Six(Cube_URF, Cube_DLB)

# 初始状态str_condition = 'RLRUUDFDUFBUBRLUBFDFLRFRLLRDFBUDLLFDBFLRLDUBBFUDDBURRB'

str_condition = ColorMatch.getSixCondition(imgs)

# 魔方已经处于还原状态
if str_condition is None:
    print('魔方已处于还原状态')
    sys.exit(0)
print(str_condition)

# 操作序列
ops = CubeSolve.CubeSolve(str_condition)

for op in ops:
    img = CubeExpansion.DrawSixSides(str_condition, 'Next Step : ' + op)
    CubeExpansion.showImg(img)
    str_condition = Controller.Operate(str_condition, op)

img = CubeExpansion.DrawSixSides(str_condition, 'Good job!!')
CubeExpansion.showImg(img)
print('还原成功')
sys.exit(0)