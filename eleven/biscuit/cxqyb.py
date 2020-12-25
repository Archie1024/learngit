# 找到python编辑器的路径
# import sys
# print(sys.path)

"""数据类型"""
# print("hello world")
# print(type("a"))
# print(type(2))
# print(type(4.333))  #浮点数最大精度是17位
# print(type([])) #列表
# print(type({})) #字典
# print(type(())) #元组

"""加减乘数取模乘方"""
# print(2+2-1)
# print(2*2)
# print(2/3)#不取整，最多保留17位
# print(round(2/3,2))   #2保留小数的位数，最后一位四拾伍入
# print(7//3)#取整，向下取整
# print(23%4)#取模
# print(2**3)#乘方，2的3次方
# a=1
# a += 1    #等于 a = a+1
# a -= 1    #等于 a = a-1
# a *= 1    #等于 a = a*1
# a /= 1    #等于 a = a/1
#-表达式&字面量的概念
# 会产生一个确定值的式子，通常在赋值语句右侧,比如下面的1+1就是表达式。
# a = 1 + 1
#从表达式产生的值叫字面量，比如下面的是字面量（literal）
# 1
# "我是一个字符串"

#连接符的使用，只能连接字符串或者加减数值，不能字符串和数字加减
# print(3+2)
# print("我是字符串" + "我也是字符串")
# print("123"+123)      #(not "int") to str
# print(1+"1")           #unsupported operand type(s) for +: 'int' and 'str'

#变量的命名规则,
# 规则1、不能在keywordlist里面
# import keyword
# print(keyword.kwlist)
# 规则2、数字不能开头
# 规则3、不能和内置函数同名，会使得内置函数失去原来的含义
# 非强制规则4、不能下划线开头
# 非强制规则5，简洁有含义，下换线法比驼峰法用的多，定义类的时候驼峰法用的多。

#变量赋值永远跟随着最后一次的指向，但list有深浅copy。
# 例子1
# a = 3
# b = a
# a = 5
# print(b)   #b=3

# 例子2
# a = 3
# b = a
# a = 5
# b = a
# print(b)     #b=5
# print(id(a))   #查看a的内存地址
# print(id(b))   #查看b的内存地址和a一致

# ---------------------------------python的深浅拷贝，如果想用深copy，要引入新的方法-------------------------------
# l1 = [1,2,3,[11,22,33]]
# l2 = l1
# print(l2) #[1,2,3,[11,22,33]]
# l2[3][2]='aaa'
# print(l1) #[1, 2, 3, [11, 22, 'aaa']]
# print(l2) #[1, 2, 3, [11, 22, 'aaa']]
#修改l2,可以看到l1也被修改了，因为子列表公用内存地址。

# l1[0] = 0
# print(l1) #[0, 2, 3, [11, 22, 'aaa']]
# print(l2) #[1, 2, 3, [11, 22, 'aaa']]
# print(id(l1)==id(l2)) #Flase


# 字符串引号的使用
# 单引号里面用双引号，双引号里面用单引号，不够用的话用三引号，三引号还可以用来进行多行注释，依旧不够用就用转译符
# print('he say:"我是傻逼"')
# print("he's 傻逼")
# print("""我是"傻"'"逼""")
# print("小明说：\"我是傻逼\"")
# print(r"小明说：\"我是傻逼\"")
# print("we" * 6)  #对字符串重复输出

# 字符串序列的序列操作。sequence
# b = "name is tom!"
# print(b[1])    #字符串的切片操作，记住，从零开始数的。
# print(b.index("m"))     #查询字符串指定元素的下标，只能查询到第一个。59621
# print(len(b))           #查询指定字符串的长度
# print(b[-1])            #倒叙切出字符串最后一个字符
# print(b[len(b)-1])      #和上边一样，同样是切除字符串的最后一个字符。

# 字符串的切片操作
# info = "my name is tom!2019-3-23"
# print(info[3:3+4])  #左含右不含，左边数到下标的会被取到，而右边数到会少取一个，因此要多一位。
# print(info[:-9])  #取头写尾，右不含，写到会被切掉取不到
# print(info[-9:])  #取尾写头，写到的不会被切到
# print(info[-10-3:-10])  #负下标切片
# v = "asdfg"
# print(v[::-1])  #翻转字符串

##############################列表list##################################
# list的定义和序列下标使用
# list是一种序列类型，有下标，可以存储任意数据类型，由一个个元素组成。
# list1 = [1,100,3.14,[12,15]]
# print(type(list1))
# print(list1[3][1])   #切出列表list1中第四个元素(子列表)的第二个元素。
# print(100 in list1)    #结果是true,100在list1里面
# print(12 in list1)    #结果为false，12不在list1列表里面
# print(12 in list1[3])  #结果为true，12在子列表里面

# list的新增、合并、删除、和弹出
# list2 = []
# list2.append("阿俊")
# print(list2)    #在尾部增加。
# #
# list2.insert(0,"好儿子")  #（a,b） a要插入的下标，b要插入的值
# print(list2)    #在指定位置增加
#
# list2 = (list2+["俊儿","臭弟弟"])  #列表的合并方法1，括号，里面列表加列表
# list2.extend(["进进","好朋友"])    #list的合并方法2，extend方法
# print(list2)
# #
# del list2[0] #删除了当前下标为0的元素，好儿子
# my_son = list2.pop(0) #弹出了当前下标为1的元素“阿俊”，但是阿俊还能被继续访问
# print(list2)
# print(my_son)
#
# list2.remove("臭弟弟")#使用rmove匹配删除最慢，且只能删除遇到的的第一个匹配上的值
# print(list2)

#元组的定义和使用，和list差不多
# 元组也是序列类型，也可以通过下标访问元素，但是不支持增删改，只能进行查询
# 所以对于列表和元组的使用场景，储存类型是需要改变的话，需要用列表！储存的场景不需要修改的，可以用元组！！！
# tu1 = ("fds",)
# print(type(tu1))    #当一个元组时间，必须要有逗号，否则就换转换类型

# 内置函数和内置方法。用sort和sorted来比较。
# 内置函数格式     函数名(对象)
# 方法格式！       对象.方法名(传参)
# list3 = [4324,324,43,32,4,56,7878787]
# print(sorted(list3))#这是以函数，并不改变原来的值
# print(list3)        #只是调用一下原值，但是并不改变原值的叫函数
# list3.sort()        #直接对原值作用的叫方法，直接该表原值
# print(list3)        #对原值作用，改变了原值

#关于元组的内置函数，关于列表的内置函数  和内置方法，因为只有list可以对原值修改，所以只有list有方法，
# tuple2 = (4,987654,3.333,23456)
# print(len(tuple2))      #计算元组内的元素个数！
# print(max(tuple2))      #最大值
# print(min(tuple2))      #最小值
#
# list10 = [123,12345,6543,12345678234567]
# print(len(list10))      #统计元素个数
# print(max(list10))      #求最大
# print(min(list10))      #求最小
#
# print(list10.reverse())   这些是方法
# print(list10[::1])    #可以翻转列表排列列表中的所有元素。

#---------------------if else while，布尔表达式流程控制---------------------------
# 流程控制的三种方法
# 1、顺序结构，从上到下依次运行！        #可以指定行运行，缩进：tab   取消缩进：shift+tab
# 2、选择结构，在某一步选择判断，然后进入分支开始执行      #if 后面不能为空，可以写pass（空语句）
# 3、循环结构，在特定条件下，一直执行某段代码

# 具体使用哪种的心得
# 使用场景，如果只是普通多分支的，用elif写。
# 条件多层次的，考虑if嵌套语句
# 需要循环的，用while循环写
# if 条件 处理 ：对满足条件的进行处理，不满足条件的不再处理
# if 条件 处理  else 另外处理 : 对满足条件的进行处理，不满足条件的也进行处理
# if 条件1 处理  elif  条件2  条件2处理：满足条件1，处理，否则如果满足条件2，另外处理，两个都不满足，继续运行
# score = int(input("请输入你的分数"))
# if score >= 60:
#     print("及格了")
#     if score >= 90:
#         print("A等级")
#     elif score >= 80:
#         print("B等级")
#     elif score >= 70:
#         print("C等级")
# else:
#     print("不及格")
# print("run over")

