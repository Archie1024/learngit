# print("开始")
# def get_sum(start,end,step=1):
#     """这就是那个让你没有面试机会的傻逼代码"""
#     zhonghe = 0
#     while start <= end:
#         zhonghe += start
#         start += step
#     print(zhonghe)
# print("结束啦")



#把这坨大便一样的围棋demo放到这里吧

#-----------------------------------一个围棋有关的demo--------------------------------------------------
# import copy
# def checkline(pts):
#     """把list按照下标单双分为两个新list，也就是分为红黑两方的子"""
#     for one in pts:
#         # print(pts.index(one))
#         if pts.index(one)%2 == 1:
#             redp_list.append(one)
#         else:
#             blap_list.append(one)
#
# def qiefen_panduan(A):
#     """切分组合坐标字符串并判断是否存在"""
#     # 判断棋子横坐标是否在棋盘中存在直线
#     realA = copy.deepcopy(A)
#     AA = copy.deepcopy(A)
#     action = len(AA)
#     while action >= 3:
#         p_count = 3
#         san = ""
#         for one in AA:
#             if len(one) == 3:
#                 linshi = one[-2:]
#             else:
#                 linshi = one[-1]
#             san += linshi
#             p_count -= 1
#             if p_count == 0:
#                 break
#         action -= 1
#         del AA[0]
#         print(san)
#         if san in abscissa or abscissa_desc:
#             print("连成一条直线，直线横坐标是{}".format(san))
#
#     # 判断红字纵坐标是否在旗盘中存在直线
#     action2 = len(realA)
#     # print(len(BB))
#     while action2 >=3:
#         p_count2 = 3
#         san2 = ""
#         for one in realA:
#             linshi2 = one[0]
#             san2 += linshi2
#             p_count2 -=1
#             if p_count2 == 0:
#                 break
#         action2 -= 1
#         del realA[0]
#         print(san2)
#         if san2 in abscissa:
#             print("连成一条直线，直线纵坐标是{}".format(san2))
#
# abscissa = "12345678910111213141516171819"
# abscissa_desc = "19181716151413121110987654321"
# ordinate = "ABCDEFGHJKLMNOPQRST"
# ordinate_desc = ordinate[::-1]
# print(ordinate_desc)
# luozhi = ["Q16","D4","Q4","D16","F3","C6","F17","R17","Q17","R16","R14","R15","Q15"]
# redp_list = []  #红字坐标['D4', 'D16', 'C6', 'R17', 'R16', 'R15']
# blap_list = []  #黑子坐标['Q16', 'Q4', 'F3', 'F17', 'Q17', 'R14', 'Q15']
# checkline(luozhi)
# # print(type(redp_list),redp_list)
# # print(type(blap_list),blap_list)
# qiefen_panduan(redp_list)
# qiefen_panduan(blap_list)

#-------------------------------------这个是差不多的逻辑啦，这个差一点啦---------------------------------
# def checkline(pts):
#     """把list按照下标单双分为两个新list，也就是分为红黑两方的子"""
#     for one in pts:
#         # print(pts.index(one))
#         if pts.index(one)%2 == 1:
#             redp_list.append(one)
#         else:
#             blap_list.append(one)
#
# def qiefen_panduan(A):
#     """切分组合坐标字符串并判断是否存在"""
#     # 判断棋子横坐标是否在棋盘中存在直线
#     realA = A
#     AA = A
#     action = len(AA)
#     while action >= 3:
#         p_count = 3
#         san = ""
#         for one in A:
#             if len(one) == 3:
#                 linshi = one[-2:]
#             else:
#                 linshi = one[-1]
#             san += linshi
#             p_count -= 1
#             if p_count == 0:
#                 break
#         action -= 1
#         del AA[0]
#         print(san)
#         if san in abscissa:
#             print("红字连成一条直线，直线横坐标是{}".format(san))
#
#     # 判断红字纵坐标是否在旗盘中存在直线
#     BB = realA
#     print(realA)
#     action2 = len(BB)
#     # print(len(BB))
#     while action2 >=3:
#         p_count2 = 3
#         san2 = ""
#         for one in A:
#             linshi2 = one[0]
#             san2 += linshi2
#             p_count2 -=1
#             if p_count2 == 0:
#                 break
#         action2 -= 1
#         del BB[0]
#         print(san2)
#         if san2 in abscissa:
#             print("红子连成一条直线，直线纵坐标是{}".format(san2))
#
# abscissa = "12345678910111213141516171819"
# ordinate = "ABCDEFGHJKLMNOPQRST"
# luozhi = ["Q16","D4","Q4","D16","F3","C6","F17","R17","Q17","R16","R14","R15","Q15"]
# redp_list = []  #红字坐标['D4', 'D16', 'C6', 'R17', 'R16', 'R15']
# blap_list = []  #黑子坐标['Q16', 'Q4', 'F3', 'F17', 'Q17', 'R14', 'Q15']
# checkline(luozhi)
# print(type(redp_list),redp_list)
# qiefen_panduan(redp_list)

