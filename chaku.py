# import sys
# import MySQLdb
#
# userId = int(sys.argv[1])
# planId = int(sys.argv[2])
# seq = userId % 32
#
# host = "10.64.35.163"
# port = 8823
# user="test"
# password="123456"
#  12 db="danube"
#  13
#  14 danube = MySQLdb.connect(
#  15     host=host,
#  16     port=port,
#  17     user=user,
#  18     passwd=password,
#  19     db=db)
#  20
#  21 curDanube = danube.cursor()
#  22
#  23 db="material"
#  24
#  25 material = MySQLdb.connect(
#  26     host=host,
#  27     port=port,
#  28     user=user,
#  29     passwd=password,
#  30     db=db)
#  31
#  32 curMaterial = material.cursor()
#  33
#  34 db="creative"
#  35
#  36 creative = MySQLdb.connect(
#  37     host=host,
#  38     port=port,
#  39     user=user,
#  40     passwd=password,
#  41     db=db)
#  42
#  43 curTemporary = creative.cursor()
#  44
#  45 print "----------------"
#  46 print "danube_plan_info"
#  47 print "----------------"
#  48
#  49 sql = "select * from danube_plan_info where id = " + str(planId)
#  50 curDanube.execute(sql)
#  51 for row in curDanube.fetchall():
#  52     print " ".join([str(x) for x in row])
#  53 sql = "select * from danube_creative_info_" + str(seq) + " where user_id = " + str(userId) + " and danube_plan_id = " + str(planId)
#  54 curDanube.execute(sql)
#  55 for row in curDanube.fetchall():
#  56     mt = row[6]
#  57     print "--------------------------------"
#  58     print "danube_creative_info_" + str(seq) + " mt: " + str(mt)
#  59     print "--------------------------------"
#  60     print " ".join([str(x) for x in row])
#  61     print "--------------------------------"
#  62     print "formal_material_" + str(seq) + " mt: " + str(mt)
#  63     print "--------------------------------"
#  64     creative_id = row[3]
#  65     sql = "select * from formal_material_" + str(seq) + " where id = " + str(creative_id)
#  66     curMaterial.execute(sql)
#  67     for row in curMaterial.fetchall():
#  68         temporary_material_id = row[3]
#  69         print " ".join([str(x) for x in row])
#  70         print "-------------------------------"
#  71         print "temporary_material_" + str(seq) + " mt: " + str(mt)
#  72         print "-------------------------------"
#  73         creative_id = row[3]
#  74         sql = "select * from temporary_material_" + str(seq) + " where id = " + str(temporary_material_id)
#  75         curTemporary.execute(sql)
#  76         for row in curTemporary.fetchall():
#  77             print " ".join([str(x) for x in row])
#  78         print "--------------------------------"
#  79         print "audit_info_" + str(seq) + " mt: " + str(mt)
#  80         print "--------------------------------"
#  81         creative_id = row[3]
#  82         sql = "select * from audit_info_" + str(seq) + " where mc_id = " + str(temporary_material_id)
#  83         curTemporary.execute(sql)
#  84         for row in curTemporary.fetchall():
#  85             print " ".join([str(x) for x in row])
#  86 curTemporary.close()
#  87 curMaterial.close()
#  curDanube.close()
