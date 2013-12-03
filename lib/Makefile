files = DB_perl.pm DB_py.py Common.pm
null:
install:
	install -d ${TEST_PATH_LIB}/
	install $(files) ${TEST_PATH_LIB}/
uninstall:
	for t in $(files); do rm -f ${TEST_PATH_LIB}/$$t ; done
clean:
	rm -f *~
