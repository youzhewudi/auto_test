#!/usr/bin/env python

import MySQLdb

def sql_exec(sql, ip = 'localhost'):
    if (sql == ''):
        print "Need sql!"
        quit()

    try:
        conn = MySQLdb.connect(host    = ip,
                               user    = 'forceview',
                               passwd  = 'forceview',
                               db      = 'waa')
        conn.autocommit(True)
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    except BaseException, error:
        print ("Connect mysql error: ")
        print (str(error))
        quit()

    try:
        sql.lower()
        count = 0
        if sql.find('select') == 0:
            count   = cursor.execute(sql)
            results = cursor.fetchall()
        else:
            results = cursor.execute(sql)
    except BaseException, error:
        print ("Execute sql error: ")
        print (str(error))
    finally:
        cursor.close()
        conn.close()

    return results