# height=float(input('请输入身高（单位米）:'))
# strong=float(input('请输入体重（单位千克）:'))
# print('您的身高为{}米,体重为{}千克'.format(height,strong))
# BIM=strong/height**2
# print('您的身体状况指数为%s'%BIM)
# if BIM<18.5:
#     print('过轻')
# elif BIM>=18.5 and BIM<=25:
#     print('正常')
# elif BIM>=25 and BIM<=28:
#     print('过重')
# elif BIM>=28 and BIM<=32:
#     print('肥胖')
# elif  BIM>=32:
#     print('严重肥胖')
# else :
#     print('超级超级肥胖')


# 以下格式可以用，但是不提倡
# A = int(input("请输入你的成绩:"))
# if A >= 60:
#     if A >= 80:
#         print("小伙子你成绩不错")
#     else:
#         print("小伙子能考及格呀，可以啦。")
# elif A >= 30:
#     print("你还有救")
# else:
#     print("你去死吧，没救了！")


# 以下代码等同于上面的代码
# A = int(input("请输入你的成绩:"))
# if A >= 80:
#     print("小伙子你成绩不错")
# elif A > 60:
#     print("小伙子能考及格呀，可以啦。")
# elif A >= 30:
#     print("你还有救")
# else:
#     print("你去死吧，没救了！")
##############################符合判断###################################33
# age = int(input("请输入您的年龄："))
# sex = input('请输入您的性别（"M"or"W"）：')
# if age >= 60 and sex == "M":
#     print("oldman")
# #和下面的代码效果相同。
# age = int(input("请输入您的年龄："))
# sex = input('请输入您的性别（"M"or"W"）：')
# if age >= 60:
#     if sex == "M":
#         print("oldman")
###########################一个判断运营商的简单尝试#########################
# Y = ["130", "131", "132", "155", "156", "185", "186", "145", "176"]
# L = ["134", "135", "136", "137", "138", "139", "150", "151", "152", "157", "158", "159", "182", "183", "184", "187",
#      "188", "147", "178"]
# D = ["133", "153", "180", "189"]
# A = 3
# while A > 1:
#     telephonenumber = input("请输入")
#     if telephonenumber == "Q":
#         A = 0
#     elif len(telephonenumber)==11:
#         if  telephonenumber.isdigit():
#             if telephonenumber[:3] in Y:
#                 print("移动")
#             elif telephonenumber[:3] in L:
#                 print("联通")
#             elif telephonenumber[:3] in D:
#                 print("D")
#             else:
#                 print("号段不存在")
#         else:
#             print("有数字之外的非法字符")
#     else:
#             print("号码位数有误")
#
# print("感谢使用")

##################初识函数#################################
# def func():         #函数定义是不会执行函数内部的代码
#     print("step1")
#     print("step2")
#     print("step3")
#
# func()          #只有函数调用的时候才执行函数里面的代码
#---------------------------------------------------------------------------
# def func():         #函数定义是不会执行函数内部的代码
#     print("step1")
#     print("step2")
#     print("step3")
#     fo()        #函数调用一定要子啊函数定义的后面！因为这这里是函数里面，所以下面是先定义了！
#
# def fo():
#     print("fo函数")
# func()          #只有函数调用的时候才执行函数里面的代码

#------------------------函数的参数，形参和实参---------------------------
# 形参,在函数定义的时候的参数
#实参，在函数调用的时候传入的参数。
# def fun(a,b):   #必填形参，只有参数名的时候，是必填形参
#     print(a,b)
#
# fun(2,3)  #实参，顺序传参数
# fun([],{})#实参可以是任意类型
# fun(b=1000,a=22) #指名道姓传参
# 先指名道姓在顺序传参是错误的！！！！！！

#######################函数练习#################################3
#写一个函数，比较两个值的大小
# def get_res(a,b):
#     if  a > b:
#         print("a大")
#     elif a < b:
#         print("b大")
#     elif a==b:
#         print("一样大")
#
# get_res(5435,5435)

#其实上面的方法不好,不容易写到代码逻辑里面。
# def get_res(a,b):
#     if  a > b:
#         return 1
#     elif a < b:    #这里用elif比if好的多，因为elif是上面不满足才会过来，if是即使上面满足也要再执行一遍浪费时间。
#         return 2
#     elif a == b:
#         return 3
#
# if get_res(33,4343) == 1:
#     print("a大")

#内置函数,max,len,min，print，str()int(),字符串和int互转换等等等，帮助手册可以查看函数。

####################判断开头元素，结尾元素，纯数字，纯字母的四个函数#####################
# print('my name 123 jack'.endswith('aack'))#如果字符串的结尾是某字符串，那就返回false
# print('my name 123 jack'.startswith('my'))#如果字符串的开头是某字符串，那就返回true
# print('baa'.isalpha())  #如果字符串至少有一个字符，且全部字符都是字母，则为真，阿尔法！！！！
# print('1'.isdigit())  #如果字符串至少有一个字符，且全部字符串都是数字，则为真，低级特！！！！


#切割方法，split方法，以某值切割，就像下面，切除Jack名字。
# print('my name is jack'.split(' ')[-1])

#######################python中一切皆为对象#################################3
#方法可以看做对象的行为，count统计方法，统计字符串中，某字符串出现了几次、
# str = "tom:my name is tom!"
# print(str.count("t"))   #对象.count(被搜索词)，统计被搜索词出现了几次
# print(str.find("m",3))  #查找指定字符串，后面的参数是从第几个下标开始找，对象.find(值,从第几个小标开始找)

#join拼接，join拼接可以把任意一个序列类型，用指定字符串拼接起来。
# print("我是连接内容".join(("dfsdf","sfsd","俊儿")))

#------------------------------split 切片操作____________________________
# str_name = "my name is tom!"
# print(str_name.split(" "))   #以空格切开字符串，不保留空格，以什么切不保留什么。结果是list
# print(str_name.split("m"))     #以什么切不保留什么。
# str1 = "卧槽，这是什么骚操作-啊啊发沙发垫"
# a,b = str1.split('-')                   # 可以直接切开，再分别赋值给多个字符串
# print(a)
# print(b)

# print("China".lower())  #全部转小写
# print("CHina".upper())  #全部转大写
# print("china".title())  #转换首字母大写
# print("tom is a dog,ajun is a dog.".replace("dog","pig"))  #dog替换成pig.
# print("tom is a dog,ajun is a dog.".replace("dog","pig",1))  #dog替换成pig.也可以传参，只替换几个。

#去空格的几个老朋友----------------------------------------------------------------------
# str_5 = "     my name is tom!               "
# print(str_5)
# print(str_5.strip())   #去头尾空格
# print(str_5.lstrip())   #去头空格
# print(str_5.rstrip())   #去尾空格
# print(str_5.replace(" ",""))    #替换掉所有空格

#列表的方法总结------------------------------------------------------------------
# alist = [123,23456,"3456"]
# blist = [32435543,2345,"32435676543276544"]
# alist.append("我把直接添加的最后")
# alist.insert(2,"我把自己添加的第三个")
# del alist[-2]    #以下标把2356删除
# print(alist)

#------------------------------------------list直接字符串-------------------------------------
# a = "adsdf"
# b = list(a)
# print(b)
#
# alist = alist + blist  #把B列表和C列表合并,等于 alist.extend(blist)
# print(alist)
#
# tanchu = alist.pop(3)  #把“我把直接添加的最后”弹出并存储在tanchu里面
# alist.remove(123)  #匹配123并删除
# print(alist)
# alist.reverse()  #打印反转后的列表
# print(alist)
# clist = alist + blist     #   list的合并方法1
# print(clist)
# alist.extend(blist)     #list的合并方法2
# print(alist)

#一种简单的字符串格式化方法，format。
# name = "tom"
# age = 20
# print("name:{},age:{}".format(name,age))  #顺序填坑法，坑必须填满
#
#
# name = "tom"
# age = 20
# info = "名字：{2},年龄：{2}岁.".format(name,age,"我是第三者，也就是下标二")# .format()下标填坑法，{2}填写的是“阿俊”的下标
# print(info)
#
# info = "名字：{name},年龄：{age}岁.".format(age = 3,name = "tom")  #指名道姓填坑法
# print(info)

