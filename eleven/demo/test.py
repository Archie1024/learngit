# import random
# def get_list(start,end,step=1):
#     "得到指定步进的数字列表"
#     a_list = []
#     for one in range(start,end,step):
#         a_list.append(one)
#     return a_list
# # range_list = (get_list(0,13))
# # print(range_list)
# range_list = (get_list(0, 13))
# while 1:
#     one = random.sample(range_list,1)
#     print("这次轮到{}".format(one))
#     range_list.remove(one)


# name_list = {"江村","帅奇","汤"}
# import random
# one = random.randint(0,13)
# print("这次轮到{}".format(one))
# range_list.remove(one)
# 根据尾号饭量，先映射给多个尾号（饭量），这样分散偶然性，while   range，不算是思路，


# s_b = []
# tongxue_size = [3,2,6,5,6]
# for one in tongxue_size:
#     geren = []
#     for one
#     s_b.append(geren)
# print(s_b)


# import random
# panzhi = []     #盘子列表1，根据饭量大小分盘子,也就是分配比重
# panzhi2 = []    #盘子列表2，所有人的盘子列表一满了以后，启用盘子列表2
#
# fanliang_list = [2,5,9]   #静香，小夫，胖虎 的饭量指数
# for one in fanliang_list:
#     A = one
#     while A:
#         panzhi.append(one)
#         A -= 1
# print(panzhi)
# # print(random.sample(panzhi,1))
# yifen = random.sample(panzhi,1)
# print(yifen)
# panzhi.remove(yifen)

# fenpeiguo = []
# import random
# member_dict = {'赵永华': 7, '孙晶晶': 8, '邢文': 1, '杨晓玲': 6, '李梦佳': 7,
#                '曹春美': 7, '李硕': 9, '江村': 2, '汤婷': 8, '张慧': 6, '胡研': 5, '杨昌为': 8, '刘帅奇':6}
# total = 0
# for key in member_dict:
#     total = total + member_dict[key]
#     member_dict[key] = total
#     print(total)
#
# num = random.randint(1, total)
#
#
#     print(fenpeiguo)
#     if num not in fenpeiguo:
#         for key in member_dict:
#             if num <= member_dict[key]:
#                 print("下一个包子是你的:", key)
#                 break
#
#     fenpeiguo.append(num)


# import random
# fenpeiguo = []  #盘子已经占用的位置。
# while 1:
#     member_dict = {'赵永华': 7, '孙晶晶': 8, '邢文': 1, '杨晓玲': 6, '李梦佳': 7,
#                    '曹春美': 7, '李硕': 9, '江村': 2, '汤婷': 8, '张慧': 6, '胡研': 5, '杨昌为': 8, '刘帅奇':6}
#     total = 0
#     for key in member_dict:
#         total = total + member_dict[key]
#         member_dict[key] = total
#
#     num = random.randint(1, total,)
#     fenpeiguo.append(num)
#     if num not in fenpeiguo:
#         for key in member_dict:
#             if num <= member_dict[key]:
#                 print("下一个包子是你的:", key)
#                 break
#
#     fenpeiguo.append(num)

# import random
# fenpeiguo = []  #盘子已经占用的位置。
# while 1:
#     member_dict = {'赵永华': 7, '孙晶晶': 8, '邢文': 1, '杨晓玲': 6, '李梦佳': 7,
#                    '曹春美': 7, '李硕': 9, '江村': 2, '汤婷': 8, '张慧': 6, '胡研': 5, '杨昌为': 8, '刘帅奇':6}
#     total = 0
#     for key in member_dict:
#         total = total + member_dict[key]
#         member_dict[key] = total
#
#     total_list = range(1,total)
#     num = random.sample(total_list)
#     fenpeiguo.append(num)
#     if num not in fenpeiguo:
#         for key in member_dict:
#             if num <= member_dict[key]:
#                 print("下一个包子是你的:", key)
#                 break
#
#     fenpeiguo.append(num)




# import random
# member_dict = {'赵永华': 7, '孙晶晶': 8, '邢文': 1, '杨晓玲': 6, '李梦佳': 7,
#                '曹春美': 7, '李硕': 9, '江村': 2, '汤婷': 8, '张慧': 6, '胡研': 5, '杨昌为': 8, '刘帅奇':6}
# total = 0
# for key in member_dict:
#     total = total + member_dict[key]
#     member_dict[key] = total
#
# while 1:
#     total_list = range(1,total)
#     num = random.sample(total_list)
#     for key in member_dict:
#         if num <= member_dict[key]:
#             print("下一个包子是你的:", key)
#             break

# #
# from random import randrange
#
# def get_list(start,end,step=1):
#     "获取指定步进的数字列表"
#     a_list = []
#     for one in range(start,end,step):
#         a_list.append(one)
#     return a_list
#
# member_dict = {'赵永华': 7, '孙晶晶': 8, '邢文': 1, '杨晓玲': 6, '李梦佳': 7,
#                '曹春美': 7, '李硕': 9, '江村': 2, '汤婷': 8, '张慧': 6,
#                '胡研': 5, '杨昌为': 8, '刘帅奇':6}
#
# total = 0
# for key in member_dict:
#     total = total + member_dict[key]
#     member_dict[key] = total
#
# total_list = get_list(1,total+1)  #得到肚子列表
# while 1:
#     num_index = randrange(len(total_list))
#     num = total_list[num_index]
#     total_list.remove(num)  #标记盘子某位置已被占据
#     for key in member_dict:
#         if num <= member_dict[key]:
#             print("这个包子是你的:", key)
#             break
#     print("瞄一眼大家肚子的剩余空间:{}".format(total_list))

# while 1:
#     import random
#     list1 = [2, 7, 5, 4]
#     num = random.sample(list1,1)[0]
#     print(num)


