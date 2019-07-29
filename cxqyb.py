
"""数据类型"""
# print("hello world")
# print(type("a"))
# print(type(2))
# print(type(4.333))
# print(type([])) #列表
# print(type({})) #字典
# print(type(())) #元组

"""加减乘数取模乘方"""
# print(2+2)
# print(2*2)
# print(2/3)#不取整，最多保留17位
# print(7//3)#取整，向下取整
# print(23%4)#取模
# print(2**3)#乘方
# a += 1    #等于 a = a+1
# a -= 1    #等于 a = a-1
# a *= 1    #等于 a = a*1
# a /= 1    #等于 a = a/1
#-表达式&字面量的概念
# 会产生一个确定值的式子，通常在赋值语句右侧,比如下面的1+1就是表达式。
# a = 1 + 1
#从表达式产生的值叫字面量，比如下面的是字面连
# 1
# "我是一个字符串"

#连接符的使用，只能连接字符串或者加减述职，不能字符串和数字加减
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
# 非强制规则5，简洁有含义，下换线法比驼峰法多

#变量赋值永远跟随着最后一次的指向
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

# 字符串，单引号里面用双引号，双引号里面用单引号，不够用的话用三引号，三引号还可以用用来注释，依旧不够用就用转移符
# print('he say:"我是傻逼"')
# print("he's 傻逼")
# print("""我是"傻"'"逼""")
# print("小明说：\"我是傻逼\"")

# 字符串序列的序列操作操作。sequence
# b = "name is tom!"
# print(b[1])    #字符串的切片操作，记住，从零开始数的。
# print(b.index("m"))     #查询字符串指定元素的下标，只能查询到第一个。59621
# print(len(b))           #查询指定字符串的长度
# print(b[-1])            #倒叙切出字符串最后一个字符
# print(b[len(b)-1])      #和上边一样，同样是切除字符串的最后一个字符。

# 字符串的切片操作
# info = "my name is tom!2019-3-23"
# print(info[3:3+4])  #左含右不含，左边数到下标的会被切到，右边数到的必须再多一个。
# print(info[:-9])  #切头写尾，右不含，写到会被切掉
# print(info[-9:])  #切尾写头
# print(info[-10-3:-10])  #负下标切片

# list的定义和序列下标使用
# list是一种序列类型，有下标，可以存储任意数据类型
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
#
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

#元组的定义和使用，和list差不多
# 元组也是序列类型，也可以通过下标访问元素，但是支持增删改，只能进行查询
# 所以对于列表和元组的使用场景，储存类型是需要改变的话，需要用列表！储存的场景不需要修改的，可以用元组！！！
# tu1 = ("fds",)
# print(type(tu1))    #当一个元组时间，必须要有逗号，否则就换转换类型

# 内置函数和内置方法。用sort和sorted来比较。
# 内置函数格式     函数名(对象)
# 方法格式！       对象.方法名(传参)
# list3 = [4324,324,43,32,4,56,7878787]
# print(sorted(list3))#这是以函数，并不该表原来的值
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
# 2、选择结构，在某一步选择判断，然后进入分支开始执行      #if 后面不能为空，如果需求不清晰，可以写pass（空语句）
# 3、循环结构，在特定条件下，一直执行某段代码

# 具体使用哪种的心得
# 使用场景，如果只是普通多分支的，用elif写。
# 条件多层次的，考虑if嵌套语句
# 需要循环的，用while循环写

# 具体使用哪种的心得
# 使用场景，如果只是普通多分支的，用elif写。
# 条件多层次的，考虑if嵌套语句
# 需要循环的，用while循环写
# if 条件 处理 ：对满足条件的进行处理，不满足条件的不再处理
# if 条件 处理  else 另外处理 : 对满足条件的进行处理，不满足条件的夜进行处理
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
#     telephonenumber = input("请输入你的手机号,我将会告诉你运营商(输入Q退出工具):")
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
# 形参。在函数定义的时候的参数
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