# info = "名字：{:>6},年龄：{:>6}岁.".format("tom",23)   #右对齐6个长度，左对齐”<“。箭头指哪边对哪边
# print(info)

# info = "名字：{:^6},年龄：{:^6}岁.".format("tom",23)   #右对齐6个长度，左对齐”<“。箭头指哪边对哪边,亦或符号对中间
# print(info)

# info = "名字：{:0>6},年龄：{:￥>6}岁.".format("tom",23)   #大于小于符号以后补0或任意符号
# print(info)

# name = "tom"
# age = 20
# info = f"名字：{name},年龄：{age}岁."      #字符串前面加加f等于调用format方法。
# print(info)

# 转换符号---------------------------------------------------------
# file_dir = "C:/lsq/123"
# file_dir1 = "C:\test"   #路径中的t会被转译。t被转换成了换行符号
# file_dir2 = r"C:\test"  #前面加r取消转译
# file_dir3 = "C:\\test"  #所以用转译符写路径的时候，一定要写两个。、，取消转译
# print(file_dir1,file_dir2,file_dir3)

#循环语句和注释
# def get_sum(start,end,step):
#     """数列求和"""
#     zhonghe = 0
#     while start <= end:
#         zhonghe += start
#         start += step
#     return zhonghe
# print(get_sum(0,100,1))
#
# #--------------------------------------------------
# print(sum(range(0,101,1)))    #一行代码解决
#
# #--------------------------------------------------
# list_sum = []               #加列表法
# for one in range(101):
#     list_sum.append(one)
# print(sum(list_sum))
#-------------------------------------------
# print(sum([one for one in range(101)]))   #一行代码

#打印1-100之间的所有数字
# a = 1
# while a <= 100:
#     print(a," ",end="")
#     a += 1

#####################################标识位，当满足某条件以后，标示未改变不再循环#############
#无限输入密码，直到输对为止
# action = True
# while action:
#     pass_wd = input("请输入密码：")
#     if pass_wd == "123":
#         print("密码正确")
#         action = False
#     else:
#         print("密码错误，请重新输入")

# 或者可以用break。
# while True:
#     pass_wd = input("请输入密码：")
#     if pass_wd == "123":
#         print("密码正确")
#         break
#     else:
#         print("密码错误，请重新输入")

#-----------------------循环list里面的值-----------------------------
# name_list = ["mike","jack","mary"]
# chishu = 0
# while chishu < len(name_list):
#     print(name_list[chishu])
#     chishu += 1


# name_list = ["mike","jack","mary"]
# for one in name_list:
#     print(one)

#用for询函打印零到100所有数字
# for one in range(0,101,1):  #左含右不含
#     print(one,"",end="")

# print([one for one in range(100)])  #列表生成式


# 创建一个指定步进的列表
# list_step5 = []
# for one  in  range(0,101,5):
#     list_step5.append(one)
# print(list_step5)
#
# print([one for one in range(0,101,5)])  # 列表生成式

# 把上面的以固定步进创建列表写成函数
# def create_list(start,end,step):
#     list_step15 = []
#     for one in range(start,end,step):
#         list_step15.append(one)
#     return list_step15
#
# print(create_list(0,301,15))  #永远的左含右不含

#breack和continue的使用、比如以下的学生表
# student_list = [
#     ["ajun",25],
#     ["archie",24],
#     ["abiao",26]
# ]
# #
# for one in student_list:  #找Archie以后跳出循环。
#     if one[0] == "archie":
#         break
#     print(one)

# for one in student_list:
#     if one[0] == "archie":
#         continue             #continue为不执行此时循环
#     print(one)

# for循环适合遍历操作，while循环适合不到特定条件不停止的操作
# 文件的读写，先不学了，先跳过去学别的
"""-----------------------------常用的注释方法------------------------------"""
# 第一步        句前注释
# 句号注释演示（我是句前注释）
# print("hello world!")    #打印字符串  （）
#############################文件的读写#########################################
'''文件的打开怕open,有返回值，可以赋值给变量'''
# file_object = open(file_name,access_"r")
# file_name:文件的路径，绝对路径和相对路径
# access_mode:读，写，读加写，默认为读！
# file_dir = r"D:\Python\存放一些简单文件\new 1.txt"      # 一定要指定后缀名
# fire_object = open(file_dir)        #默认为r,文件的打开操作
# print(type(fire_object))

# 绝对路径，相对路径，带盘符的是绝对路径，相对路径不是从盘符来说的。

# -----------------------------文件指针的概念----------------------------------------

# 获取当前文件指针位置tell
# file_dir = r"C:\Users\archie\Desktop\简历&笔记\红楼梦\葬花吟.txt"      # 一定要指定后缀名
# fire_object = open(file_dir)        #默认为r,文件的打开操作
# a = fire_object.read()    #默认一口气读完
# print(type(fire_object))
# print(fire_object.tell())   读到哪里，指针就在哪里，重新打开，指针重新刷新
# print(a)

# #
# '''从光标开始顺序操作，比如read，操作到哪里，文件指针就在哪里'''#重新打开的文件，指针刷新
# print(fire_object.read(3))     #参数是读几个字！！
# print(fire_object.read(6))     #参数是鸡就读几个字！！
# print(fire_object.read())       #如果什么都不写，就默然全部读取
#
# '''养成好习惯，打开的文件一定要及时关闭'''
# fire_object.close()
# print(fire_object.read(6))      #关闭的文件无法继续读取

# ----------------------------------文件指针的移动，seek方法--------------------------------------
"""seek0模式，默认模式"""
# file_dir = r"C:\Users\archie\Desktop\简历&笔记\红楼梦\葬花吟.txt"      # 一定要指定后缀名
# fire_object = open(file_dir)        #默认为r,文件的打开操作
# # print(type(fire_object))
# print(fire_object.tell())
# print(fire_object.read(9))       #读到哪里，指针就在哪里
# fire_object.seek(2)            #使用seek方法移动文件指针，0是seek的绝对模式，直接移动到指定位置2。默然模式0。
# print(fire_object.read(7))     #因为指针位置在2，所以应该只读取小数点后面的位数


""" "r" 只读模式不支持的1模式，1模式可以向后移动,r模式open打开主要txt，log文件"""
# 别的一些文件最好用”rb"模式打开，二进制模式打开！，打开后不是字符串！
# file_dir = r"C:\Users\archie\Desktop\简历&笔记\红楼梦\葬花吟.txt"      # 一定要指定后缀名
# fire_object = open(file_dir,"rb")        #rb二进制打开
# # print(type(fire_object))
# print(fire_object.tell())
# print(fire_object.read(2))      #读到哪里，指针就在哪里
# print(fire_object.tell())
# fire_object.seek(3,1)       #1模式是相对位置移动指针，从当前位置向后移动3个单位
# print(fire_object.tell())
# print(fire_object.read(5))      #从指针移动到的位置再读五个单位
# fire_object.seek(-3,1)
# print(fire_object.tell())

"""此外还有2模式，也是绝对模式，从最后位置移动指针"""
"""文件里面换行是两个元素的！！要注意"""

# -------------------------------整行读-------------------------------------
# file_dir = r"C:\Users\archie\Desktop\简历&笔记\红楼梦\葬花吟.txt"      # 一定要指定后缀名
# fire_object = open(file_dir,"r")        #rb
# print(fire_object.readline())       #读一整行！也是有光标的，读到哪里光标在哪里。读出的是字符串
# print(fire_object.readlines())      #读所有行，结果是一个列表list，会有换行符
# # '''如果想去掉换行符，可以用for进行遍历，再用替换replace，或者用下面的方式读！'''
# fire_object.seek(0)         #把文件指针重新定位会起始位置
# print(fire_object.read().splitlines())#返回的是去过换行符号的列表

################################写模式，如果文件不存在会新建############################
# '''如果文件不存在会新建！当用写模式打开文件，原有文件会消失！！！在保存之前还好，只是在内存里面！写入磁盘里面就完蛋了！'''
# file_dir = r"D:\Python\new 1.txt"      # 一定要指定后缀名
# fire_object = open(file_dir,"w")
# fire_object.write("12345")       # 写模式一定要写字符串进去，写在了内存，没有写在磁盘
# fire_object.write("12345" + "\n")  #写入一行以后自动换行
# fire_object.close()     #关闭的时候回直接保存
# fire_object.flush()     #写入刷新，可以保存，这种方式写入没有换行


# ---------------------追加模式，不做任何清空操作，接着写-------------------------------------
# fire = r"D:\Python\存放一些简单文件\linshi.txt"     #路径
# f = open(fire,"a")    #追加模式，不做清空操作，所以此段代码每运行一次，就增加一段"abac"
# f.write("abac")         #在可写的文件上写入字符串！
# # print(f.read())     #只读文件不支持写，所有此条操作无用！
# f.flush()       #保存已经写入的内容到硬盘！
# f.close()       #关闭也会再次保存！！
# re_fire = open(fire,"r")
# print(re_fire.read())       #阅读重新打开的所有文件！

# ------------------------------文件的可读可写操作------------------------------
""""r+:为了读写打开文件，如果文件不存在，会报错，文件指针在文件的开头
    w+:为了读写打开文件，如果文件不存在，会新建，文件指针在文件的开头。重新打开文件，如果文件已经存在，文件会被清空。
    a+:为了读写打开文件，如果文件不存在，会新建，文件指针永远在文件结尾

"""
"""                     文件的另一种写入方法，执行结束后自动运行close的写入方法  with open                  """

# with open("D:\Python\存放一些简单文件\linshi.txt","r")  as f:
#     fc = f.read()
#     print(fc)

# 支持多种方式打开。
# with open("D:\Python\存放一些简单文件\linshi.txt","a+")  as f,open (r"D:\Python\存放一些简单文件\new 1.txt","a+")  as f2:
#     f.write("春江潮水连海平\n")
#     f2.write("海上明月共潮生\n")
#
# f_open = open(r"D:\Python\存放一些简单文件\linshi.txt")
# f2_open = open(r"D:\Python\存放一些简单文件\new 1.txt")
# print(f_open.read() + f2_open.read())
#####################################循环嵌套以及算法######################################3
"""男女相亲，要求，每个男生和每个女生都要有机会接触"""###编辑首选for询函！！！！！
# boys = ["mike","jack","tom"]
# girls = ["lisa","linda","mary"]
# for boy in boys:
#     for girl in girls:
#         print("南海：{}；女孩：{}".format(boy,girl))

"""打印九九乘法表"""
# for h in range(1,10):
#     for s in range(1,h+1):
#         print("{}*{}={}".format(h,s,h*s),end = " ")
#     print()
####################################列表生成式####################################################3
# beforetax = [1000,10000,353643,32456,5000]
# aftertax = []
# for one in beforetax:
#     if  one > 5000:
#         aftertax.append(one*0.9)
#
# print(aftertax)

# #上面的代码和下面的一样的效果,不容易找BUG，逻辑简单的时候可以用。
# beforetax = [1000,10000,353643,32456,5000]
# aftertax = [one*0.9 for one in beforetax if one > 5000]
# print(aftertax)
#----------------------------把列表排序--------------------------
# alist = [43,543,5432,2,45,65,6,543234]
# alist.sort()        #正序排列
# print(alist)
# alist.reverse()     #正序排外反转
# print(alist)
# alist.sort(reverse=True)    #sort的变量
# print(alist)

"""冒泡排序，冒泡排序 """
# print([one for one in range(0,5)])   #测试代码，忽略
# alist = [43,543,5432,54323,42,45,65,6]
# for i in range(0,len(alist)-1):   #因为j是比较坐标，第一个是不用和第一个比的，所以-1.
#     # print(alist[i])
#     for j in range(0,len(alist)-i-1):  #因为最后一个是不用和最后一个比的，所以-1,
#         # print(alist[j])
#         if  alist[j] > alist[j + 1]:
#             alist[j],alist[j+1] = alist[j+1],alist[j]
# print(alist)

#i是末尾不用排的，i是末尾不用排序的，而j是在里面循环，一个个比，如果大，就滚去后面。

"""使用append排序，找出最小的append添加的list里面"""
# blist = [32312, 3213, 4, 5, 34543, 543543, 643654657777777777, 766666]
# clist = []
# while len(blist):
#     clist.append(min(blist))
#     del blist[(blist.index(min(blist)))]  #找出blist列表中，最大只的下标
# # print(blist)
# print(clist)

#if后面只要不是非零自然数都满足，负数小数都满足，非空字符串也都是满足的。
# if -100:
#     print("满足了")
# if "ha":
#     print("满足了")

'''字典，字典的定义和特性以及list套list的弊端
弊端1：list套list不清晰，age = students[1][1]
弊端2：list套list查找麻烦，需要遍历查找。
弊端3：拓展性差，一旦插入内容，下标会改变，只能在后面增加，否则老代码会有问题，删掉以后会越界
'''
# dict1 ={"name":"archie","age":18}
# set1 = {23,323,232,323}
# print(type(dict1),type(set1))#花括号，不一定是字典，因为字典一定要是键值串出现的，一个键代表一个元素。
#
# print(len(dict1)) #键和值算一个元素，所有的类型都是没有逗号的时候算一个元素。key value
# #字典不能通过下标访问，因为不是序列类型，只能通过key访问，
# print(dict1["name"])      #字典的查询操作
# dict1["体重"] = "100公斤"       #字典如何新增元素，字典名[key] = value
# print(dict1)     #新增后
# dict1["体重"] = "200公斤"       #当key存在时，就会对元素进行修改。因为key永远是唯一的。
# print(dict1)    #修改后
#字典里面没有顺序的概念，直接是放到尾部的，是通过key找的所以顺序无所谓
#
# del dict1["name"]       #通过键去删除元素。
# print(dict1)
#
# age_pop = dict1.pop("age")#通过弹出去key的方式弹出value
# print(age_pop)      #弹出的值
# print(dict1)
# 没有remove方法，因为永远是通过key访问值的
'''
键：
    1、可以是 字符串，int，float,元组，布尔，用字符串是最合适的！！！
    2、不可以是list，字典，不是哈希类型
值：
    可以任意类型！！

重点：
    注意一定要注意键的唯一性
    键值效率非常高
    字典的特性称之为map；list，string，tuple的特性称之为sequence（序列类型）
    字典可以用len统计键值对个数
'''

# ---------------------------------------字典的应用---------------------------------------------------------
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
# print(students["jack"]["age"])  #可以通过键去取值
# #判断key是否在字典
# print("mike" in students)   #判断是否在字典中！返回是布尔型！判断是否在字典中！返回是布尔型！

# --------------------------------------字典的遍历---------------------------------------
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

# 如何遍历值，比如要取到所有学生的年龄。
# for one in students:
    # print(one)  # 字典的遍历是遍历的键，单独遍历就是键，但是遍历到了键就是遍历到了值
    # print(students[one])  #这种情况下就是遍历值。
    # print(one,students[one]["age"]) #取到所有学生的信息。

# ----------------------------------遍历键值对，需要使用items-----------------------------------
"""
为什么键值对不能直接使用下标操作！

# print(students.items())     #遍历到键值对，是类列表，类列表是不支持下标操作的，可以用list()强转列表、
以键值存在的类列表,不支持下标操作,但是类列表支持遍历操作。
这种”类列表"每个“键值对”是一个元组封装的元素，最外层是类列表！
new_list = list(students.items())#转成列表后支持下标操作！
print(new_list[1])

"""

# new_list = list(students.items())#转成列表后支持下标操作！
# print(new_list)
# print(new_list[0])  #类列表支持下标操作
# for name,info in students.items():      #类列表支持遍历，把键值分开取，可以对键值分别进行操作。
#     print(name,info)
# 示例
# alist = [("juner","erzhi"),("archie","baba")]
# for name,jiaoshe in alist:
#     print(f"{name} : {jiaoshe}")
# ---------------------------------清空字典操作--------------------------------------
# dict2 = {1:2,3:4}
# dict2.clear()#把当前字典的物理存储清空
# dict2 = {}  #改变列表的指向，和上面的清空完全不一样！！
# 比如调用一个函数去清空一个列表，只能用clear，因为在函数里面重新指向，只是一个局部变量！！只是在函数里面等于空了！

# --------------------------------字典的常用操作-------------------------------------------------
# # 得到所有的key返回到类list中,类型是<class 'dict_keys'>，<class 'dict_values'>
# dict3 = {1:2,3:4}
# a = dict3.keys()
# print(a)
# print(type(a))
#
#
#的到所有value返回类list中
# dict4 = {1:2,3:4}
# b = dict4.values()
# print(b)
# print(type(b))

#
# 得到所有key,values返回到类list中.key,values成为一个元组，作为类列表的一个元素！！
# dict4 = {1:2,3:4}
# c = dict4.items()
# print(c)
# for key,values in c:
#     print(key,values)


# 更新字典。一般用在字典的合并！！用来字典的批量合并
# dict5 = {1:2,3:4}
# dict5.update({5:6})     #相当于增加一个键值对，等同于下一行的key = value写法
# dict5[9] = "值"
# print(dict5)

# 字典并非万能，不同的数据类型，各有各的用途
# 一些简单的数据，无需字典，列表就行了
# 字典是无序的，如果需要用顺序，就无法使用字典。特性决定用途！！

#####################################再识函数############################################3
"""
1、函数的做用域，就是变量的作用范围
2、函数的缺省参数
3、函数的不确定参数

"""
# X = 2 #全局变量，在同一个模块里面，在函数外面的变量就是全局变量，只要定义过，模块内都能用
# def func():
#     X = 9       #这就是局部变量。出了函数会被回收
#     print("我是函数里面的X",X)       #可以引用全局变量，也可以使用变量局部！优先执行局部变量！不是覆盖，是优先使局部变量！！
#
# func()
# print("------------")
# print("我是函数外面的X",X)

# ------------------------------在函数内部定义全局变量global方法---------------------------------------------
# X = 2
# def func():
#     global X        #告诉解释器，我下面定义的是全局变量！！
#     X = 9
#     print("我是函数里面的X",X)
#
# func()
# print("------------")
# print("我是函数外面的X",X)
# ------------------------------------函数的缺省参数-----------------------------------
# def get_sum(start,end,step = 1):        #不写就是默认，可以不写实参的参数就缺省参数，可传可不传，不传就默认
#     """这就是当初坑到你没有面试机会的那个傻逼代码"""
#     sum = 0
#     while   start <= end:
#         sum += start
#         start += step
#     return sum
# print(get_sum(1,100))
#
# print("hello",end = "**")      #python自带换行,把end = 的默认值改掉就不换行了。必填必须在可缺省的前面。
# print("world")
# #
#
#
# print(1,2,3,4)  #逗号隔开的默认单独元素，用空格分开显示
# print(1,2,3,4,sep="#######")    #改掉默认参数，就可以改掉空格。
# # open()#de 缺省参数是“r”


# ------------------------------可变数量参数----------------------------------------------------

# 比如print，可以输入无数个参数。*变量名  叫可变数量参数，可变熟练参数不接受“变量=值”的写法。
# def func(a,b = 1,*args):    #打印后args是一个元组
#     print(a,b,args)

# func(10,3,32,435,5345,453)  #args是一个无底洞，多少个实参都填不满它,3会先给B，然后剩余的值会给args
# """以上方法及其不推荐，因为,因为我也不知道为啥不推荐，反正不推荐"""

"""这种方法及其推荐是标准库里面的方法！！"""
# def func(a,*args,b = 1):    #因为args是无底洞，所以b没有机会拿到实参
#     print(a,b,args)
# #
# func(10,3,32,435,5345,453,b=10000)  #args是一个无底洞，多少个实参都填不满，所以b没有机会拿到实参--
# 所以如果b在后面，必须是用等于号传

# print(1, 2, 3, 4, sep="#######")   #就像是是print，sep或end想要拿到参数，就必须用等于号来传值

""""*可以展开列表,把列表的每一个元素作为可变数量参数传入"""
# list_num = [1,34,234,53,65,45654,7546,546546,5465,46,353454]
# def get_sum(*ages):
#     sumdate = 0
#     for one in ages:
#         sumdate += one
#     return sumdate
# print(get_sum(1,3,4))
# print(get_sum(*list_num))   #*在导入实参的时候代表展开，可以展开列表，一个个导入

# -------------------------------------关键字可变数量参数  两个*封装成字典，传入键值对-------------------------------------

# d = {"name":"archie","age":15}
# def func(a,*args,b = 1,**kwargs):    #把关键字封装成字典，可以对字典进行操作，这种是最标准的写法！！
#     print(a,b,args,kwargs)
#
# func(1,3245,3435,312321,b = 100,age = "tom",name = 19)  #传入也以字典进行传入，key必须是字符串。
# func(444,23,4,3,**d)  #两个*号可以传入字典，key必须是字符串，如果不是字符串会报错，因为int不能等于另一个不相等的int
# 所以定义字典的时候尽量用字符串，否则展开的时候回出错的。而且用int当key和下标差不多，也看不懂！字典的键也尽量不要和变量重名
# 如果想在函数里面展开字典,字典的key必须是字符串。

# 综合起来用的传参顺序，必填参数，可变数量，缺省参数，和关键字参数
# 注意字典中的key不能和变量名重名！！
# 变量= 值后面一定要是变量= 值
# 可变数量不接受 A = 5的键值对参数，赋给关键字参数，可变数量只能顺序传参。
# 默然格式最好是（必填，可变数量，可缺省，键值对参数，比如下面）
# def a (a,*args,b=2,**kwargs):
#     print(a,args,b,kwargs)
# a(1,22,212313,阿俊="shabi")  #注意，key不需要加引号。

##############################################模块与包###################################################33

# 模块的作用
"""一个.py文件叫做一个模块,按照功能点进行分割，分割成300—500行左右的文件。
不要什么都放在一起。
包里面是模块的上级，模块的上级叫包！
模块化的好处：
1、以库的形式封装功能，方便给别的代码调用
2、库其实就是模块和包
3、可以使用自己写的库，python标准库，第三方库
可以避免变量名冲突（包括函数名）
1、如果一个代码文件特别大，变量的名字容易发生重复
2、需要想出不同的变量名或者函数名
3、如果采用模块分割代码，每个模块的代码文件不是很多，就可以大大缓解这个问题
4、每个模块中的变量名的作用域只在本模块内
"""

# 同包的模块调用.(同一个包里面可以省略包名)
# import sumfun      #同一个包内模块的引用：import  + 模块名
# sumfun.get_sum2(1,100)     #同一个包下的调用：模块名.函数

# 不同包的模块调用方法2  (最简单，最好用，也最通用。)
# import pack1.sum2 as sm
# sm.get_sum(1,100)
"""""""""""""""""""""""""也可以只导入一个函数,这种写法有个弊端，一般只能一次导入一个"""""""""""""""""""""""""""""""""""""
# from AAAA.sumfun import get_sum2
# get_sum2(1,2)   #这时候就是仅导入一个函数了，仅导入一个函数，可以直接调用
# 非常不建议from sumfun import *，容易有同名函数就会被覆盖！！！如果全部导入还不如直接导入整个模块。
# 当有同名函数的时候，起别名非常有用！！！！

# -------------------------------包下面有初始化模块的概念，就是那个不新建就有的模块----------------------------------
# 初始化模块是包下面的_init_.py，只要调用这个包，就会调用初始化模块。写配置操作，配置，初始化配置，环境库，你只要用我的包，
# 我就执行这个代码，在一个包里面是公用的，包内公用的。永远不要删
# 在一个文件夹下新增这个初始化模块，这个模块就会变成一个包。
# --------------------------------什么是包package------------------------
# 当我们项目比较大的时候，模块不够用，
# 一个目录下几百上千个模块？
# 将功能相关的模块放在相应的目录结构来组织模块，这些存放模块的目录，我们称之为包
# 包里面可以有包，但是每一个包里面都有初始化模块

"""
调用包里面模块的方式有三种
1、import phone.mobile.analog             导入包—子包—模块
phone.mobile.analog.dial()          

2、import phone.mobile.analog  as hh        直接从其他包里面导入某个模块
hh.dial()              

3、from phone.mobile.analog import dial,dia2
dial()        仅导入某个函数，可以直接调用,加逗号，可以导入多个模块。

"""

# ----------------解决，在我模块里面的测试代码，当别的调用的时候时候，我不希望别人调用，仅使他调用有用部分---------------
""" __name__,可以帮助解决这个问题"""  # __name__在当前模块里面的时候，就会等于“__main__”
# 如果是导入的时候“__name__”就会不等于，mine。
# print(__name__)   #当在本模块内的时候"__name__"等于 "__mine__"
"""所以模块内不想被别人调用的测试代码，可以用i判断是否在主模块内，如果是在被调用模块内，也就是主模块内，那就运行，
在调用模块内，就不会调用测试代码。现在你去看demo3模块内的你好，你好1有这个判断，所以不会在调用模块运行。
“傻逼，我只在主模块运行”，就不会在调用模块运行。
"""
# #从某包某模块内倒入某函数！！
# from pack1.sumfun import  get_sum2    #demo3里面的if __name__ == "__main__":下的测试代码就不糊运行了！
# get_sum2(start = 0,end = 100)
###################################模块与包的使用###########################3
"""使用标准库"""
# 标准库，python自带的功能模块和包！！
# 内置函数类型，比如len,int,open,直接使用，无需import
# 功能模块，包含程序设计的主要功能，只需要import导入他们就可以使用！
# 比如打印当前时间,比如一些计算器！
# import time
# print(time.strftime("%Y_%m_%d %H:%M:%S"))
# 根据python文档可以查看细节！或者使用谷歌。

"""模块搜索规则，相当于python的环境变量，如果模块不在path里面，是无法导入的"""
# import sys
# print(sys.path)# 展示python的环境变量，是个列表，展示的第一个是当前路径！
# sys.path.append("变量地址")
# print(sys.path)#"变量地址就被append里面了"
# 怎么增加path的环境变量的，可以调用append方法增加路径。因为他是列表！！！
# 在解释器中，增加的路径关闭解释器以后会被回收！！（是应该的，要不路径越来越长！）
# 第三封库的路径的路径在最后一个（自动的，无需操心）

"""pip安装第三方库，第三方库的默认安装路径，python_tool/lib/sitepackages"""
# 安装命令、pip install 第三方库名。pip install selenium  默认安装较高版本
# 安装指定版本的第三方库。
# pip install 库名 == 版本号
# 卸载  pip uninstall 库名
# 更新安装pip install  库名 -U
# pip list 可以查看所有第三方库
####################################pycharm的使用##############################3###########################
"""project视图，代码结构化视图
代码导航
语法高亮，自动补齐，错误提示，自动修复
代码重构，
主流开发框架的支持
集成版本控制，Git，svn
单元测试
图形界面调试
一切报错以控制台输出为准
"""
# 查看代码结构
# structure  侧边栏能看到整个模块里面所有的函数和变量

# 安装插件
# settings--plugins,里面可以安装各种插件，比如数据库管理插件，比如SVN插件

# 版本管控能
# 用svn控制发布代码，可以用版本管控工具Git等

# 更换解释器或安装卸载第三方库
# project lesson 可以换解释器，或者直接安装和卸载第三方库

# 查看函数在哪里被调用，
# 1、先ctrl加鼠标左键回道定义的地方，再Ctrl悬停鼠标，能够查看在哪里被调用。
# 2、直接选中函数，鼠标左键，find usages,能够找到函数在哪里被调用，能直接展示哪一行调用
"""例子"""
# import pack1.guifangdemo as  g
# g.binarySearch_new([123, 1312, 4324, 3, 24, 32, 4324333], 24)


# 批量重构变量名或函数名
# ，找到任何一个变量或函数的名字，右键refactor—rename，然后在控制台点“do”

"""增加根目录，模块搜索路径设置"""
# 选中包，右键，点击mack dic,删除也是同样的操作。

# 查看历史代码，
# 如果代码不小心Ctrl + C已经无法补救了，那么可以用local history,本地历史功能补救，在模块右键补救。


"""皮肤调整"""
# file>>seting//App&B(外观和行为)>>herre        选黑色darcula，再选一个亮色的background 调5的透明度是舒服的
# editor>>fort>>size   #修改字体，字体大小，行距等等，我一般选择monosppaced   等宽字体，比较舒服。
# color scherma  修改配色方案，感觉darcula配合darcula背景最舒服


#######################################程序的调试，难点##############################
# 调试的作用
# 举例
"""
1、思路分析
    1、获取每一行的数据，时间，课程id、学生id
        1、打开文件fo = open(文件路径)
        2、去换行符读取所在行，info列表 = fo.read().splitlines()
        3、对每一行进行遍历处理，for line in infolines：
        4、采集有用的信息
"""
"""debug快捷键：
"F8"单步运行。step over
"art + F9"直接运行到指定位置(鼠标点击处)，或者运行到下个断点处。run to cursor

"""

# fileDir = f"D:\Python\wenjian\students.txt"
# def putInfoToDict(filename):
#     res_dict = {}
#     #1、打开文件
#     with open(filename) as fo:
#         infoList = fo.read().splitlines()#高层信息列表，去换行符切割
#         for line in infoList:#遍历这个列表
#             line  = line.replace("(","").replace(")","").replace("'","")
#             temp = line.split(",")
#             CheckTime = temp[0].strip()     #名字等于换行符号。
#             IessionId = int(temp[1].strip())     #转换为int
#             UserId  = int(temp[2].strip() )      #转换为int
#             #2-统计
#             info_dict = {"lessonid":IessionId,"checkintime":CheckTime}
#             if UserId not in res_dict:#如果不在 #如果uid不在总字典里面   总字典key uid   value 信息列表
#                 res_dict[UserId] = []       #,新增key = value,value是一个列表，新增UID = 列表！！
#             res_dict[UserId].append(info_dict)      #字典的value是列表，key可以直接表示这个列表，向里面新增信息
#
#     return res_dict
#
#
# print(putInfoToDict(fileDir))
# # 完美打印
# import pprint
# pprint.pprint(putInfoToDict(fileDir))
# json打印
# import json
# print(json.dumps(putInfoToDict(fileDir),indent=1))

# 调试的方法1
# 1、设置断点，
# 2、单步执行，step over
# 3、查看变量，表达式的值  debug后，左边查看变量，右边查看表达式的值
# 4、跳入和跳出，跳入函数，跳出函数  step into  step out    运行到光标位置step cursor

# 调试的方法2，打印log信息。log的主要组成部分，时间，级别，详细信息
# import logging
# log_file =  "文件地址"
# logging.basicConfig(filename=log_file,level=logging.DEBUG)
# logging.debug("this is debug message")
# logging.info("this is info message")
# logging.warn("this is warn message")
# logging.critical("this is criticalmessage")

"""---------------------------------面向对象1-------------------------------"""
# 面向过程变成（函数形式变成）           #面向对象变成
# OOD:面向对象语言
# OOL:非面向对象语言（非面向对象语言也可以实现面向对象的思路，但因为没有类的概念，所以非常难以维护）

"""类名通常首字母大写！驼峰法比较好，变量用下划线吧！没有继承关系，可以不写括号！
特征就是属性，行为就是方法！对象的方法就是对象的行为，
# 静态属性：类属性，共有属性，类里面的自己定义的变量。
# 动态属性；实例属性 私有属性,在类里面用函数的方式定义，每次都使用初始化方法，然后由实例定义的时候赋予值。
# 静态方法：类方法，共有的方法，与具体实例无关，类可以直接调用，不需要实例。
# 动态方法：实例方法，只能用实例访问，不能用类访问。
# 定义的时候用@staticmethod修饰，只能修饰一个。调用方式  类.方法   或   实例.方法，可以通过类访问。
"""
# class Sheep:#羊累
#     class_name = "羊"
#     def __init__(self,inWeight=100):
#         self.Weight = inWeight
#     def roar(self):
#         print("mei~")
#         self.Weight -= 5
# #
# class Tiger:#老虎类
#     class_name = "老虎"#类里面的变量叫静态属性，静态属性：类属性，共有属性
#     def __init__(self,inWeight = 200):#初始化方法，函数，在类里面叫方法，特有方法，后面跟实例属性，当创建实例的时候会被执行
#         self.Weight = inWeight#再赋值，重新再赋值。实例属性是针对实例的,有点像函数的缺省值
#     def roar(self):
#         print("wow!")
#         self.Weight -= 5
#
# class Room:#房间类
#     def __init__(self,num,animal):
#         self.num = num
#         self.animal = animal


