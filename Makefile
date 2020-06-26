#
# A simple Makefile to generate caltechlibrary.github.io with
# shorthand.
#

BRANCH = $(shell git branch | grep -E "\* " | cut -d\   -f 2)

build: *.md page.tmpl
	./mk_website.py

clean:
	/bin/rm -f *.html

save:
	./mk_website.py
	if [ "$(msg)" != "" ]; then git commit -am "$(msg)"; else git commit -am "Quick Save"; fi
	git push origin $(BRANCH)

refresh:
	git fetch origin
	git pull origin $(BRANCH)

website:
	./mk_website.py

# We're not using publish.bash here because this website doesn't
# require publication via gh-pages branch.
publish:
	./mk_website.py
	git commit -am "Publishing website"
	git push origin main

