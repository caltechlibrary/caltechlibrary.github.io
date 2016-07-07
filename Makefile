#
# A simple Makefile to generate caltechlibrary.github.io with
# shorthand.
#
index.html: index.md index.shorthand
	shorthand index.shorthand > index.html

publish:
	shorthand index.shorthand > index.html
	git commit -am "Publishing website"
	git push origin master

