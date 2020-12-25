# API_SERVER = "localhost"
#
# sender = '13721330307@163.com'  # 发件人邮箱
# sender_name = 'test：线上环境接口监控邮件，莫慌'    # 发件人名字
# sender_key = 'lsq123'  # 网址邮箱分配给第三方客户端的秘钥
# mail_title = '接口监控报警，请关注。'  #邮件标题
# recipient = '13721330307@163.com'  # 收件人邮箱账号，我这边发送给自己outlook和总监的outlook。
# recipient_name = "可爱的胖虎"              #邮件接收者名字

#
time_top = 60   #请求间隔
time_sum = 0
time_new = 0
while True:
    time_new += 5
    time_sum += time_new
    if time_new >= time_top:
        break
print(time_sum//3600)