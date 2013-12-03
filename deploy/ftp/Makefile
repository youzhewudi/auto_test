target = ftp_client ftp_server
default:
	for i in $(target); \
	do \
	{ cd $$i && \
	  $(MAKE) && \
	  cd -; \
	 } || exit "$$?" ; \
	done;
install:
	for i in $(target); \
	do \
	$(MAKE) -C $$i install; \
	done
uninstall:
	for i in $(target); \
	do \
	$(MAKE) -C $$i uninstall; \
	done
clean:
	for i in $(target); \
	do \
	$(MAKE) -C $$i clean; \
	done
	rm -f *~
