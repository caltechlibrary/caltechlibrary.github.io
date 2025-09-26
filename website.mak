#
# Makefile for running pandoc on all Markdown docs ending in .md
#
PROJECT = caltechlibrary.github.io

PANDOC = $(shell which pandoc)

# Setup for standate pages and posts

#MD_PAGES = $(shell ls -1 *.md posts/*/*/*/*.md | grep -v 'nav.md')
MD_PAGES = $(shell find . -type f | grep '\.md$$' | grep -v '.venv' | grep -v 'nav.md' | grep -v './presentations/')

#HTML_PAGES = $(shell ls -1 *.md posts/*/*/*/.md | grep -v 'nav.md' | sed -E 's/.md/.html/g')
HTML_PAGES = $(shell find . -type f | grep '\.md$$' | grep -v '.venv' | grep -v 'nav.md' | grep -v './presentations/' | sed -E 's/.md/.html/g')

# Setup for presentations
build: $(HTML_PAGES) $(MD_PAGES) rss.xml pagefind

$(HTML_PAGES): $(MD_PAGES) .FORCE
	if [ -f $(PANDOC) ]; then $(PANDOC) --metadata title=$(basename $@) -s --to html5 $(basename $@).md -o $(basename $@).html \
		--lua-filter=links-to-html.lua \
	    --template=page.tmpl; fi
	@if [ $@ = "README.html" ]; then mv README.html index.html; fi

$(HTML_PRESENTATIONS): $(MD_PRESENTATIONS) .FORCE
	pandoc -V lang=en -s -t $(SLIDE_FORMAT) $(basename $@).md -o $(basename $@).html
	git add $(basename $@).html

pagefind: .FORCE
	pagefind --verbose --exclude-selectors="nav,header,footer" --site .
	git add pagefind

clean:
	@if [ -f index.html ]; then rm *.html; fi

.FORCE:
