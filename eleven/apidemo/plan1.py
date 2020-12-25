import apidemo.mail as M
import apidemo.uint_modifyCourse_liushuaiqi as U
import time


# plan的设置，初始求情时间和每次报警都会增加的时间。
gap_time = 3
gap_time_add = 5

# 这是可以plan，每个plan下可以放多个unit
ERROR_COUNT = 1

while True:
    try:
        time.sleep(gap_time)
        U.unit_modifyCourse()  #这仅是一个unit，unit包括三个suit
    except Exception as ERROR_INFO:
        M.mail(str(ERROR_INFO) +
             """
             这是计划启用以来的第{}错误！每一次计划运行出错，
             计划报警间隔将增加5秒钟，当前计划轮循间隔约为{}
             问题处理后，请重新启用监控计划，报警间隔会重置为初始时间。
             """.format(ERROR_COUNT,gap_time)
               )

        gap_time += gap_time_add
        ERROR_COUNT += 1

