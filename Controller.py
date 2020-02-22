#返回新的状态
def Operate(str_condition, operate): #旧的状态和当前操作

    # #该面顺时针旋转90度
    if operate in {'U', 'R', 'F', 'D', 'L', 'B'}:
        str_condition = Clockwise_90(str_condition, operate)

    #该面逆时针旋转90度（相当于顺时针旋转270度）
    elif operate in {'U\'', 'R\'', 'F\'', 'D\'', 'L\'', 'B\''}:
        list = [x for x in operate]
        str_condition = Clockwise_90(str_condition, list[0])
        str_condition = Clockwise_90(str_condition, list[0])
        str_condition = Clockwise_90(str_condition, list[0])

    #该面顺时针旋转90度
    elif operate in {'U2', 'R2', 'F2', 'D2', 'L2', 'B2'}:
        list = [x for x in operate]
        str_condition = Clockwise_90(str_condition, list[0])
        str_condition = Clockwise_90(str_condition, list[0])

    return str_condition

# side顺时针旋转90度
def Clockwise_90 (str_condition, side):

    if side is 'U':
        str_condition = U_Clockwise_90(str_condition)
    elif side is 'R':
        str_condition = R_Clockwise_90(str_condition)
    elif side is 'F':
        str_condition = F_Clockwise_90(str_condition)
    elif side is 'D':
        str_condition = D_Clockwise_90(str_condition)
    elif side is 'L':
        str_condition = L_Clockwise_90(str_condition)
    elif side is 'B':
        str_condition = B_Clockwise_90(str_condition)

    return str_condition

# U面顺时针旋转90度
def U_Clockwise_90(str_condition):
    list = [x for x in str_condition] #转变成列表方便访问
    #对周围四个面造成的变化
    t1, t2, t3 = list[9], list[10], list[11]
    list[9], list[10], list[11] = list[45], list[46], list[47]
    list[45], list[46], list[47] = list[36], list[37], list[38]
    list[36], list[37], list[38] = list[18], list[19], list[20]
    list[18], list[19], list[20] = t1, t2, t3
    # 当前面的变化
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = list[0: 9]
    list[0] = t7
    list[1] = t4
    list[2] = t1
    list[3] = t8
    list[5] = t2
    list[6] = t9
    list[7] = t6
    list[8] = t3
    str_condition = ''.join(list) #变回字符串

    return str_condition

# R面顺时针旋转90度
def R_Clockwise_90(str_condition):
    list = [x for x in str_condition] #转变成列表方便访问
    #对周围四个面造成的变化
    t1, t2, t3 = list[2], list[5], list[8]
    list[2], list[5], list[8] = list[20], list[23], list[26]
    list[20], list[23], list[26] = list[29], list[32], list[35]
    list[29], list[32], list[35] = list[51], list[48], list[45]
    list[51], list[48], list[45] = t1, t2, t3
    # 当前面的变化
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = list[9: 18]
    list[9] = t7
    list[10] = t4
    list[11] = t1
    list[12] = t8
    list[14] = t2
    list[15] = t9
    list[16] = t6
    list[17] = t3
    str_condition = ''.join(list) #变回字符串

    return str_condition

# F面顺时针旋转90度
def F_Clockwise_90(str_condition):
    list = [x for x in str_condition] #转变成列表方便访问
    #对周围四个面造成的变化
    t1, t2, t3 = list[38], list[41], list[44]
    list[38], list[41], list[44] = list[27], list[28], list[29]
    list[27], list[28], list[29] = list[15], list[12], list[9]
    list[9], list[12], list[15] = list[6], list[7], list[8]
    list[6], list[7], list[8] = t3, t2, t1
    # 当前面的变化
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = list[18: 27]
    list[18] = t7
    list[19] = t4
    list[20] = t1
    list[21] = t8
    list[23] = t2
    list[24] = t9
    list[25] = t6
    list[26] = t3
    str_condition = ''.join(list) #变回字符串

    return str_condition

# D面顺时针旋转90度
def D_Clockwise_90(str_condition):
    list = [x for x in str_condition] #转变成列表方便访问
    #对周围四个面造成的变化
    t1, t2, t3 = list[15], list[16], list[17]
    list[15], list[16], list[17] = list[24], list[25], list[26]
    list[24], list[25], list[26] = list[42], list[43], list[44]
    list[42], list[43], list[44] = list[51], list[52], list[53]
    list[51], list[52], list[53] = t1, t2, t3
    # 当前面的变化
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = list[27: 36]
    list[27] = t7
    list[28] = t4
    list[29] = t1
    list[30] = t8
    list[32] = t2
    list[33] = t9
    list[34] = t6
    list[35] = t3
    str_condition = ''.join(list) #变回字符串

    return str_condition

# L面顺时针旋转90度
def L_Clockwise_90(str_condition):
    list = [x for x in str_condition] #转变成列表方便访问
    #对周围四个面造成的变化
    t1, t2, t3 = list[0], list[3], list[6]
    list[0], list[3], list[6] = list[53], list[50], list[47]
    list[53], list[50], list[47] = list[27], list[30], list[33]
    list[27], list[30], list[33] = list[18], list[21], list[24]
    list[18], list[21], list[24] = t1, t2, t3
    # 当前面的变化
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = list[36: 45]
    list[36] = t7
    list[37] = t4
    list[38] = t1
    list[39] = t8
    list[41] = t2
    list[42] = t9
    list[43] = t6
    list[44] = t3
    str_condition = ''.join(list) #变回字符串

    return str_condition

# B面顺时针旋转90度
def B_Clockwise_90(str_condition):
    list = [x for x in str_condition] #转变成列表方便访问
    #对周围四个面造成的变化
    t1, t2, t3 = list[0], list[1], list[2]
    list[0], list[1], list[2] = list[11], list[14], list[17]
    list[11], list[14], list[17] = list[35], list[34], list[33]
    list[35], list[34], list[33] = list[42], list[39], list[36]
    list[42], list[39], list[36] = t1, t2, t3
    # 当前面的变化
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = list[45: 54]
    list[45] = t7
    list[46] = t4
    list[47] = t1
    list[48] = t8
    list[50] = t2
    list[51] = t9
    list[52] = t6
    list[53] = t3
    str_condition = ''.join(list) # 变回字符串

    return str_condition