# # -*- coding: utf-8 -*-
# #
# import random
#
# customers = ['1049447', '1013187', '1200265', '1040452', '1043867',
#              '1013649', '1203216', '1014458', '1050748', '1048781',
#              '1041158', '1048046', '1051066']
#
# # 按照饭量分配桌子位置，饭量越大，占的位置越大，在分配中占据的可能性越大
# big_table = []
# for custom in customers:
#     if int(custom[-1]) == 0:  # 特殊情况，这才是最能吃的，虽然我们组没有
#         big_table.extend([custom] * 10)
#     else:
#         big_table.extend([custom] * int(custom[-1]))
#
# meal_amount = len(big_table)  # 初始化总量，包子管够，都能吃饱，又不浪费
# while meal_amount:
#     you_eat = random.randrange(meal_amount)  # 随机选取分配位，下标对应的人吃这个包子
#     print("{}, you eat this one.".format(big_table[you_eat]))
#     big_table.pop(you_eat)  # 吃过一个，剩余饭量减小，权重相应减小
#     meal_amount -= 1
#
# print("We are full.")






# def get_list(start,end,step=1):     #"获取指定步进的数字列表"
#     a_list = []
#     for one in range(start,end,step):
#         a_list.append(one)
#     return a_list
#
# a_list = ['a', 'b', 'c', 'd']
# b_list = get_list(1,(len(a_list)+1))
# c_list = ("key_"+str(a) for a in b_list)
#
# dict_c = dict(zip(c_list,a_list))
# print(dict_c)


# list1=["a","b","c","d"]
# list2=[0,1,2,3]
# d={}
# for i in range(len(list2)):
#     d[list2[i]]=list1[i]
# print (d)


# a_list = ['a', 'b', 'c', 'd']



def get_list(start,end,step=1):     #"获取指定步进的数字列表"
    a_list = []
    for one in range(start,end,step):
        a_list.append(one)
    return a_list
#
# a_list = ['a', 'b', 'c', 'd']
# c_list = ("key_"+str(a) for a in get_list(0,(len(a_list)+1)))
# dict_c = dict(zip(c_list,a_list))
# print(dict_c)


# a_list = ['a', 'b', 'a', 'd']
# dict_sum = {}
# for one in a_list:
#     # dict_sum["key_"+str(a_list.index(one))] = one
#     dict_sum.update({"key_"+str(a_list.index(one)):one})
# print(dict_sum)


# list1=["a","b","c","d"]
# list2=[0,1,2,3]
# d={}
# for i in range(len(list2)):
#     d[list2[i]]=list1[i]
# print (d)
#
#
#
# def list_to_dict0(a_list):  # 笨办法：遍历，计数算下标
#     a_dict = {}
#     idx = 0
#     for element in a_list:
#         a_dict["key_{}".format(idx)] = element
#         idx += 1
#     return a_dict
#
#
# def list_to_dict1(a_list):  # 遍历下标，取值
#     a_dict = {}
#     for i in range(len(a_list)):
#         a_dict["key_{}".format(i)] = a_list[i]
#     return a_dict
#
#
# def list_to_dict2(a_list):  # 遍历下标，取值 - 极简写法
#     return {"key_{}".format(i): a_list[i] for i in range(len(a_list))}
#
#
# def list_to_dict3(a_list):  # enumerate遍历，直接拿到下标和元素值
#     a_dict = {}
#     for idx, element in enumerate(a_list):
#         a_dict["key_{}".format(idx)] = element
#     return a_dict
#
#
# def list_to_dict4(a_list):  # enumerate遍历，直接拿到下标和元素值 - 极简写法
#     return {"key_{}".format(idx): element for idx, element in enumerate(a_list)}
# def list_to_dict5(a_list):  # list.index的用法；警告：前提是你要确定list中没有重复元素，否则就有问题了
#     return {"key_{}".format(a_list.index(element)): element for element in a_list}
#
#
# if __name__ == '__main__':
#     print(list_to_dict0(['a', 'b', 'a', 'c']))
#     print(list_to_dict1(['a', 'b', 'a', 'c']))
#     print(list_to_dict2(['a', 'b', 'a', 'c']))
#     print(list_to_dict3(['a', 'b', 'a', 'c']))
#     print(list_to_dict4(['a', 'b', 'a', 'c']))
#     print(list_to_dict5(['a', 'b', 'a', 'c']))


# """方案1"""
# def get_list(start,end,step=1):     #"获取指定步进的数字列表"
#     a_list = []
#     for one in range(start,end,step):
#         a_list.append(one)
#     return a_list
#
# print(sum(get_list(0,1001)))
#
# """直接加总"""

#
# def sum_1(start,end,step=1):
#     sum_1 = 0
#     for one in range(start,end,step):
#         sum_1 = sum_1 + one
#     return sum_1
# print(sum_1(1,1001))

# print(range(1,1001,1)

# print(sum(range(1,1001,1)))

#         def main():
#             for a in range(1, 10):
#                 for b in range(10):
#                     for c in range(10):
#                         s1 = a * 100 + b * 10 + c
#                         s2 = pow(a, 3) + pow(b, 3) + pow(c, 3)
#                         if s1 == s2:
#                             print
#                             s1
#
# if __name__ == '__main__':
#     main()

# def get_list(start,end,step=1):     #"获取指定步进的数字列表"
#     a_list = []
#     for one in range(start,end,step):
#         a_list.append(one)
#     return a_list




from math import sqrt
def isprime(x):
    if x==1:
        return False
    k=int(sqrt(x))
    for j in range(2,k+1):
        if x%j==0:
            return False
    return True
for i in range(2,101):
    if isprime(i):
        print(i,end=' ')