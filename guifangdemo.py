def binarySearch(nums,target):
    print("数字列表总长度:",len(nums))
    start = 0
    end = len(nums) - 1
    while start <= end:
        print(nums[start:end + 1])   #披露每次掐头去尾后剩余nums的长度
        middle = (start + end) // 2
        print("start+end:{}+{}={}".format(start,end,(start+end)),"中间数下标：",middle,"中间数实际值:",nums[middle])
        if target > nums[middle]:
            start = middle + 1      #掐头操作
        elif target < nums[middle]:
            end = middle - 1   #去尾操作
        else:
            return middle      #刚好中间的那个数是
    return -1     #数字不在list里面！

if __name__ == "__main__":
    List = [1,3,9,77,100,222,555,3333,44444]
    # print(List)
    print(binarySearch(List,77))
"""
测试这段代码是否符合预期
场景1、nums数量为奇数或偶数，根据中间值坐标直接掐头去尾操作，奇偶无影响
场景2、猜想的数字为nums中有连续相等的数字，这种情况下取不到正常的值，所有用来排序高考成绩是不合适的！
"""