# def qiuzhu(A):
#     realA = A
#     BB = A
#     while 某条件:
#         "对BB进行修改操作"
#     CC = realA
#     while 某条件2:
#         "对CC进行操作"

# 问：为什么CC不等于A ? 是被修改后的BB。
# 我想在第二个while里面操作原始实参A，要怎么办？


#--------------------------------------------------------------------------------------------------------
# def checkline(pts):
#     """把list按照下标单双分为两个新list"""
#     for one in pts:
#         # print(pts.index(one))
#         if pts.index(one)%2 == 1:
#             redp_list.append(one)
#         else:
#             blap_list.append(one)
#
# def qiefen_panduan(A):
#     """切分出组合出三位字符串并判断是否存在"""
#     p_count = 3
#     san = ""
#     while True:
#         for one in A:
#             linshi = one[-1]
#             print(linshi)
#             san += linshi
#             p_count -= 1
#             if p_count == 0:
#                 break
#     if san in abscissa:
#         print("红字连成一条直线，直线横坐标是{}".format(san))
#
#
# abscissa = "12345678910111213141516171819"
# ordinate = "ABCDEFGHJKLMNOPQRST"
# luozhi = ["Q16","D4","Q4","D16","F3","C6","F17","R17","Q17","R16","R14","R15","Q15"]
# redp_list = []  #红字坐标['D4', 'D16', 'C6', 'R17', 'R16', 'R15']
# blap_list = []  #黑子坐标['Q16', 'Q4', 'F3', 'F17', 'Q17', 'R14', 'Q15']
# redp_list = []
# checkline(luozhi)
# print(type(redp_list),redp_list)
# qiefen_panduan(redp_list)


#------------------------------------------------------------------------------------------------------
# def creat_num_list(start,stop,step=1):
#     """构造有序数组并添创建list"""
#     alist = []
#     for num in range(start,stop,step):       #以指定步进创建列表
#         alist.append(num)
#     return alist
#
# def checkline(pts):
#     """把list按照下标单双分为两个新list"""
#     for one in pts:
#         # print(pts.index(one))
#         if pts.index(one)%2 == 1:
#             redp_list.append(one)
#         else:
#             blap_list.append(one)
#
# def qiefen_panduan(A,B):
#     """切分出组合出三位字符串并判断是否存在"""
#     for one in A:
#         one.split[-1]
#
# abscissa = creat_num_list(1,19+1)
# print(abscissa)
# ordinate = ["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","Q","R","S","T"]
# # print(abscissa,"{}".format(len(abscissa)),ordinate,"{}".format(len(ordinate)),'\n')
# luozhi = ["Q16","D4","Q4","D16","F3","C6","F17","R17","Q17","R16","R14","R15","Q15"]
# redp_list = []  #红字坐标['D4', 'D16', 'C6', 'R17', 'R16', 'R15']
# blap_list = []  #黑子坐标['Q16', 'Q4', 'F3', 'F17', 'Q17', 'R14', 'Q15']
#
# checkline(luozhi)

#---------------------------------------------------------------------------------------------------
#  美国GDP20万亿美元，中国GDP14万亿美元。若美国GDP以每年3%的增长速度，中国GDP以5%的增长速度，求多少年以后，中国和美国GDP持平

# def get_years_number(MM = 14,GM = 20,MP =0.05,GP =0.03):
#     years_number = 0
#     if MM * (1+MP) == GM * GP * (1+GP):
#         years_number += 1
#
# year = 1
# A = 14
# B = 20
# while True:
#     if  A  * 1.05 >= B * 1.03:
#         print(year)
#         break
#     else:
#         A *= 1.05
#         B *= 1.03
#         year += 1

def get_yearnum(C_GDP,A_GDP,C_p,A_p):
    year = 0
    while True:
        if  C_GDP * (1 + C_p)**year >= A_GDP * (1 + A_p)**year:
            print(year)
            break
        else:
            year += 1

get_yearnum(1,1.5,0.02,0.01)