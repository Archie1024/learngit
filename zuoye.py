
# m_telnumber = ["187","139","137","188"]
# u_telnumber = ["135","130","137","155"]
# t_telnumber = ["199","133","181","180"]
#
# tel = input("请输入你的手机号：")
# # 判断位数
# def tel_select():
#     if len(tel) == 11:
#         if tel.isdigit():#不用谢==True,因为满足以后直接是满足了。因为直接是bool
#             tel_num = tel[:3]       #切一次，用三次，划算，需要多次调用传值给变量。
#             if tel_num in m_telnumber:
#                 # print("移动")
#                 return 1
#             elif tel_num in u_telnumber:        #这里用elif ,否则如果，避免匹配以后继续判断。
#                 # print("联通")
#                 return 2
#             elif tel_num in t_telnumber:
#                 # print("电信")
#                 return 3
#             else:
#                 # print("无此号段")
#                 return -1
#         else:
#             # print("不是纯数字")
#             return -2
#     else:
#         # print("手机号位数有误")
#         return -3       #可以根据返回值判断状态。
#
# if  tel_select() == -3:     #根据返回值判断状态！！
#     print("位数有误了！")

#----------------------------这个乘法口诀表-----------------------------
# for n in range(1,10):
#     for m in range(1,10):
#         print("{}{}{}{}{}".format(n,"*",m,"=",n*m))
#
#     print("")         #这是个错误的，下面写一个正确的。
#
# for m in range(1, 10):
#     for n in range(1, m + 1):
#         print("%d*%d=%d\t" % (n, m, n * m), end="")
#
#     print("")
#

#-----------------------------以固定格式输出学生和学生年龄---------------------------
# fadf,4;adfasdf,24;fsfadsf,432;
# info = input("信息格式“姓名，年龄；”请输入您的信息：")
# if  ";" in info and info.count(",") == info.count(";"):
#     stu_info = info.split(";")#切开之后是list，两刀三段，后面有一个空元素
#     print(stu_info)
#     for one in stu_info:
#         if one == "":#简单过滤到空字符串
#             continue
#         temp = one.split(",")#把每一个学生的信息切成一个list
#         name = temp[0].strip()#用下标取到每个学生的name并去空格
#         age = temp[1].strip()
#         print("{:<20}:{:>3};".format(name,age))
#
# else:
#     print("输入信息格式不对")

# #可以加while，可以判断是否有逗号，可以判断是否是int。
#-----------------------------------------------------------------------------------------


"""题目，假设以下字符串log是一个log文件，每行的第一列是文件类型，第二列是文件大小，求统计每种文件类型的总大小"""


log = """
f20180111014341/i_51a7hC3W.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156063244230469	image/jpeg	0
f20180111014341/j_R0Hpl4EG.json	1036	ForGzwzV3e-uR3_UzvppJs1VgfQG	15156064773253144	application/json	0
f20180111020739/i_0TDKs0rD.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156076847077556	image/jpeg	0
f20180111020739/j_JFO6xiir.json	1040	FmUhTchdLOd7LBoE8OXzPLDKcW60	15156077904192983	application/json	0
f20180111090619/i_1BwNksbL.jpg	49634	FtXBGmipcDha-67WQgGQR5shEBu2	15156329458714950	image/jpeg	0
f20180111090619/i_3BKlsRaZ.jpg	30152	FoWfMSuqz4TEQl5FT-FY5wqu5NGf	15156330575626044	image/jpeg	0
f20180111090619/i_5XboXSKh.jpg	40238	Fl84WaBWThHovIBsQaNFoIaPZcWh	15156329453409855	image/jpeg	0
f20180111090619/i_6DiYSBKp.jpg	74017	FrYG3icChRmFGnWQK6rYxa88KuQI	15156329461803290	image/jpeg	0
f20180111090619/i_76zaF2IM.jpg	38437	Fui8g5OrJh0GQqZzT9wtepfq99lJ	15156334738356648	image/jpeg	0
f20180111090619/i_B6TFYjks.jpg	37953	FleWqlK2W1ZmEgAatAEcm1gpR0kC	15156329464034474	image/jpeg	0
f20180111090619/i_N9eITqj3.jpg	38437	Fui8g5OrJh0GQqZzT9wtepfq99lJ	15156330419595764	image/jpeg	0
f20180111090619/i_QTSNWmA6.jpg	37953	FleWqlK2W1ZmEgAatAEcm1gpR0kC	15156333104224056	image/jpeg	0
f20180111090619/i_XdHcAfh1.jpg	56479	FjLQIQ3GxSEHDfu6tRcMylK1MZ05	15156334227270309	image/jpeg	0
f20180111090619/i_Xyy723MU.jpg	50076	FsfZpQzqu084RUw5NPYW9-Yfam_R	15156334229987458	image/jpeg	0
f20180111090619/i_d8Go0EOv.jpg	30152	FoWfMSuqz4TEQl5FT-FY5wqu5NGf	15156334736228515	image/jpeg	0
f20180111090619/i_diuHmX53.jpg	40591	FuTx1pw4idbKnV5MSvNGxCA5L470	15156333878320713	image/jpeg	0
f20180111090619/i_qQKzheSH.jpg	55858	Fj0A3i8V7fzzOiPQFL79ao15hkN9	15156329456666591	image/jpeg	0
f20180111090619/i_rHL5SYk8.jpg	40238	Fl84WaBWThHovIBsQaNFoIaPZcWh	15156336509742181	image/jpeg	0
f20180111090619/i_xZmQxUbz.jpg	40238	Fl84WaBWThHovIBsQaNFoIaPZcWh	15156333240603466	image/jpeg	0
f20180111090619/i_zBDNgXDv.jpeg	73616	FlgNwq8lypgsxrWs_ksrS_x47SQV	15156334232887875	image/jpeg	0
f20180111090619/j_4mxbEiVh.json	2990	Fpq-3yl3Yr1CadNrJVSDnpeRhQtT	15156331445226898	application/json	0
f20180111090619/j_i1K74768.json	3042	Fl5PpDw1TsZXMuhoq1RUrOeGZ6br	15156335067090003	application/json	0
f20180111095839/i_Q7KMKeda.png	518522	Fl-yB1_ruL2uxZN9k7DjB62h9dYH	15156359599713253	image/png	0
f20180111095839/j_5DpqHolV.json	184	FoYvi7cmSrzuVjUgCRzW5kU95SVo	15156359719719064	application/json	0
f20180111100442/i_No8kToIV.jpg	48975	Fu1cw3f--5Vpz9kLGeJfvljhCtyZ	15156364349642377	image/jpeg	0
f20180111100442/i_P1bkvSeg.jpg	68200	FvYe8vi46TjUKhEy_UwDqLhO6ZsW	15156363800690634	image/jpeg	0
f20180111100442/i_T1AulKcD.jpg	52641	Fj2YzvdC1n_1sF93ZZgrhF3OzOeY	15156364021186365	image/jpeg	0
f20180111100442/i_X8d8BN07.jpg	50770	FivwidMiHbogw77lqgkIKrgmF3eA	15156363969737156	image/jpeg	0
f20180111100442/i_g0wtOsCX.jpg	76656	Fmtixx0mP9CAUTNosjLuYQHL6k0P	15156363448222155	image/jpeg	0
f20180111100442/i_h5OT9324.jpg	72672	FvbIqPLTh2cQHTIBv2akUfahZa_Z	15156364401354652	image/jpeg	0
f20180111100442/i_he8iLYI6.jpg	49399	FjeJvwjwhU-hKZsq66UoBg9_tEJs	15156363907932480	image/jpeg	0
f20180111100442/i_kg29t7Pp.jpg	76293	FuYj__sSeEN7AsXMbxO24Z8Suh8d	15156364156384686	image/jpeg	0
f20180111100442/i_oz1YoBI1.jpg	75620	FkY3xsUMwOI01zgoH1iXXgiQeq6I	15156364089112904	image/jpeg	0
f20180111100442/i_xrOT98on.jpg	50021	Fql7ookM1Rc6V7VairKAfnKe-o9w	15156363856357316	image/jpeg	0
f20180111135114/i_Zqt8Tmoe.png	161629	FlELw59_mV3VqDBLyu1BKN4fIWnx	15156500155209863	image/png	0
f20180111135114/j_uhHoMXKq.json	159	FrypljwAr2LgoLAePBNTUYTUAgDt	15156500200488238	application/json	0
f20180111142119/i_s83iZ2GR.png	92278	Fns8tdh3JCkRmfE_COYEu4o8w03E	15156517082371259	image/png	0
f20180111142119/j_0g45JRth.json	159	Fq1rFwdRguYRXrp61nGZ5TsUG1V-	15156517143375596	application/json	0
f20180111144306/i_yE5TC84E.png	139230	Fjf61ymabEnEvnr5ZMHFjXGCrYlP	15156530038824150	image/png	0
f20180111144306/j_OF4WVtSH.json	159	FqwkKcxfo8jd0jFUyuH4X2CrnE9q	15156530083419530	application/json	0
f20180111150230/i_KtnER4g3.png	120044	FuwOWdrqzcr2-UScem-LzEMgMezs	15156541734892258	image/png	0
f20180111150230/j_xMSUEejY.json	158	FjJr_4deMqFphGaptm-2Pa6wwRP2	15156541771989216	application/json	0
f20180111151741/i_JuSWztB3.jpg	92506	FrIjRevHSi6xv4-NQa2wrHu5a1zQ	15156550875370965	image/jpeg	0
f20180111153550/i_9wWzVenl.gif	769872	FvslKY9JUaCQm-lu02E34tvAP_oG	15156561674621628	image/gif	0
"""
#
"""--------------------------------------用标志位可以得到，正确答案-----------------------------------------------"""
# res = []
# line_list = log.split("\n")
# # print(line_list)
# for line in line_list:#遍历，提取每一行的文件类型和大小
#     if line == "":#过滤空字符串
#         continue
#     temp = line.split("\t")
#     file_type = temp[0].split(".")[-1]#以标点符号获得文件类型
#     file_size = int(temp[1].strip())#去空格，转成int型，为累加操作做准备
#     # print(file_type,file_size)
#     inflag = False
#     for one in  res:   #[[],[],[].[].[],[]]的列表格式去匹配新增，如果是新的就要新增，如果发现匹配的上就累加大小
#         if file_type == one[0]:#去匹配这一行的文件类型。
#             one[1] += file_size
#             inflag = True#匹配成功！！
#             break   #成功后面的就不要匹配了。跳出匹配，匹配结束
#     if  inflag == False:#for当前list，如果标志位状态没变，匹配失败，新增文件大小和类型。
#         res.append([file_type,file_size])
# print(res)
"""-------------------------逻辑好像一致，为什么用else不用标志位就得不到正确答案----------------------------"""
# res = []
# line_list = log.split("\n")
# # print(line_list)
# for line in line_list:#遍历，提取每一行的文件类型和大小
#     if line == "":#过滤空字符串
#         continue
#     temp = line.split("\t")
#     file_type = temp[0].split(".")[-1]#以标点符号获得文件类型
#     file_size = int(temp[1].strip())#去空格，转成int型，为累加操作做准备
#     # print(file_type,file_size)
#     for one in  res:   #[[],[],[].[].[],[]]的列表格式去匹配新增，如果是新的就要新增，如果发现匹配的上就累加大小
#         if file_type == one[0]:#去匹配这一行的文件类型。
#             one[1] += file_size
#             break   #成功后面的就不要匹配了。跳出匹配，匹配结束
#         else:
#             res.append([file_type,file_size])
# print(res)  #为什么不行，为什么不行！！！！！！！！！！
"""第一次for的时候one不存在，所以不会进入for循环
把添加one的逻辑写在for里面，就永远不会有one，自锁了
也就是说第一次for的时候，for了一个空，没有运行下面的代码。"""

"""--------------------错误写法2，为什么可以得到正确答案----------------------------------"""
# res = []
# line_list = log.split("\n")
# # print(line_list)
# for line in line_list:#遍历，提取每一行的文件类型和大小
#     if line == "":#过滤空字符串
#         continue
#     temp = line.split("\t")
#     file_type = temp[0].split(".")[-1]#以标点符号获得文件类型
#     file_size = int(temp[1].strip())#去空格，转成int型，为累加操作做准备
#     # print(file_type,file_size)
#     for one in  res:   #[[],[],[].[].[],[]]的列表格式去匹配新增，如果是新的就要新增，如果发现匹配的上就累加大小
#         if file_type == one[0]:#去匹配这一行的文件类型。
#             one[1] += file_size
#             inflag = True#匹配成功！！
#             break   #成功后面的就不要匹配了。跳出匹配，匹配结束
#     else:
#         res.append([file_type, file_size])
# print(res)  #为什么又可以了，为什么又可以啦

#------------------------------------创建一个列表oldlist,按照从大小排列到一个新的列表里面-----------------------------

#方法一，直接排序
# oldlist = [123,13,4,6,31231231,5345]
# newlist = oldlist.sort()
# print(oldlist)

#方法二，使用min来进行append排序
# def sort_list(inlist):
#     newlist = []
#     while len(inlist) > 0:
#         min_num = min(inlist)
#         newlist.append(min_num)
#         inlist.remove(min_num)
#     return  newlist     #return代表着一个while循环的结束，一定要放在while那层，因为一旦运行，循环结束
#
# print(sort_list([123,13,4,6,31231231,5345]))

#方法三，假设法
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
#             idx +=1     #取一个one下标就加1,下标更新，这是当前one的坐标
#         newlist.append(minDate)
#         del inlist[minindx]     #利用最小值下标删除最小值
#     return newlist
#
# print(sort_list([123,13,4,6,31231231,5345]))

# #--------------------------------不用下标，直接remove，方便理解----------------------3---------
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

#############################3读写文件，工资##############################################
# 计算工资，这个是你感兴趣的
# rfile_dir = r"D:\Python\wenjian\file1.txt"
# wfile_dir = r"D:\Python\wenjian\file2.txt"
# with open(rfile_dir) as rfile,open(wfile_dir,"w") as wfile:
#     #!、读取文件名字加工资
#     info_list = rfile.read().splitlines()#list
#     for line in info_list:
#         if ";" in line:#有分号的进入拼接分支
#             temp = line.split(";")#list ["name","工资"]。先切两段
#             if ":" in temp[0] and ":" in temp[1]:
#                 name = temp[0].split(":")[1].strip()##切，下标取值，去空格
#                 salary = temp[1].split(":")[1].strip()#切，下标取值，去空格
#                 if salary.isdigit():#判断工资是否是数字！
#                     salary = int(salary)    #转成int型准备扣税
#                     #写入文件，按照一定的要求写入
#                     ourstr = "name:{:<9};sllary:{:<9};tax:{:<9};income:{:<9};".format(name,salary,salary*0.1,salary*0.9)
#                     # wfile.write(ourstr + "\#这个可以放到最外层
#                 else:
#                     ourstr = "工资不是数据，无法正常写入！"
#                     # wfile.write(ourstr + "\n")#这个可以放到最外层
#             else:
#                 ourstr = "这一行没有冒号，无法正常写入。"
#                 # wfile.write(ourstr + "\n")#这个可以放到最外层
#         else:#没有分号的line进入此分支
#             ourstr = "这一行没有分号，无法正常写入。"
#         wfile.write(ourstr + "\n")#为什么在这里呢，因为这里已经是和第一个if并列的了，是if的最外层
#####################################房间老虎喂食游戏##########################################333
# class Tiger:#老虎类
#     class_name = "老虎"
#     def __init__(self,Weight = 200):
#         self.Weight = Weight
#
#     def roar(self):  #叫声
#         print("wow!")
#         self.Weight -= 5  #哪个实例叫，哪个实例减5斤
#
#     def feed(self,food):
#         if food == "肉":
#             self.Weight += 10
#             print("喂食老虎成功，体重+10斤")
#         else:
#             self.Weight -= 10
#             print("喂食老虎错误，体重-10斤")
#
# class Sheep:#羊类
#     class_name = "羊"
#     def __init__(self,Weight = 100):
#         self.Weight = Weight
#
#     def roar(self):  #叫声
#         print("mei~~")
#         self.Weight -= 5  #哪个实例叫，哪个实例减5斤
#
#     def feed(self,food):
#         if food == "草":
#             self.Weight += 10
#             print("喂食羊成功，体重+10斤")
#         else:
#             self.Weight -= 10
#             print("喂食羊错误，体重-10斤")
#
# class Room:#房间类
#     class_name = "room"
#     def __init__(self,num,animal):  #用初始化方法进行对象的组合
#         self.num = num
#         self.animal = animal
#
# #对以上的东西进行关系组网
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
# start_time = time.time()
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
#         if is_select.strip() == "y":
#             room.animal.roar()
#         feed_food = input("请给该房间的动物喂食，肉/草")
#         if feed_food.strip() == "肉" or feed_food.strip() == "草":
#             room.animal.feed(feed_food.strip())     #
#         else:
#             print("喂食食物错误！")
#             continue
#     else:
#         print("您输入有误，进行下一次游戏")
#         continue
#----------------------------------终极题目，飞机大战-----------------------------------------------------

