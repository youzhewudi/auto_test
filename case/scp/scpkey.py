from fabric.api import *
import os
import time

def scpkey():
    if not os.path.isfile('/root/.ssh/id_rsa.pub'):
        local('./scpkey.sh')
        time.sleep(30)

    put('/root/.ssh/id_rsa.pub', '/root/.ssh/authorized_keys')