# T1 = Tiger(400)#创建T1的老虎实例！
# print(T1.Weight)#每个个体的实例属性都不一样，属于每个单独的实例
# T2 = Tiger(inWeight=500)
# print(T2.Weight)
# T3 = Tiger()
# print(T3.Weight)
# print(T1.class_name)#老虎类的公有属性，静态属性，可以用实例去调用
# print(Tiger.class_name)#也可以用类去调用公有属性，类属性，静态属性
#
class Tiger: #老虎类
    class_name = "老虎"           #类属性
    def __init__(self,Weight = 200):         #初始化实例属性
        self.Weight = Weight                 #初始化实例属性

    def roar(self):                          #方法 叫声
        print("wow!")
        self.Weight -= 5  #哪个实例叫，哪个实例减5斤

    def feed(self,food):
        if food == "肉":
            self.Weight += 10
            print("喂食老虎成功，体重+10斤")
        else:
            self.Weight -= 10
            print("喂食老虎错误，体重-10斤")

class Sheep:#羊类
    class_name = "羊"
    color = "白花花的"
    def __init__(self,Weight = 100):
        self.Weight = Weight

    def roar(self):  #叫声
        print("mei~~")
        self.Weight -= 5  #哪个实例叫，哪个实例减5斤

    def feed(self,food):
        if food == "草":
            self.Weight += 10
            print("喂食羊成功，体重+10斤")
        else:
            self.Weight -= 10
            print("喂食羊错误，体重-10斤")

# class Room:#房间类
#     class_name = "room"
#     def __init__(self,num,animal):  #用初始化方法进行对象的组合，当使用类创建实例的时候，会自动调用这个方法。
#         self.num = num
#         self.animal = animal
# #
# # #对以上的东西进行关系组网，增加一个房间列表
# from random import randint
# import time
# rooms = []  #列表里面的元素是房间实例。
# for one in range(0,10):
#     if randint(0,1):  #1是 true，o是Fulse
#         ani = Tiger()
#     else:
#         ani = Sheep()
#     room_object = Room(one,ani)
#     rooms.append(room_object)
# print(rooms)
#
#
# start_time = time.time()        #这个小算法也可以关注下，每次while里面，运用一个新时间。
# while True:
#     curren_time = time.time()
#     if curren_time - start_time > 60:
#         print("时间到了，游戏结束")
#         sum_weight = 0
#         for one in rooms:
#             sum_weight += one.animal.Weight
#             print("第{}个房间，动物是{}，体重是{}斤".format(one.num+1,one.animal.class_name,one.animal.Weight))
#             print("总成绩是：{}".format(sum_weight))
#         break
#     room_num = randint(1,10) #显示随机房间号
#     room = rooms[room_num - 1]
#     is_select = input("该房间号为{},是否需要敲门：y/n?".format(room_num))
#     if is_select.strip() == "y" or is_select.strip() == "n":
#         if is_select.strip() == "y":        #先判断一个大范围，再判断一个小范围
#             room.animal.roar()
#         feed_food = input("请给该房间的动物喂食，肉/草")
#         # room.animal.feed(feed_food.strip())    # 此行代码假定，有草和肉之外的其他食物，
#         if feed_food.strip() == "肉" or feed_food.strip() == "草":
#             room.animal.feed(feed_food.strip())     #喂样肉和草之外的食物，完全不吃，不进入类
#         else:
#             print("我们不提供这种食物，只有肉和草！！")
#             continue
#     else:
#         print("您输入有误，进行下一次游戏")
#         continue

###############------------------------对象的继承----------------------------------------------------------
"""比如用华南虎去继承上面的老虎类"""
# class STigre(Tiger):
#     age = 20  #继承父类也可以定义自己的类和方法。
#
# huananhu1 = STigre()   #创建华南虎实例
# print(huananhu1.Weight,huananhu1.age)      #华南虎有老虎的属性，也有自己属性
# huananhu1.roar()                           #继承父类的方法
# print(huananhu1.Weight)

# class SSSTTT(Tiger,Sheep):      #新品种，老虎羊
#     pass
# ST1 = SSSTTT()       #一只普通的老虎羊
# print(ST1.class_name,ST1.color)     #优先继承第一个类的属性,若第一个没有，才会去继承第二个父类的属性


# class STiger(Tiger):
#     def __init__(self,inWeight=200):    #之类初始化，要去调用父类的初始化方法。
#         Tiger.__init__(self,inWeight)
#     def roar(self):
#         print("我是子类的方法")
# ST = STiger()
# print(ST.Weight)
# ST.roar()  #调用之类重写的方法
# super(STiger,ST).roar()  #在重写中调用父类的方法！格式super(子类类名,子类的实例名).方法，super相对于父类。这个很重要.
# super(子类类名,子类的实例名).方法     使用父类的方法。


#############################枚举和标值对#############################################33
# alist = ["a","b","c"]
# """希望有时间可以探讨一下标值对的应用"""
# for one in enumerate(alist):
#     print(one)
################################什么是异常#############################################

"""常见的异常类型"""
# 目的是希望程序不要退出，继续执行，给客户和程序员一些提示信息
# 没有定义：NameError: name 'a' is not defined
# 除数不能为0：ZeroDivisionError: division by zero
# 找不到文件:NO search file or dtrectory ：路径
# 超限：IndexError: list index out of range

#异常的捕获和处理，捕获已知异常
import time
# import traceback
#
# while True:
#     num = input("inpuy a num:")
#     try:
#       print("10000 / {}  = {}".format(num,10000/int(num)))
#       # print(name)
#     except ZeroDivisionError as e:        #异常类型
#         print("您输入的值不能为零")  #对异常进行处理，然后继续运行。
#         print(e)                     #输出异常信息,可以打到log日志里面
#     except ValueError as e1:               #多个异常类型就多分支，多个except
#         print("输入的值的类型不对")
#         print(e1)
#     except Exception as e2:          #父类，捕获所有异常！！简写excepy:
#         print(e2)
#     except:                            #可以加else。如果没有异常，执行else里面的内容
#         print(traceback.format_exc())    #打印出错的具体信息，捕获未知异常
#     finally:                 #跟无论有没有异常都会执行的代码
#         print("我一定会被执行")

##########################################调用函数栈######################################################33
#------------------------------------函数调用栈-----------------------------------------
# 函数调用栈，
"""
解释器中断代码执行，并抛出一个异常对象
并在函数调用栈，从上到下，层层寻找捕获该异常的代码，如果能找到就执行对应的代码
如果不能找到，就一直找到最外层，抛出异常！
处理过了，也应该上报！！要往上抛异常！
"""
# def f3():
#     print("f3开始")
#     try:
#         b = 4/0
#     except:
#         print("处理F3异常")
#         raise  #虽然F3处理了，但是还是要上报，在F2也要有异常捕获，否则还是全程抛错！
#     print("f3结束")
#
#
# def f2():
#     print("f2开始")
#     f3()
#     print("f2结束")
#
# def f1():
#     print("f1开始")
#     f2()
#     print("f1结束")
# try:
#     f1()
# except:
#     print("在调用处处理了一个异常。")

"""自定义异常集成exception"""
# class NameToolongError(Exception):
#     pass
# class NameTooshortError(Exception):   #继承父类
#     pass
#
# def input_name():
#     name = input("请输入用户名：")
#     if len(name) > 10:
#         raise NameToolongError  #raise 把异常抛给调用方处理！
#     elif len(name) < 5:
#         raise NameTooshortError
# try:
#     input_name()
# except NameToolongError:
#     print("名字太长")
# except NameTooshortError:
#     print("名字太短")

