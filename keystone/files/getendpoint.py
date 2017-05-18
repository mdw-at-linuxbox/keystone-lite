#!/usr/bin/python
import os, time, sqlite3, sys

dbname = '/var/lib/keystone/keystone.db'

def fetch_endpoint_counts():
    try:
        if not os.path.isfile(dbname):
	    print >>sys.stderr, "bad/missing db: " + dbname
	    return None
	con = sqlite3.connect(dbname)
	cur = con.cursor()
	j = cur.execute("select count(*) from endpoint;")
	q = j.fetchall()
	return q[0][0]
    except BaseException as e:
	print >>sys.stderr, "Exception: " + str(e)
	return None

def main(argv):
    global dbname
    if len(argv) > 0:
	dbname = argv[0]
    q=fetch_endpoint_counts()
    if q is None:
       exit(1)
    print q
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
