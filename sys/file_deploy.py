from fabric.api import *
import os
import sys
path = os.getenv('TEST_PATH_LIB')
sys.path.append(path)
import DB_py

def deploy(id):
    sql = "select group_id,method_id from test_cfg where id =" + id
    data_raw = DB_py.sql_exec(sql)
    if len(data_raw) == 0:
        print "data is NULL"
        exit(1)

    sql = "select name from test_method where id =" + str(data_raw[0]['method_id'])
    data_dir = DB_py.sql_exec(sql)
    if len(data_dir) == 0:
        print "dir is NULL"
        exit(1)

    sql = "select * from dev_item where group_id =" + str(data_raw[0]['group_id'])
    data_item = DB_py.sql_exec(sql)

    for i in range(0, len(data_item)):
        if data_item[i]['dev_type'] in [3,4]:
            cmd = "fab -f file_upload.py -H %s -u %s -p %s testfile_upload:type=%s,name=%s" % (data_item[i]['ip_addr'], data_item[i]['user'], data_item[i]['passwd'], data_item[i]['dev_type'], data_dir[0]['name'])
            local(cmd)
