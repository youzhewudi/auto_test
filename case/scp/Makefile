FILE = trans_scp scpkey.sh scpkey.py

default:

install:
	install -d ${TEST_PATH_CASE}/scp
	install fabfile.py accel_test_scp ${TEST_PATH_CASE}/scp

	install -d ${TEST_PATH_FILE}/scp/branch
	install $(FILE) ${TEST_PATH_FILE}/scp/branch

	install -d ${TEST_PATH_FILE}/scp/central
uninstall:
	rm -f ${TEST_PATH_CASE}/scp/fabfile.py
	rm -f ${TEST_PATH_CASE}/scp/accel_test_scp
	for t in $(FILE); do rm -r ${TEST_PATH_FILE}/scp/branch/$$t; done
clean:
	rm -f *~ \#*
