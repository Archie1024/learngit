"""
html是超文本标记语言：hyper text markup language
HTML页面由HTML元素构建而成，HTML元素由标签标示，浏览器分析渲染页面呈现的内容

HTML标签：
所有能在页面上看到的内容都在body里面
开始标签和结束标签构成了一个元素
H1定义最大标题，H6定义最小标题
段落标签是P，就是直接空一行的标签。
图像标签，只有一个标签，既是开始标签，又是结束标签，是有一个斜杠的。
a标签，是超链接
table标签，表格，以后用到再细讲
drv元素，用来划分整个网页区域的，drv元素可以嵌套，可以包含很多子drv


HTML属性：
类似于一个变量，能够提供HTML更多信息，出现的方式键值对
比如a标签中标记源地址的那部分href属性,比如图片的SRC属性
id是标记属性，可以出现在95%的元素里面，一般用来唯一标示这个元素，在整个HTML中都是唯一的。
class属性是有很多，可以很多元素公用一个class属性！
style属性控制元素的样式，背景颜色，字体颜色和尺寸，文本对齐等

"""
# 通过selenium这样的一个接口库，调用各种浏览器对应的驱动webdriver来控制浏览器。
# 安装接口库，cmd       pip install selenium   安装接口库。
# 安装webdriver  直接百度搜索chromewebdriver，下载对应版本
import time
from selenium import webdriver   #固定方式，永远固定，别问，一直这样写就对了
# 调用webdriver模块的chrome类，生产driver实例对象，chrome类里面都是可选参数。
# driver = webdriver.Chrome(r"D:\tool\chromedriver")   #chrome类里面需要参数，path，如果不填的话，需要把chromedriver搞到解释器的环境变量里面
#
# driver.get("https://baidu.com")
# input_kw = driver.find_element_by_id("kw")
# input_kw.send_keys("松勤")
# bt1 = driver.find_element_by_id("su")
# bt1.click()
# time.sleep(1)   #代码等待网页打开
# 获取百度松勤的第一条结果,a标签没有id属性,获取上级的
# res = driver.find_element_by_id("1")
# print(res.text)
# if "松勤软件测试" in res.text:
#     print("pass")
# else:
#     print("fail")
#
# driver
# driver.quit()
#######################################选择和操作界面元素########################################
"""
1、选择界面元素:
2、操作界面元素
    输入操作：点击，输入文字，拖拽
    输出操作：获取元素的各种属性
3、根据界面上获取的数据进行分析和处理

webdriver：操作浏览器和当前整个页面
1、在当前页面寻找符合要求的对象
2、打开网址，前进后退，刷新网页
3、获取，改变浏览器窗口大小，关闭浏览器，截屏
4、获取，设置cookies

webelement：操作对应的web元素
1、当前web元素里面的子元素里面所有符合查找条件的对象
2、操作该web元素比如
    点击元素
    输入字符
    获取元素的属性信息，如元素坐标，尺寸，文本内容等
"""
# from selenium import webdriver
# driver = webdriver.Chrome(r"D:\tool\chromedriver")
# driver.get(r"C:\Users\archie\Desktop\学习\2、selenium_web自动化\视频\autoUI_selenium\lesson02\s1.html")
# ele = driver.find_element_by_id("food")
# print(ele.text)  #拿到元素的文本信息，所有食物
# # print(ele.get_attribute("innerHTML"))    #获取内部源代码
# food_text = ele.get_attribute("innerHTML")
# # print(ele.get_attribute("outerHTML"))    #获取外部源代码
# # 怎么元获取牛肉的类。meat
# ret1 = food_text.split("</span>")[1].split(">")[0].split("<span ")[1]  #不知道为什么用空格切就是取不到
# print(ret1)
"""
获取元素信息，get_attribute方法
该元素某个属性的值   ele.get_attribute("href")  
该元素对应的HTML源码  ele.get_attribute("outerHTML")
获取该元素内部部分HTM看源码  ele.get_attribute(innerHTML)

"""
# from selenium import webdriver
# driver = webdriver.Chrome(r"D:\tool\chromedriver")
#
# driver.get(r"C:\Users\archie\Desktop\学习\2、selenium_web自动化\视频\autoUI_selenium\lesson02\s1.html")
# ele = driver.find_element_by_id("baidulink")
# print(ele.get_attribute("href"))  #拿到元素的属性
#

# 以上的代码太暴力啦，不优雅，用beautifulsoup

# 安装 pip install beautifulsoup4
# 安装 pip install html5lib  补充bs4对HTML的兼容，辅助解析


# 假设反洗bs1的HTML
from selenium import webdriver
driver = webdriver.Chrome(r"D:\tool\chromedriver")

bs1 = r"C:\Users\archie\Desktop\学习\2、selenium_web自动化\视频\autoUI_selenium\lesson02\bs1.html"
# ele = driver.get(r"C:\Users\archie\Desktop\学习\2、selenium_web自动化\视频\autoUI_selenium\lesson02\bs1.html")
with open(bs1,encoding="utf8") as f:
    htmldoc = f.read()

from bs4 import BeautifulSoup  #导入BS4
soup = BeautifulSoup(htmldoc,"html5lib")  #指定html5lib来解析HTML
tag = soup.find_all("a")   #所有满足条件的会成为一个列表，可以用指定下标的方式取值
print(tag)
tag = soup.find("a",id="link3")  #如果不指定，取第一个，bs可以直接根据属性，直接获取指定的元素。
print(tag)

tag = soup.div.a          #因为有节点，所有支持链式调用,如果不知名，只返回第一个！！！！
print(tag)

tag = soup.div.a.parent #获取指定元素的父元素！
print(tag)

time.sleep(10)
driver.quit()

#-----------------------------通过name选择元素###########################################333
# 有id就用id，没有id可以用name
ele = driver.find_element_by_name("name值")   #只会返回第一个。
ele = driver.find_elements_by_name("name值")  #返回是一个列表，找不到也不抛错。


###############################通过tag定位元素，tag，tag就是a,p,div，这些都叫标签-------------------------------
#假如tag名士唯一的，可以通过tag名来定位元素，注意head里面的元素是不能够获取的
ele = driver.find_elements_by_tag_name("标签名")

# 通过超链接来获取元素
ele = driver.find_elements_by_link_text("超链接文本：转到百度")
ele = driver.find_elements_by_partial_link_text("部分超链接文本：百度")






