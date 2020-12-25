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
#-----------------------------冒泡法------------------------------
# alist = [43,543,5432,2,45,65,6,543234]
# for i in range(0,len(alist)-1):
#     # print("i = {}".format(i))
#     for j in range(0,len(alist)-1-i):
#         print("j ={}".format(j))
#         if  alist[j] > alist[j + 1]:
#             alist[j],alist[j+1] = alist[j+1],alist[j]
# print(alist)
#---------------------------冒泡做成函数-------------------------43
# def bubble_sort(nums):
#     for i in range(len(nums) - 1):
#         for j in range(len(nums) - i - 1):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     return nums
#
# res = bubble_sort([123,13,4,6,31231231,5345])
# print(res)
#---------------------------指定步进求和-----------------------------------
# def get_sum2(start,end,step=1):
#     """指定步进的求和函数"""
#     sum_date = 0
#     while start < end+1:
#         sum_date += start
#         start +=step
#     return sum_date
# print(get_sum2(1,100,2))
#------------------------打印指定步进列表--------------------------------
# def get_list(start,end,step=1):
#     "打印指定步进的数字列表"
#     a_list = []
#     for one in range(start,end,step):
#         a_list.append(one)
#     return a_list
# print(get_list(0,101,5))


# 文件的读写
file_dir = r"C:\Users\archie\Desktop\简历&笔记\红楼梦\葬花吟.txt"      # 一定要指定后缀名
fire_object = open(file_dir,"rb")        #rb二进制打开
fire_object.seek(3,1)       #1模式是相对位置移动指针，从当前位置向后移动3个单位，2模式最后位置移动指针
print(fire_object.read(6))     #参数是鸡就从指针开始读几个字
print(fire_object.readline())       #读一整行！也是有光标的，读到哪里光标在哪里。读出的是字符串
print(fire_object.readlines())      #读所有行，结果是一个列表list，会有换行符
print(fire_object.read().splitlines())#返回的是去过换行符号的列表



'''如果文件不存在会新建！当用写模式打开文件，原有文件会消失！！！在保存之前还好，只是在内存里面！写入磁盘里面就完蛋了！'''
file_dir = r"D:\Python\new 1.txt"      # 一定要指定后缀名
fire_object = open(file_dir,"w")
fire_object.write("12345")       # 写模式一定要写字符串进去，写在了内存，没有写在磁盘
fire_object.write("12345" + "\n")  #写入一行以后自动换行
fire_object.close()     #关闭的时候回直接保存
fire_object.flush()     #写入刷新，可以保存，这种方式写入没有换行


# ---------------------追加模式，不做任何清空操作，接着写-------------------------------------
# fire = r"D:\Python\存放一些简单文件\linshi.txt"     #路径
# f = open(fire,"a")    #追加模式，不做清空操作，所以此段代码每运行一次，就增加一段"abac"
# f.write("abac")         #在可写的文件上写入字符串！
# # print(f.read())     #只读文件不支持写，所有此条操作无用！
# f.flush()       #保存已经写入的内容到硬盘！
# f.close()       #关闭也会再次保存！！
# re_fire = open(fire,"r")
# print(re_fire.read())       #阅读重新打开的所有文件！


""""r+:为了读写打开文件，如果文件不存在，会报错，文件指针在文件的开头
    w+:为了读写打开文件，如果文件不存在，会新建，文件指针在文件的开头。重新打开文件，如果文件已经存在，文件会被清空。
    a+:为了读写打开文件，如果文件不存在，会新建，文件指针永远在文件结尾

"""
"""                     文件的另一种写入方法，执行结束后自动运行close的写入方法  with open                  """
# 支持多种方式打开。
# with open("D:\Python\存放一些简单文件\linshi.txt","a+")  as f,open (r"D:\Python\存放一些简单文件\new 1.txt","a+")  as f2:
#     f.write("春江潮水连海平\n")
#     f2.write("海上明月共潮生\n")

#打印1-100之间的所有数字
# a = 1
# while a <= 100:
#     print(a," ",end="")
#     a += 1

#---------------------------------打印九九乘法表--------------------------------------------
# for i in range(1,10):   #行              #外层用一个，和内层每一个都发生关系！！！外层的一个区遍历内层的所有
#     for j in range (1,i+1):  #列         #内层的所有被外层的遍历
#         print("{}*{}={}".format(i,j,i*j)) #外面的每一行的被每一列的所有区成一边做已结，每一节取消print换行时就会成为一列
#     print()         #当一个内乘外的一节完成，就换行。打印另一节

#---------------------------------上边因为有print，所有每一行都还是一节外遍历内----------------------------

# for i in range(1,10):   #行              #外层用一个，和内层每一个都发生关系！！！外层的一个区遍历内层的所有
#     for j in range (1,i+1):  #列         #内层的所有被外层的遍历
#         print("{}*{}={}".format(i,j,i*j),end ="  ")        #外面的每一行的被每一列的所有区成一边做一行
#     print()#print自带换行，每一个内乘外完成后的节变列完成后，换行打印另一个行。


#----------------------桂芳二等分题目-------------------
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


# 临时提炼需要纪录的东西

