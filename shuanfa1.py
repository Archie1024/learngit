# ------------------------------------创建一个列表oldlist,按照从大小排列到一个新的列表里面-----------------------------
# 方法一，直接排序
# oldlist = [123,13,4,6,31231231,5345]
# newlist = oldlist.sort()
# print(oldlist)
#
# 方法二，使用min来进行append排序
# def sort_list(inlist):
#     newlist = []
#     while len(inlist) > 0:
#         min_num = min(inlist)
#         newlist.append(min_num)
#         inlist.remove(min_num)
#     return  newlist     #return代表着一个while循环的结束，一定要放在while那层，因为一旦运行，循环结束
#
# print(sort_list([123,13,4,6,31231231,5345]))
#
# 方法三，假设法
# def sort_list(inlist):
#     newlist = []
#     while len(inlist) > 0:
#         #假设法，假设第一个元素最小
#         minDate = inlist[0] #假设最小值是第一个元素
#         minindx = 0
#         idx = 0     #总列表的下标
#         #验证假设
#         for one in inlist:
#             if minDate > one:   #说明假设的值不是最小，更新最小值
#                 minDate  = one
#                 minindx = idx
#             idx +=1     #取一个one下标就加1,下标更新
#         newlist.append(minDate)
#         del inlist[minindx]     #利用最小值下标删除最小值
#     return newlist
#
# print(sort_list([123,13,4,6,31231231,5345]))
#
#
#
# --------------------------------不用下标，直接remove，方便理解-------------------------------
# def sort_list(inlist):
#     newlist = []
#     while len(inlist) > 0:
#         minDate = inlist[0]
#         #假设法，假设第一个元素最小
#         #验证假设
#         for one in inlist:
#             if minDate > one:   #说明假设的值不是最小，更新最小值
#                 minDate  = one
#         newlist.append(minDate)
#         inlist.remove(minDate)    #利用最小值下标删除最小值
#     return newlist
#
# print(sort_list([123,13,4,6,31231231,5345]))




# import  shongqin.demo1      #导入包.模块，同一个包内的函数不需要加包名
                           #想到用函数，就用模块名.函数
# print("你好")
#
# def get_sum2(start,end,step=1):
#     """指定步进的求和函数"""
#     sum_date = 0
#     while start < end+1:
#         sum_date += start
#         start +=step
#     return sum_date
# print(get_sum2(1,100,2))