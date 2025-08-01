#
# A simple Makefile to generate caltechlibrary.github.io with
# shorthand.
#

BRANCH = $(shell git branch | grep -E "\* " | cut -d\   -f 2)

build: website

project_index: .FORCE
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
	flatlake
	flt posts rss api/all/page-1.json >rss.xml
	flt posts markdown api/all/page-1.json >blog.md
	make -f website.mak

# NOTE: I'm not using publish.bash here because this website doesn't
# require publication via gh-pages branch. Publish in this case
# Just makes sure the project index is updated (takes a while before a push)
publish: project_index save
	git push origin main

.FORCE:
