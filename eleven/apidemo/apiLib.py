import requests
from pprint import pprint
import apidemo.cfg as pz

g_sessionid = None
def loglin(username,password):
    "登陆接口"
    global g_sessionid
    body = {"username":username,
            "password":password}
    res = requests.post(f"http://{pz.API_SERVER}/api/mgr/loginReq",data=body)
    g_sessionid=res.cookies["sessionid"]

    retobj = res.json()
    pprint(retobj)
    pprint(f"sessionid:{g_sessionid}")
    return retobj

def addCourse(name,desc,idx):
    """添加课程"""
    body = {"action": "add_course",
            "data": f'''{{
                    "name":"{name}",
                    "desc":"{desc}",
                    "display_idx":"{idx}"}}'''
            }
    # header = {"Content-Type":"x-www-form-urlencoded"}  URLencoded格式，不要用headers，用了反而会出错
    res = requests.post(f"http://{pz.API_SERVER}/api/mgr/sq_mgr/",
                        data=body,cookies={"sessionid":g_sessionid})
    retobj = res.json()
    pprint(retobj)
    return retobj


def listCourse(action="list_course",pagenum="1",pagesize="20"):
    """列出课程"""
    param = {"action":action,"pagenum":pagenum,"pagesize":pagesize}
    res = requests.get(f"http://{pz.API_SERVER}/api/mgr/sq_mgr/",params=param,
                       cookies={"sessionid": g_sessionid})

    retobj = res.json()
    pprint(retobj)
    return retobj

def modifyCourse(cid,name,desc,idx):
    """修改课程"""
    body = {"action": "modify_course",
            "id":cid,
            "newdata":f'''{{
                    "name":"{name}",
                    "desc":"{desc}",
                    "display_idx":"{idx}"}}'''
            }

    res = requests.put(f"http://{pz.API_SERVER}/api/mgr/sq_mgr/",
                        data=body,cookies={"sessionid":g_sessionid})
    retobj = res.json()
    pprint(retobj)
    return retobj

def deleteCourse(cid):
    """删除课程"""
    body = {"action": "delete_course","id":cid,}

    res = requests.delete(f"http://{pz.API_SERVER}/api/mgr/sq_mgr/",
                        data=body,cookies={"sessionid":g_sessionid})
    retobj = res.json()
    pprint(retobj)
    return retobj



