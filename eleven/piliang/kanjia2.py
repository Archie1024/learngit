import requests
from pprint import pprint
from piliang import cfg
import time
time_stamp = int(round(time.time() * 1000))


def Bargain_help():
    """砍价"""
    body = {
            "idenid": "{}".format(cfg.helperinfo[one]["helperOpenId"]),
            "unionid": "{}".format(cfg.helperinfo[one]["unionid"]),
            "ts":time_stamp,
            "pid": 852,
            "mid": "r+PbzLz2yQYGzDjc6VkFXg==",   #会员id，此接口暂时不用
            "callerid": "train.mo.frontend",
            "encodeidenid": "{}".format(cfg.helperinfo[one]["encodeidenid"]),
            "encodeunionid": "{}".format(cfg.helperinfo[one]["encodeunionid"]),
            "AppId": "wx336dcaf6a1ecf632",
            "checkcode": "",
            "helperUnionId": "{}".format(cfg.helperinfo[one]["unionid"]),
            "helperIcon": "{}".format(cfg.helperinfo[one]["helperIcon"]),
            "initiatorEncodedUnionId": "{}".format(cfg.UnionId),
            "encodedOrderId": "{}".format(cfg.OrderId),
            "helperNick": "{}".format(cfg.helperinfo[one]["helperNick"]),
            "helperOpenId": "{}".format(cfg.helperinfo[one]["helperOpenId"]),
            "helperMobile": "",
            "actid": "43cabd718bdbb65b170092fc9cdb52e5"
            }

    res = requests.post("{}".format(cfg.bargain_product),
                        data=body)
    retobj = res.json()
    pprint(body)
    print("?????????????????????????????????我是请求和响应的分割线????????????????????????????????????????????????????")
    pprint(retobj)
    print("---------------------------------我是每条助力内容的分割线--------------------------------------------------")
    return retobj

time_count = cfg.help_time
helper_count = len(cfg.helperinfo)
if time_count > helper_count:
    print("你所需要的助力次数超过了已有账号信息，仅能助力{}次，若想继续助力，请新增helperinfo".format(helper_count))

for one in cfg.helperinfo:
    if time_count:
        Bargain_help()
        time_count -= 1
    else:
        break

print("助力已完成，向上翻动查看每次助力结果")