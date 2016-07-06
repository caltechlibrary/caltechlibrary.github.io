#
# A simple Makefile to generate caltechlibrary.github.io with
# shorthand.
#
index.html: index.md index.shorthand
	shorthand index.shorthand > index.html
