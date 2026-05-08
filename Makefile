#
# A simple Makefile to generate caltechlibrary.github.io with
# shorthand.
#

BRANCH = $(shell git branch | grep -E "\* " | cut -d\   -f 2)

build: website presentations

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
	flt rss posts api/all/page-1.json >rss.xml
	flt markdown posts api/all/page-1.json >blog.md
	make -f website.mak

presentations: .FORCE
	cd presentations && make

.FORCE:
