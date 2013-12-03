from fabric.api import *

import os
import sys
lib_path = os.getenv("TEST_PATH_LIB")
sys.path.append(lib_path)
import DB_py

sql = "select * from dev_item where dev_type=3"
test_branch  = DB_py.sql_exec(sql)

sql = "select * from dev_item where dev_type=4"
test_central = DB_py.sql_exec(sql)

sql = "select * from test_cfg"
test_cfg = DB_py.sql_exec(sql)

env.hosts    = [test_branch[0]['ip_addr']]
env.user     = test_branch[0]['user']
env.password = test_branch[0]['passwd']

if test_cfg[0]['direc'] == 1: ## from branch to central
    direc = "upload"
elif test_cfg[0]['direc'] == 2: ## from central to branch
    direc = "download"

## begin to transport data
def run_scp():
    dest     = test_central[0]['ip_addr']
    password = test_central[0]['passwd']
    path     = "/tmp/branch/scp"
    with cd (path):
        ## config scp key
        cmd = "fab -f scpkey.py -H %s -p %s scpkey" % (dest, password)
        run(cmd)

        ## transport data
        cmd = "./trans_scp --direc %s --host %s" % (direc, dest)
        run(cmd)
