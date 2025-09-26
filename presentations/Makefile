
# Build the following Pandoc presentations

SLIDE_FORMAT = slidy

MD_PAGES = $(shell ls -1 *.md)
HTML_PAGES = $(shell ls -1 *.md | sed -E 's/.md/.html/g')

build: $(HTML_PAGES)

$(HTML_PAGES): $(MD_PAGES) .FORCE
	pandoc -V lang=en -s -t $(SLIDE_FORMAT) $(basename $@).md -o $(basename $@).html
	git add $(basename $@).html

.FORCE:
