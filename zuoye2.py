# from selenium import webdriver
# import time
# driver = webdriver.Chrome(r"D:\tool\chromedriver")
# driver.get("http://www.weather.com.cn/jiangsu/index.shtml")
# time.sleep(3)
# eles = driver.find_element_by_id("forecastID")
# # print(eles.text)
# cities = eles.text.split("℃\n")  #以换行符和C进行切割
# # print(cities)
# lowest = None
# lowest_cities = []  #因为城市温度最低的城市不唯一
# for one in cities:
#     city_name = one.split("\n")[0]  #取到了名字。
#     city_tmp = (one.split("\n")[1].replace("℃","").split("/"))  #最高温度和最低温度的列表,因为最后一个没有/，所以要先替换掉，再切割
#     low_tmp = min([int(tmp) for tmp in city_tmp])  #如果上面没有用int，用列表生成式，min()
#     if lowest == None or low_tmp < lowest:
#         lowest = low_tmp
#         lowest_cities = [city_name]
#     elif lowest == low_tmp:
#         lowest_cities.append(city_name)
#
# print("最低温度城市有{}，温度最低是：{}".format("".join(lowest_cities),lowest)) #join把列表里面的值，取出来，放到字符串里面
# time.sleep(3)
# driver.quit()
#
# #----------------------------------------这个题目再好好理解理解-------------------其实也可以用bs4来做。
# from selenium import webdriver
# driver = webdriver.Chrome(r"D:\tool\chromedriver")
# import time
# driver.get("http://www.weather.com.cn/jiangsu/index.shtml")
# time.sleep(3)
# eles = driver.find_element_by_id("forecastID")
# # print(eles.text)
# cities = eles.text.split("℃\n")
# print(cities)
# low_city = []
# lowest = None
# for one in cities:
#     city = one.split("\n")[0]
#     city_tmp = one.split("\n")[1].replace("℃","").split("/")   #用的时候考虑好顺序哈
#     city_low_tmp = min([int(tmp) for tmp in city_tmp])
#     if lowest == None or city_low_tmp < lowest:
#         lowest = city_low_tmp
#         low_city = [city] #这里需要把城市直接放进列表里面，否则就不能append了，这个是动态的，满足or后面的，city就跟着变了
#     elif city_low_tmp == lowest:
#         low_city.append(city)
# print("最低温度{},城市有{}".format(lowest,"".join(low_city)))
#
# time.sleep(20)
# driver.quit()

#用bs4来做一遍！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！1
# from selenium import webdriver
# driver = webdriver.Chrome(r"D:\tool\chromedriver")
# import time
# driver.get("http://www.weather.com.cn/jiangsu/index.shtml")
# time.sleep(3)
# eles = driver.find_element_by_id("forecastID")
# html_doc = eles.get_attribute("innerHTML")
# from bs4 import BeautifulSoup   #固定写法
# soup = BeautifulSoup(html_doc,"html5lib")    #固定写法
# print(soup)
# # 发现每个城市的信息都在dl里面
# dls = soup.find_all("dl")
# # 将城市和气温信息保存到列表citys中
# cities = []
# for dl in dls:
#     name = dl.dt.a.string   #调用文本用string
#     ltemp1 = dl.dd.b.string.replace("℃","")  #找值1
#     ltemp2 = dl.dd.span.string.replace("℃","")  # 找值2
#     ltemp = min(int(ltemp1),int(ltemp2))  #把值1处理成为int
#     # print(name,ltemp)
#     cities.append([name,ltemp])
#
# print(cities)
# #比较最低温度
# lowest = None
# lowest_city = []  #温度最低城市列表
# for one in cities:
#     city = one[0]
#     ltemp = one[1]
#     if lowest == None or lowest > ltemp:
#         lowest = ltemp
#         lowest_city = [city]
#     elif ltemp == lowest:
#         lowest_city.append(city)
#
# print("最低温度城市有{}，温度最低是：{}".format("".join(lowest_city),lowest)) #join把列表里面的值，取出来，放到字符串里面
#
# time.sleep(20)
# driver.quit()

# 这他们的都行？min连字符串都不怂的吗？
# a = "343"
# b = "324"
# print(min(a,b))