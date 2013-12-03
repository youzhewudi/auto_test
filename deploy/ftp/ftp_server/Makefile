FILES = account.txt auto_ftp vsftpd.conf vsftp.vu waa_ftp

default:

install:
	install -d ${TEST_PATH_FILE}/ftp/central
	install $(FILES) ${TEST_PATH_FILE}/ftp/central
uninstall:
	for t in $(FILES); do rm -f ${TEST_PATH_FILE}/ftp/central/$$t; done
clean:
	rm -f *~ \#*
