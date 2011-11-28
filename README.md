The Dali'an Project
=====

Introduction
-----

"Dali'an" is the heroine's name from "Dantalian no Shoka"(「ダンタリアンの書架」),
she is the manager of the demon's library, and this project intends to be my
entrance for the great library of Internet, and a replacement to those
about:blank or google.com in my browsers.

Publicly featuring bookmarks for quick reference and access on others computers
and activities which combines rss/oauth news updates from my frequent visited
social-alike websites.

Privately (after logged in) featuring bookmarks /w readlist-style feature and
a place to quickly collect piece of ideas (in text format), can also be used
as todo-list.

LOCAL SETUP & TEST-
-----

1. 	```bash
	git clone git://github.com/AquarHEAD/dalian.git
	```
2. 	```bash
	cp settings.py.example settings.py
	```
3. 	fill the settings
4. 	create database
5. 	```bash
	python manage.py syncdb
	python manage.py runserver
	```
6. 	open http://127.0.0.1 in your browser

Deploy on DotCloud-
-----

>signup dotcloud and install the CLI
>dotcloud create dalian
>clone this git repo and cd into it
>copy settings.py.example to settings.py.dotcloud and fill it out
>make
>dotcloud alias add dalian.www xxx.example.com
>set your browser's default homepage and
>enjoy :D
