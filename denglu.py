# passwd = {"archie":"123","ajun":"2b"}
# error_cnt = 3
# userName = input("请输入用户名：").strip()
# while True:
#     #- 如果用户名错误，提示一直输入
#     if userName not in passwd:
#         userName  = input("请输入用户名：").strip()
#         continue
#     #- 用户名正确，提示输入密码
#     psw = input("当前用户名是：{}，请输入密码：".format(userName).strip())
#     #- 验证账号密码一一对应
#     if (userName,psw) in passwd.items():
#         print("欢迎用户：{},登陆成功！".format(userName))
#         break#结束登陆
#     else:#不成功，只要进来，一定是密码错误
#         error_cnt -= 1
#         if error_cnt ==0:#三次机会没有了
#             print("今天三次机会没有了，请明天再试")
#             break
#         print("密码错误，您还有 {} 次机会".format(error_cnt))


"""--------------------------------一个获取名字的需求----------------------------------------------"""
"""
A old lady come in, the name is Mary,level 312
A pretty boy come in,the name is Archie,level 32232432
"""
# def get_name(srcstr):
#     #函数体
#     name = srcstr.split("is")[1].split(",")[0].strip()#以the name is 切开，下标取1，取到第二段,再以逗号切，取第一个，去空格
#     return name
# inStr = input("输入信息：")
# print(get_name(inStr))