# print("China".lower())  #全部转小写
# print("CHina".upper())  #全部转大写
# print("china".title())  #转换首字母大写

# print("tom is a dog,ajun is a dog.".replace("dog","pig"))  #dog替换成pig.
# print("tom is a dog,ajun is a dog.".replace("dog","pig",1))  #dog替换成pig.也可以传参，只替换几个。

#去空格几个老朋友----------------------------------------------------------------------
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
# del alist[-2]    #以下标把2356删除                     #这个多看下格式
# print(alist)
#
# alist = alist + blist  #把B列表和C列表合并,等于 alist.extend(blist)
# print(alist)
#
# tanchu = alist.pop(3)  #把“我把直接添加的最后”弹出并存储在tanchu里面
# alist.remove(123)  #匹配123并删除
# print(alist)
# alist.reverse()  #打印反转后的列表
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
# file_dir2 = "C:\test"   #路径中的t会被转译。t被转换成了换行符号
# file_dir2 = r"C:\test"  #前面加r取消转译
# file_dir3 = "C:\\test"  #所以用转译符写路径的时候，一定要写两个。、，取消转译
# print(file_dir3)

#循环语句和注释
# def get_sum(start,end,step):
#     """这就是那个让你没有面试机会的傻逼代码"""
#     zhonghe = 0
#     while start <= end:
#         zhonghe += start
#         start += step
#     return zhonghe
# print(get_sum(0,100,1))
#
# sum_shabi = 0
# a = 1
# b =100
# while a <= b:
#     sum_shabi += a
#     a += 1
# print(sum_shabi)

#打印1-100之间的所有数字
# a = 1
# while a <= 100:
#     print(a," ",end="")
#     a += 1

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
#         print("")
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
#     print(one)

# 创建一个指定步进的列表
# list_step5 = []
# for one  in  range(0,101,5):
#     list_step5.append(one)
# print(list_step5)

# 把上面的以固定步进创建列表写成函数
# def create_list(start,end,step):
#     list_step15 = []
#     for one in range(start,end,step):
#         list_step15.append(one)
#     return list_step15
#
# print(create_list(0,301,15))

#breack和continue的使用、比如以下的学生表
# student_list = [
#     ["ajun",25],
#     ["archie",24],
#     ["abiao",26]
# ]

# for one in student_list:  #找Archie以后跳出循环。
#     if one[0] == "archie":
#         print(one)
#         break


# for one in student_list:
#     if one[0] == "archie":
#         continue             #continue为不执行此时循环
#     print(one)

# for循环适合遍历操作，while循环适合不到特定条件不停止的操作

# 文件的读写，先不学了，先跳过去学别的


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
#
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
# alist = [324324,234,3432,546,54654,654,6,54,423,4,24,35,646,54,667676,547]
# alist.sort()
# print(alist)


"""冒泡排序，冒泡排序 """
# blist = [32312,3213,4,5,34543,543543,643654657777777777,766666]
# for i in range(0,len(blist)-1):
#     print("i",i)
#     for j in range(0,len(blist)-1-i):
#         print("j",j)
#         if blist[j] > blist[j+1]:
#             blist[j],blist[j+1] = blist[j+1],blist[j]
# print(blist)
#i是末尾不用排的，i是末尾不用排序的，而j是在里面循环，一个个比，如果大，就滚去后面。

"""使用append排序，找出最小的append添加的list里面"""
# blist = [32312, 3213, 4, 5, 34543, 543543, 643654657777777777, 766666]
# clist = []
# while len(blist):
#     clist.append(min(blist))
#     del blist[(blist.index(min(blist)))]
# print(blist)
# print(clist)

#if后面只要不是非零自然数都满足，负数小数都满足，非空字符串也都是满足的。
# if -100:
#     print("满足了")
# if "ha":
#     print("满足了")



