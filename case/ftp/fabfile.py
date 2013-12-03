from fabric.api import *
import os
import sys
sys.path.append(os.getenv("TEST_PATH_LIB"))

import DB_py

## ftp client infomation
sql = "select * from dev_item where dev_type=3"
test_branch  = DB_py.sql_exec(sql)

## ftp server infomation
sql = "select * from dev_item where dev_type=4"
test_central = DB_py.sql_exec(sql)

## test cfg infomation
sql = "select * from test_cfg"
test_cfg = DB_py.sql_exec(sql)


branch  = test_branch[0]['ip_addr']
central = test_central[0]['ip_addr']

env.passwords = {
    branch  : test_branch[0]['passwd'],
    central : test_central[0]['passwd']
}

env.roledefs = {
    'client' : [branch],
    'server' : [central]
}

## config ftp server
@roles('server')
def run_server():
    with cd("/tmp/central/ftp"):
        run("./auto_ftp")

## begin to transport data
@roles('client')
def run_client():
    user = "waa_ftp"
    passwd = "123"
    if (1 == test_cfg[0]['direc']): ## from client to server
        direc = "upload"
    else:
        direc = "download"

    with cd("/tmp/branch/ftp"):
        cmd = "./ftp_client --direc %s --host %s --user %s --passwd %s" % (direc, central, user, passwd)
        run(cmd)