# print(round(2/3,2))     #2保留小数的位数，最后一位四拾伍入
# print(2**3)#乘方，2的3次方
# print(id(a))   #查看a的内存地址
# print(r"小明说：\"我是傻逼\"") #取消转译效果
# print(b.index("m"))     #查询字符串指定元素的下标，只能查询到第一个。59621
# tu1 = ("fds",)   一个元组时，必须有逗号
# print('my name 123 jack'.endswith('aack'))#如果字符串的结尾是某字符串，那就返回false
# print('my name 123 jack'.startswith('my'))#如果字符串的开头是某字符串，那就返回true
# print('baa'.isalpha())  #如果字符串至少有一个字符，且全部字符都是字母，则为真，阿尔法！！！！
# print('1'.isdigit())  #如果字符串至少有一个字符，且全部字符串都是数字，则为真，低级特！！！！
# str = "tom:my name is tom!"
# print(str.count("t"))   #对象.count(被搜索词)，统计被搜索词出现了几次
# print(str.find("m",3))  #查找指定字符串，后面的参数是从第几个下标开始找，对象.find(值,从第几个小标开始找)
# print("我是连接内容".join(("dfsdf","sfsd","俊儿")))
# print("China".lower())  #全部转小写
# print("CHina".upper())  #全部转大写
# print("china".title())  #转换首字母大写
# print("tom is a dog,ajun is a dog.".replace("dog","pig"))  #dog替换成pig.
# print("tom is a dog,ajun is a dog.".replace("dog","pig",1))  #dog替换成pig.也可以传参，只替换几个。
# print(str_5.strip())   #去头尾空格r l
# print(str_5.replace(" ",""))    #替换掉所有空格
# alist.reverse()  #打印反转后的列表
# info = "名字：{:0>6},年龄：{:￥>6}岁.".format("tom",23)   #大于小于符号以后补0或任意符号



# 改变标志位比break的好处是可以运营完这次循环才停止循环。


# 形参：定义的时候的参数，实参，调用时候的参数

# list2.insert(0,"好儿子")  #（a,b） a要插入的下标，b要插入的值
# print(list2)    #在指定位置增加
#
# list2 = (list2+["俊儿","臭弟弟"])  #列表的合并方法1，括号，里面列表加列表
# list2.extend(["进进","好朋友"])    #list的合并方法2，extend方法
# print(list2)
#
# del list2[0] #删除了当前下标为0的元素，好儿子
# my_son = list2.pop(1) #弹出了当前下标为1的元素“俊儿”，但是俊儿还能被继续访问
# print(list2)
# print(my_son)
#
# list2.remove("臭弟弟")#使用rmove匹配删除最慢，且只能删除遇到的的第一个匹配上的值
# print(list2)


# list3 = [4324,324,43,32,4,56,7878787]
# print(sorted(list3))#这是以函数，并不改变原来的值，所以是可以用于元组的
# print(list3)        #只是调用一下原值，但是并不改变原值的叫函数
# list3.sort()        #直接对原值作用的叫方法，直接该表原值
# print(list3)        #对原值作用，改变了原值

# print(list10.reverse())   这些是方法，翻转列表
# print(list10[::1])    #可以翻转列表排列列表中的所有元素。

# alist = [43,543,5432,2,45,65,6,543234]
# alist.sort()        #正序排列
# print(alist)
# alist.reverse()     #正序排外反转
# print(alist)
# # #或者
# alist.sort(reverse=True)    #sort的变量
# print(alist)


# beforetax = [1000,10000,353643,32456,5000]
# aftertax = [one*0.9 for one in beforetax if one > 5000]
# print(aftertax)

# 字典元素的增删改查
# dict1 ={"name":"archie","age":18}
# print(dict1["name"])      #字典的查询操作
# # dict1["体重"] = "100公斤"       #字典如何新增元素，字典名[key] = value，如果有就是修改
# del dict1["name"]
# age_pop = dict1.pop("age")


#字典的遍历是遍历键

# students = {
#     "mike":{
#         "age":23,
#         "height":180,
#         "weight":100
#     },
#     "jack":
#         {"age":15,
#         "height":150,
#         "weight":70
#          }
# }
# for one in students:
#     print(one)  # 字典的遍历是遍历的键，单独遍历就是键，但是遍历到了键就是遍历到了值
#     print(students[one])  #这种情况下就是遍历值。
#     print(one,students[one]["age"]) #取到所有学生的信息。

# 可以通过list方法转换层列表，就支持下标操作
# 字典清空只能用clear
# global X 可以定义全局变量


# 函数的传参
# d = {"name":"archie","age":15}
# def func(a,*args,b = 1,**kwargs):    #把关键字封装成字典，可以对字典进行操作，这种是最标注的写法！！
#     print(a,b,args,kwargs)
# func(1,3245,3435,312321,b = 100,age = "tom",name = 19)  #传入也以字典进行传入，key必须是字符串，name不需要加引号
#
# #展开列表
# list_num = [1,34,234,53,65,45654,7546,546546,5465,46,353454]
# print(*list_num)

# if __name__ == "__main__":跟随测试代码

# import time
# print(time.strftime("%Y_%m_%d %H:%M:%S"))


# 模块调用
# import pack1.sum2 as sm      #(最简单，最好用，也最通用。)
# sm.get_sum(1,100)

# from AAAA.sumfun import get_sum2
# get_sum2(1,2)   #这时候就是仅导入一个函数了，仅导入一个函数，可以直接调用

# import sys
# print(sys.path)# 展示python的环境变量，是个列表，展示的第一个是当前路径！
# sys.path.append("变量地址")
# print(sys.path)#"变量地址就被append里面了"

# pip install 库名 == 版本号
# 卸载  pip uninstall 库名
# 更新安装pip install  库名 -U
# pip list 可以查看所有第三方库

# 直接选中函数，鼠标左键，find usages,能够找到函数在哪里被调用，能直接展示哪一行调用
# 批量重构函数,找到任何一个变量或函数的名字，右键refactor—rename，然后在控制台点“do”
