#
# A simple Makefile to generate caltechlibrary.github.io with
# shorthand.
#

BRANCH = $(shell git branch | grep "* " | cut -d\   -f 2)

build: *.md page.tmpl
	./mk-website.bash

clean:
	/bin/rm -f *.html

save:
	./mk-website.bash
	git commit -am "Publishing website"
	git push origin $(BRANCH)

refresh:
	git fetch origin
	git pull origin $(BRANCH)

website:
	./mk-website.bash

# We're not using publish.bash here because this website doesn't
# require publication via gh-pages branch.
publish:
	./mk-website.bash
	git commit -am "Publishing website"
	git push origin master

