print("你好1")
if __name__ == "__main__":
    print("傻逼，我只在主模块运行")

def get_sum2(start,end,step=1):
    """指定步进的求和函数"""
    sum_date = 0
    while start < end+1:
        sum_date += start
        start +=step
    print(sum_date)
# print(get_sum2(1,100,2))

print("引用结束啊")