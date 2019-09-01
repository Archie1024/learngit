from selenium import webdriver
import time
driver = webdriver.Chrome(r"D:\tool\chromedriver")
driver.get("http://www.weather.com.cn/jiangsu/index.shtml")
time.sleep(3)
eles = driver.find_element_by_id("forecastID")
# print(eles.text)
cities = eles.text.split("℃\n")  #以换行符和C进行切割
print(cities)


lowest = None
lowest_cities = []  #因为城市温度最低的城市不唯一

for one in cities:
    city_name = one.split("\n")[0]  #取到了名字。
    city_tmp = (one.split("\n")[1].replace("℃","").split("/"))  #最高温度和最低温度的列表,因为最后一个没有/，所以要先替换掉，再切割
    low_tmp = min([int(tmp) for tmp in city_tmp])  #如果上面没有用int，用列表生成式，min()
    if lowest == None or low_tmp < lowest:
        lowest = low_tmp
        lowest_cities = [city_name]
    elif lowest == low_tmp:
        lowest_cities.append(city_name)

print("最低温度城市有{}，温度最低是：{}".format("".join(lowest_cities),lowest)) #join把列表里面的值，取出来，放到字符串里面

time.sleep(3)
driver.quit()

#----------------------------------------这个题目再好好理解理解-------------------其实也可以用bs4来做。