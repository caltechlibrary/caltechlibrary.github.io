#
# A simple Makefile to generate caltechlibrary.github.io with
# shorthand.
#

BRANCH = $(shell git branch | grep -E "\* " | cut -d\   -f 2)

build: website

generated_pages: .FORCE
	./mk_project_index.py caltechlibrary project_index.md

clean: .FORCE
	rm -f *.html

save: website
	make -f website.mak
	if [ "$(msg)" != "" ]; then git commit -am "$(msg)"; else git commit -am "Quick Save"; fi
	git push origin $(BRANCH)

refresh: .FORCE
	git fetch origin
	git pull origin $(BRANCH)

website: .FORCE
	make -f website.mak

# We're not using publish.bash here because this website doesn't
# require publication via gh-pages branch.
publish: save
	git commit -am "Publishing website"
	git push origin main

.FORCE:
