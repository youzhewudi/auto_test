files = test_link init_test_system file_deploy.py file_upload.py run_test
env_file = init_environment.sh
null:
install:
	install -d ${TEST_PATH_BIN}/
	install $(files) ${TEST_PATH_BIN}/
	cp $(env_file) /etc/profile.d/

	install -d ${TEST_PATH_FILE}/common/
	install WAA_TEST_FILE ${TEST_PATH_FILE}/common/
uninstall:
	for t in $(files); do rm -f ${TEST_PATH_BIN}/$$t ; done
	rm -f /etc/profile.d/$(env_file)
	rm ${TEST_PATH_FILE}/common/WAA_TEST_FILE
clean:
	rm -f *~
