print("开始")
def get_sum(start,end,step=1):
    """这就是那个让你没有面试机会的傻逼代码"""
    zhonghe = 0
    while start <= end:
        zhonghe += start
        start += step
    print(zhonghe)
print("结束")