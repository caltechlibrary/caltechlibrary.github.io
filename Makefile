#
# A simple Makefile to generate caltechlibrary.github.io with
# shorthand.
#
build: README.md page.tmpl
	./mk-website.bash

save:
	git commit -am "quick save"
	git push origin master

clean:
	/bin/rm -f *.html

# We're not using publish.bash here because this website doesn't
# require publication via gh-pages branch.
publish:
	./mk-website.bash
	git commit -am "Publishing website"
	git push origin master

