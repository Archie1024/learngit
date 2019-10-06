"""
有一个从小到大的数值列表，给定一个值X，使用二分法找出X在列表中的位置（下标）
二分查找法：表中的元素是正序排列的，将表中间的值与X比较，若两者相等，则查找成功，否则利用中间位置纪录将表分成
前后两个表，若中间的位置大于X，则查找前表，否则查找后表，重复以上操作，直到查找到结果或查找完毕所有数据。

测试这段代码是否符合预期
场景1、nums数量为奇数或偶数。测试结果：根据中间值坐标直接掐头去尾操作，奇偶无影响。
场景2、猜想的数字为nums中有连续相等的数字，这种情况下取不到正常的值，所有用来排序高考成绩是不合适的！

"""
# def binarySearch_new(nums, target):
#     print("数字列表总长度:",len(nums))
#     start = 0
#     end = len(nums) - 1
#     while start <= end:
#         print(nums[start:end + 1])   #披露每次掐头去尾后剩余nums的长度
#         middle = (start + end) // 2
#         print("start+end:{}+{}={}".format(start,end,(start+end)),"中间数下标：",middle,"中间数实际值:",nums[middle])
#         if target > nums[middle]:
#             start = middle + 1      #掐头操作
#         elif target < nums[middle]:
#             end = middle - 1   #去尾操作
#         else:
#             return middle      #刚好中间的那个数是
#     return -1     #数字不在list里面！
#
# if __name__ == "__main__":
#     List = [1,3,9,77,100,222,555,3333,44444]
#     # print(List)
#     print(binarySearch_new(List, 77))

# def search_x(nums,x):
#     start = 0
#     end = len(nums)
#     while start <= end:
#         middle = (start+end)//2
#         if  nums[middle] > x:  #(中间的都比X大，去尾操作)
#             end = middle - 1
#         elif nums[middle] < x:
#             start = middle + 1
#         else:
#             return middle
#     return -1
#
# if __name__ == "__main__":
#     List = [1,3,9,77,100,222,555,3333,44444]
#     # print(List)
#     print(search_x(List,444))
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


#------------------------------------------------------------------------------------------------------------
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