# 多线程和并发----------------------------------------------------------------------------------------------
# 什么是线程，什么是进程，一个进程有多个线程，一个进程至少有一个线程
# 线程共享创建它的地址空间；进程有自己的地址空间
# 线程可以直接访问其他进程的数据段；进程有他自己的父进程的数据段副本
# 线程可以和同进程的其他线程通讯；进程必须使用进程间的通讯来同其他进程通讯
# 容易创建新线程；新进程需要父进程的复制
# 线程可以对同一进程的线程进行相当大的控制；流程只能对子流程进行控制
# 并发，逻辑上同事处理多个任务的能力，并行，物理上在同一时刻执行多个并发任务。
# import time,threading
# def foo(something):
#     for i in range(5):
#         time.sleep(2)
#         print("正在",something)
#         print("正在",something)
#
# T1 = threading.Thread(target=foo,args=["看电影"])
# T2 = threading.Thread(target=foo,args=["听音乐"])
#
# T1.start()
# T2.start()

#--------------------------------啊时刻吗互相转换----------------------------
# print(ord("刘"))
# print(chr(21016))
#
# a = "ABC"
# b = b"abc"   #字符串前加b,表示字符串以bytes类型进行存储。bytes类型中的每个字符都只占用一个字节，只能存英文
# print(a,b)
#-----------------------------------------------------------------------------------
#通过encode方法，可以把中文转成bytes类型，encode可以把任何字符编辑成bytes类型
# a = "刘帅奇"
# print(a.encode("utf8"))   #看刘帅奇的utf8的encode形式
# b = a.encode("utf8")       #实际执行encode
# print(b.decode("utf8"))   #把上面的utf8形式解码成中文

#----------------什么样的编码，就需要什么样的解码,怎么写入，就需要怎么读--------------------------------
# with open("./a.txt", "w", encoding = "utf8") as f:
#     f.write("新用户")
#
# with open("./a.txt", "r", encoding = "utf8") as f:
#     a = f.read()
#     print(a)
# win是gbk,台湾日本是big5
#-------------------
# time = 6    #5
# num = 10000  #12500
# while time:
#     num *= 1.25
#     time -= 1
#     print(num)

#----------------------------------------------------------------------------
#############################文件的读写#########################################
'''文件的打开怕open,有返回值，可以赋值给变量'''
# file_object = open(file_name,access_"r")
# file_name:文件的路径，绝对路径和相对路径
# access_mode:读，写，读加写，默认为读！
# file_dir = r"D:\Python\存放一些简单文件\new 1.txt"      # 一定要指定后缀名
# fire_object = open(file_dir)       #默认为r,文件的打开操作
# print(type(fire_object))

# 绝对路径，相对路径，带盘符的是绝对路径，相对路径不是从盘符来说的。
#-----------------------------文件指针的概念----------------------------------------

# 获取当前文件指针位置tell
# file_dir = r"D:\Python\存放一些简单文件\new 1.txt"      # 一定要指定后缀名
# fire_object = open(file_dir)        #默认为r,文件的打开操作
# print(type(fire_object))
# print(fire_object.tell())
# #
# '''从光标开始顺序操作，比如read，操作到哪里，文件指针就在哪里'''#重新打开的文件，指针刷新
# print(fire_object.read(3))
# print(fire_object.read(6))
# print(fire_object.read())       #如果什么都不写，就默然全部读取
#
# '''养成好习惯，打开的文件一定要及时关闭'''
# fire_object.close()
# print(fire_object.read(6))      #关闭的文件无法继续读取

#----------------------------------文件指针的移动，seek方法--------------------------------------
"""seek0模式，默认模式"""
# file_dir = r"D:\Python\存放一些简单文件\new 1.txt"      # 一定要指定后缀名
# fire_object = open(file_dir)        #默认为r,文件的打开操作
# # print(type(fire_object))
# print(fire_object.tell())
# print(fire_object.read(9))       #读到哪里，指针就在哪里
# fire_object.seek(2)            #使用seek方法移动文件指针，0是seek的绝对模式，直接移动到指定位置2。默然模式0。
# print(fire_object.read(7))     #因为指针位置在2，所以应该只读取小数点后面的位数


""" "r" 只读模式不支持的1模式，1模式可以向后移动,r模式open打开主要txt，log文件"""
# # 别的一些文件最好用”rb"模式打开，二进制模式打开！，打开后不是字符串！
# file_dir = r"D:\Python\存放一些简单文件\new 1.txt"      # 一定要指定后缀名
# fire_object = open(file_dir,"rb")        #rb二进制打开
# # print(type(fire_object))
# print(fire_object.tell())
# print(fire_object.read(2))      #读到哪里，指针就在哪里
# fire_object.seek(3,1)       #1模式是相对位置移动指针，从当前位置向后移动3个单位
# print(fire_object.read(5))      #从指针移动到的位置再读五个单位

"""此外还有2模式，也是绝对模式，从最后位置移动指针"""
"""文件里面换行是两个元素的！！要注意"""


#-------------------------------整行读-------------------------------------
# file_dir = r"D:\Python\存放一些简单文件\new 1.txt"      # 一定要指定后缀名
# fire_object = open(file_dir,"r")        #rb二进制打开
# print(fire_object.readline())       #读一整行！也是有光标的，读到哪里光标在哪里。读出的是字符串
# print(fire_object.readlines())      #读所有行，结果是一个列表list，会有换行符
# '''如果想去掉换行符，可以用for进行遍历，再用替换replace，或者用下面的方式读！'''
# fire_object.seek(0)         #把文件指针重新定位会起始位置
# print(fire_object.read().splitlines())#返回的是去过换行符号的列表

################################写模式，如果文件不存在会新建############################
# '''如果文件不存在会新建！当用写模式打开文件，原有文件会消失！！！在保存之前还好，只是在内存里面！写入磁盘里面就完蛋了！'''
# file_dir = r"D:\Python\存放一些简单文件\new 1.txt"      # 一定要指定后缀名
# fire_object = open(file_dir,"w")
# fire_object.write("12345")       # 写模式一定要写字符串进去，写在了内存，没有写在磁盘
# fire_object.write("12345" + "\n")  #写入一行以后自动换行
# fire_object.close()     #关闭的时候回直接保存
# fire_object.flush()     #写入刷新，可以保存，这种方式写入没有换行


#---------------------追加模式，不做任何清空操作，接着写-------------------------------------
# fire = r"D:\Python\存放一些简单文件\linshi.txt"     #路径
# f = open(fire,"a")    #追加模式，不做清空操作，所以此段代码每运行一次，就增加一段"abac"
# f.write("abac")         #在可写的文件上写入字符串！
# # print(f.read())     #只读文件不支持写，所有此条操作无用！
# f.flush()       #保存已经写入的内容到硬盘！
# f.close()       #关闭也会再次保存！！
# re_fire = open(fire,"r")
# print(re_fire.read())       #阅读重新打开的所有文件！

#------------------------------文件的可读可写操作------------------------------
""""r+:为了读写打开文件，如果文件不存在，会报错，文件指针在文件的开头
    w+:为了读写打开文件，如果文件不存在，会新建，文件指针在文件的开头。重新打开文件，如果文件已经存在，文件会被清空。
    a+:为了读写打开文件，如果文件不存在，会新建，文件指针永远在文件结尾

"""
"""                     文件的另一种写入方法，执行结束后自动运行close的写入方法  with open                  """

# with open("D:\Python\存放一些简单文件\linshi.txt","r")  as f:
#     fc = f.read()
#     print(fc)

#支持多种方式打开。
# with open("D:\Python\存放一些简单文件\linshi.txt","a+")  as f,open (r"D:\Python\存放一些简单文件\new 1.txt","a+")  as f2:
#     f.write("春江潮水连海平\n")
#     f2.write("海上明月共潮生\n")
#
# f_open = open(r"D:\Python\存放一些简单文件\linshi.txt")
# f2_open = open(r"D:\Python\存放一些简单文件\new 1.txt")
# print(f_open.read() + f2_open.read())

# ---------------------------------字母也有大小关系--------------------------------------------
# print("a" < "b")     #结果为true
# str5 = "fdafsdfsgfdsgfdhjghyrjerqerwqrewqvmsjdodsomzmmlvqwertqwertyuioplkjhgfdsazxcvbnm"
# list5 = list(str5)
# print([one for one in list5 if one < "f"])

