FILE = ftp_client
default:

install:
	install -d ${TEST_PATH_FILE}/ftp/branch
	install $(FILE) ${TEST_PATH_FILE}/ftp/branch
uninstall:
	for t in $(FILE); do rm -f ${TEST_PATH_FILE}/ftp/branch/$$t; done
clean:
	rm -f *~
