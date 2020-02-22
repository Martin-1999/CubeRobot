import cv2
import numpy as np

imgs = []
kernel = np.ones((5, 5), np.uint8)
pts = np.float32([[0, 0], [270, 0], [0, 270], [270, 270]])

# 图像预处理
def imgInit(img):
    img = cv2.medianBlur(img, 5)
    mask = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    mask = cv2.erode(mask, kernel, iterations=1)
    return mask


# 对第一张图进行透视变换
def trans_URF(Cube_URF):
    # 原图中卡片分别在左上、右上、左下、右下四个角点
    pts1 = np.float32([[130, 1], [262, 40], [3, 34], [136, 87]])  # U
    pts2 = np.float32([[136, 87], [262, 40], [132, 262], [244, 195]])  # R
    pts3 = np.float32([[3, 34], [136, 87], [12, 195], [132, 262]])  # F

    # 生成透视变换矩阵
    M1 = cv2.getPerspectiveTransform(pts1, pts)
    M2 = cv2.getPerspectiveTransform(pts2, pts)
    M3 = cv2.getPerspectiveTransform(pts3, pts)
    # 进行透视变换，参数3是目标图像大小
    Cube_U = cv2.warpPerspective(Cube_URF, M1, (270, 270))
    Cube_R = cv2.warpPerspective(Cube_URF, M2, (270, 270))
    Cube_F = cv2.warpPerspective(Cube_URF, M3, (270, 270))

    Blur_U = imgInit(Cube_U)
    Blur_R = imgInit(Cube_R)
    Blur_F = imgInit(Cube_F)

    cv2.imwrite('Blur_U.jpg', Blur_U)
    cv2.imwrite('Blur_R.jpg', Blur_R)
    cv2.imwrite('Blur_F.jpg', Blur_F)

    return Blur_U, Blur_R, Blur_F


# 对第二张图进行透视变换
def trans_DLB(Cube_DLB):
    # 原图中卡片分别在左上、右上、左下、右下四个角点
    pts1 = np.float32([[3, 34], [130, 1], [136, 87], [262, 40]])  # D
    pts2 = np.float32([[132, 262], [12, 195], [136, 87], [3, 34]])  # L
    pts3 = np.float32([[244, 195], [132, 262], [262, 40], [136, 87]])  # B

    # 生成透视变换矩阵
    M1 = cv2.getPerspectiveTransform(pts1, pts)
    M2 = cv2.getPerspectiveTransform(pts2, pts)
    M3 = cv2.getPerspectiveTransform(pts3, pts)
    # 进行透视变换，参数3是目标图像大小
    Cube_D = cv2.warpPerspective(Cube_DLB, M1, (270, 270))
    Cube_L = cv2.warpPerspective(Cube_DLB, M2, (270, 270))
    Cube_B = cv2.warpPerspective(Cube_DLB, M3, (270, 270))

    Blur_D = imgInit(Cube_D)
    Blur_L = imgInit(Cube_L)
    Blur_B = imgInit(Cube_B)

    cv2.imwrite('Blur_D.jpg', Blur_D)
    cv2.imwrite('Blur_L.jpg', Blur_L)
    cv2.imwrite('Blur_B.jpg', Blur_B)

    return Blur_D, Blur_L, Blur_B


#两张顶角图还原成六张图
def Two2Six(Cube_URF, Cube_DLB):
    Cube_URF = cv2.resize(Cube_URF, (270, 270))
    Cube_DLB = cv2.resize(Cube_DLB, (270, 270))
    Blur_U, Blur_R, Blur_F = trans_URF(Cube_URF)
    Blur_D, Blur_L, Blur_B = trans_DLB(Cube_DLB)
    imgs= [Blur_U, Blur_R, Blur_F, Blur_D, Blur_L, Blur_B]
    return imgs