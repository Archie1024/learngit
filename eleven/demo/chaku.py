import sys
import mysqlclient.MySQLdb

userId = int(sys.argv[1])
planId = int(sys.argv[2])
seq = userId % 32

host = "10.64.35.163"
port = 8823
user="test"
password="123456"
db="danube"

danube = MySQLdb.connect(
    host=host,
    port=port,
    user=user,
    passwd=password,
    db=db)

curDanube = danube.cursor()

db="material"

material = MySQLdb.connect(
    host=host,
    port=port,
    user=user,
    passwd=password,
    db=db)

curMaterial = material.cursor()

db="creative"

creative = MySQLdb.connect(
    host=host,
    port=port,
    user=user,
    passwd=password,
    db=db)

curTemporary = creative.cursor()

print("----------------------------------------------")
print("danube_plan_info")
print("----------------")

sql = "select * from danube_plan_info where id = " + str(planId)      #plan的各种信息
curDanube.execute(sql)
for row in curDanube.fetchall():
    print(" ".join([str(x) for x in row])) #join用法再看看，好像平时用的少哦。把列表变成了字符串。

sql = "select * from danube_creative_info_" + str(seq) + " where user_id = " + str(userId) + " and danube_plan_id = " + str(planId)
curDanube.execute(sql)   #各种新建信息
for row in curDanube.fetchall():
    mt = row[6]
    print("--------------------------------")
    print("danube_creative_info_" + str(seq) + " mt: " + str(mt))
    print("--------------------------------")
    print(" ".join([str(x) for x in row]))
    print("--------------------------------")
    print("formal_material_" + str(seq) + " mt: " + str(mt))
    print("--------------------------------")
    creative_id = row[3]   #这里好像应该是row4
    sql = "select * from formal_material_" + str(seq) + " where id = " + str(creative_id)
    curMaterial.execute(sql)
    for row in curMaterial.fetchall():
        temporary_material_id = row[3]
        print(" ".join([str(x) for x in row]))
        print("-------------------------------")
        print("temporary_material_" + str(seq) + " mt: " + str(mt))
        print("-------------------------------")
        creative_id = row[3]
        sql = "select * from temporary_material_" + str(seq) + " where id = " + str(temporary_material_id)
        curTemporary.execute(sql)
        for row in curTemporary.fetchall():
            print(" ".join([str(x) for x in row]))
        print("--------------------------------")
        print("audit_info_" + str(seq) + " mt: " + str(mt))
        print("--------------------------------")
        creative_id = row[3]
        sql = "select * from audit_info_" + str(seq) + " where mc_id = " + str(temporary_material_id)
        curTemporary.execute(sql)
        for row in curTemporary.fetchall():
            print(" ".join([str(x) for x in row]))

curTemporary.close()
curMaterial.close()
# curDanube.close()
