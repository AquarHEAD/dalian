The Dali'an Project
=====

Introduction
-----

"Dali'an" is the heroine's name from "Dantalian no Shoka"(「ダンタリアンの書架」),
she is the manager of the demon's library, and this project intends to be my
entrance for the great library of Internet, and a replacement to those
about:blank or google.com in my browsers.

Features
-----

- Bookmarks (with categories and archive function)
- Random quotes
- Gmail check
- Notes (in development)
- Tweets (to-do)
- WEB activities integeration (to-do)

LOCAL SETUP & TEST-
-----

1. 	```
	git clone git://github.com/AquarHEAD/dalian.git
	```
2. 	```
	cp settings.py.example settings.py
	```
3. 	fill the settings
4. 	create database
5. 	```
	python manage.py syncdb  
	python manage.py runserver
	```
6. 	open http://127.0.0.1

Deploy on DotCloud-
-----

1. 	signup [dotcloud](https://www.dotcloud.com/) and set it up
2. 	```
	dotcloud create dalian
	```
3. 	```
	git clone git://github.com/AquarHEAD/dalian.git  
	cd dalian  
	cp settings.py.example settings.py.dotcloud  
	```
4. 	fill the settings
5 	```
	make
	```
6. 	you can add your custom domain
	```
	dotcloud alias add dalian.www xxx.example.com
	```
7.	set your browser's default homepage
