deploy: settings.py.dotcloud
	mkdir ../dotcloud_tmp
	mkdir ../dotcloud_tmp/dalian
	cp -a . ../dotcloud_tmp/dalian
	mv ../dotcloud_tmp/ .
	mv dotcloud_tmp/dalian/dotcloud_conf/* dotcloud_tmp/
	rm -f dotcloud_tmp/dalian/settings.py
	mv dotcloud_tmp/dalian/settings.py.dotcloud dotcloud_tmp/dalian/settings.py
	dotcloud push dalian dotcloud_tmp
	rm -rf dotcloud_tmp
