from fabric.api import *
from fabric.contrib.files import *
import os

def testfile_upload(type, name):
    if exists("/tmp/common"):
        pass
    else:
        run("mkdir -p /tmp/common")
        put(os.environ.get('TEST_PATH_FILE') + 'common/WAA_TEST_FILE', '/tmp/common/')
        put(os.environ.get('TEST_PATH_LIB')  + 'Common.pm', '/tmp/common/')
        run("chmod +x /tmp/common/*")

    if type == '3':
        if exists("/tmp/branch/" + name):
            pass
        else:
            run("mkdir -p /tmp/branch/" + name)
            put(os.environ.get('TEST_PATH_FILE') + name + '/branch/*', '/tmp/branch/' + name)
            run("chmod +x /tmp/branch/" + name + "/*")
    elif type == '4':
        if exists("/tmp/central/" + name):
            pass
        else:
            run("mkdir -p /tmp/central/" + name)
            put(os.environ.get('TEST_PATH_FILE') + name + '/central/*', '/tmp/central/' + name)
            run("chmod +x /tmp/central/" + name + "/*")
    else:
        print "Error: the value of type is wrong"
        quit
