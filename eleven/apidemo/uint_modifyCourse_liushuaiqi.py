import apidemo.apiLib as lib
import random  #随机数函数


def unit_modifyCourse():
    """修改课程单元"""
    """-------------------set_suit-----------------------------------------------"""
    # 先登陆，方便获取cookies
    lib.loglin("auto","sdfsdfsdf")

    # 随机课程名称，并添加课程
    course_name = "测试课程_"+str(random.randint(0,999999999999))
    retobj1=lib.addCourse(
        f"{course_name}",
        "随便介绍",
        "5435")

    ret_list_before = lib.listCourse()["retlist"]#把第一次添加后的结果列一下
    new_course_name = "rename_"+str(random.randint(0,999999999999))
    cid = retobj1["id"]

    """-------------------test_suit------------------------------------------------"""
    # 修改
    retobj2=lib.modifyCourse(
        f"{cid}",
        f"{new_course_name}",
        "随便介绍",
        "5435")

    if retobj2.get("retcode",None) == 0:
        print("检查点》》》retcode为0》》》检查点通过。\n\n")
    else:
        print("检查点》》》retcode为 0》》》检查点不通过！！！\n")

    #修改后再列出课程
    ret_list_after = lib.listCourse()["retlist"]

    if len(ret_list_after) == len(ret_list_before):
        print("检查点》》》修改课程后，课程数量相同》》》检查点通过！\n")
    else:
        print("检查点》》》修改课程后，课程数量不相同》》》检查点不通过！！！\n")

    courses = []
    for one in ret_list_after:
        if one not in ret_list_before:
            courses.append(one)
    assert len(courses) == 1 #判断仅有被修改的内容改变了，其他的内容不变
    course = courses[0]

    assert course["id"] == cid
    assert course["name"] == new_course_name  #返回名字等于随意生成的那个名字，别的都不变
    assert course["desc"] == "随便介绍"
    assert course["display_idx"] == 5435
    print("整体比较：修改后只有修改课程的修改项目改动了，测试用例3执行通过")

    """-------------------drop_suit----------------------------------------------"""
    lib.deleteCourse(cid)


if __name__ == '__main__':
    unit_modifyCourse()






