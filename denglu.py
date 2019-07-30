
""
"""""--------------------------------一个获取名字的需求----------------------------------------------"""

# 需求：写一个模拟登陆的小程序，用户名和密码以键值对的形式保存在字典中，若用户名输错，提示一直输入用户名；若用户名输对，提示
# 输入对应的密码，密码只有三次输入机会，机会用完提示“账号锁定”，在每次输密错码后，提示今日剩余机会。



# passwd = {"archie":"123","ajun":"2b"}
# error_cnt = 3
# userName = input("请输入用户名：").strip()
# while True:
#     #- 如果用户名错误，提示一直输入
#     if userName not in passwd:
#         userName  = input("请输入用户名：").strip()
#         continue  #contine的意思是不再运行下面的代码，继续上面的循环，只有不满足的时候，代码才向下运行。
#     psw = input("当前用户名是：{}，请输入密码：".format(userName))
#     #- 验证账号密码一一对应
#     if (userName,psw) in passwd.items():
#         print("欢迎用户：{},登陆成功！".format(userName))
#         break#结束登陆
#     else:#不成功，只要进来，一定是密码错误，因为账号肯定是对的了。
#         error_cnt -= 1
#         if error_cnt ==0:#三次机会没有了
#             print("今天已经输错三次，账号已锁定，请明天再试")
#             break
#         print("密码错误，您还有 {} 次机会".format(error_cnt))


"""--------------------------------一个获取名字的需求----------------------------------------------"""

#根据日志信息获得纯净的用户名字
"""
A old lady come in, the name is Mary,level 312
A pretty boy come in,the name is Archie,level 32232432
"""
def get_name(srcstr):
    #函数体
    name = srcstr.split("is")[1].split(",")[0].strip()#以the name is 切开，下标取1，取到第二段,再以逗号切，取第一个，去空格
    return name
inStr = input("输入信息：")
print(get_name(inStr))
