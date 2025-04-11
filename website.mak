#
# Makefile for running pandoc on all Markdown docs ending in .md
#
PROJECT = caltechlibrary.github.io

PANDOC = $(shell which pandoc)

#MD_PAGES = $(shell ls -1 *.md posts/*/*/*/*.md | grep -v 'nav.md')
MD_PAGES = $(shell find . -type f | grep '\.md$$' | grep -v 'nav.md')

#HTML_PAGES = $(shell ls -1 *.md posts/*/*/*/.md | grep -v 'nav.md' | sed -E 's/.md/.html/g')
HTML_PAGES = $(shell find . -type f | grep '\.md$$' | grep -v 'nav.md' | sed -E 's/.md/.html/g')


build: $(HTML_PAGES) $(MD_PAGES) rss.xml pagefind

$(HTML_PAGES): $(MD_PAGES) .FORCE
	if [ -f $(PANDOC) ]; then $(PANDOC) --metadata title=$(basename $@) -s --to html5 $(basename $@).md -o $(basename $@).html \
		--lua-filter=links-to-html.lua \
	    --template=page.tmpl; fi
	@if [ $@ = "README.html" ]; then mv README.html index.html; fi

rss.xml: .FORCE
	  pttk rss --atom-link="https://caltechlibrary.github.io/rss.xml" \
                      -base-url="http://caltechlibrary.github.io" \
                      -channel-title="Caltech Library, Digital Library Development" \
                      -channel-description="A sandbox of development" \
                      -channel-link="https://caltechlibrary.github.io" \
            posts >rss.xml

pagefind: .FORCE
	pagefind --verbose --exclude-selectors="nav,header,footer" --site .
	git add pagefind

clean:
	@if [ -f index.html ]; then rm *.html; fi

.FORCE:
