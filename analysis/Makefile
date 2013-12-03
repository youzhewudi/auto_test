FILE = accel_analysis flow_analysis

default:

install:
	install -d ${TEST_PATH_BIN}
	install $(FILE) ${TEST_PATH_BIN}
uninstall:
	for t in $(FILE); do rm -f ${TEST_PATH_BIN}/$$t; done
clean:
	rm -f *~ \#*
