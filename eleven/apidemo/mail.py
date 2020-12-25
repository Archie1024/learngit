import apidemo.cfg as pz
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def mail(emil_body):
    msg = MIMEText(emil_body, 'plain', 'utf-8')  # 邮件正文
    msg['From'] = formataddr([pz.sender_name, pz.sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr([pz.recipient_name, pz.recipient])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = pz.mail_title  # 邮件的主题，也可以说是标题

    server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(pz.sender, pz.sender_key)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(pz.sender, [pz.recipient, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接


if __name__ == '__main__':
    mail("测试邮件发送功能！！")




