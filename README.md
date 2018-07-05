# Digital Library Development Sandbox

This sandbox contains experimental projects.


### Web applications and command line tools

+ [dataset](https://caltechlibrary.github.io/dataset), a Go package and command line tool for storing JSON documents in collections and buckets
+ [datatools](https://caltechlibrary.github.io/datatools), command line utilities for working with JSON, Excel Workbook and CSV data. Included are misc. command line utilities, useful in Bash scripts
+ [bibtex](https://caltechlibrary.github.io/bibtex), BibTeX package and command line tools
    + [web version](https://caltechlibrary.github.io/bibtex/webapp) of tools
+ [mkpage](https://caltechlibrary.github.io/mkpage), an experimental template and markdown processor, slide generator, web server and more
+ [caltechdata_read](https://github.com/caltechlibrary/caltechdata_read), extract data from CaltechDATA repository 
+ [caltechdata_plot](https://github.com/caltechlibrary/caltechdata_plot),
display a plot of data hosted in the CaltechDATA repository. Demo at [plots.caltechlibrary.org](plots.caltechlibrary.org) 
+ [namaste](https://caltechlibrary.github.io/namaste) an "Name as text" implementation in Go support local disc, S3 and Google Cloud Storage

### Harvesters and systems integration 

+ [cait](https://caltechlibrary.github.io/cait), Caltech Archives Integration Tools, ArchivesSpace harvesting tool for repository, accessions and agent objects
+ [eprinttools](https://caltechlibrary.github.io/eprinttools), ep is a Go package and provides _ep_ a tool to harvest EPrints via EPrint REST API supporting our [CaltechAUTHORS](http://authors.library.caltech.edu) and [CaltechTHESIS](http://thesis.library.caltech.edu) repositories
+ [orcidtools](https://caltechlibrary.github.io/orcidtools), is a Go package and provides _orcid_, an ORCID harvesting tool, for v2.0 of the [ORCID API](https://orcid.org/organizations/integrators/API)
+ [crossrefapi](https://caltechlibrary.github.io/crossrefapi), is a Go package for working politely with the [CrossRef API](https://api.crossref.org).

### Golang packages

+ [bibtex](https://github.com/caltechlibrary/bibtex), a package for working with BibTeX content
+ [tmplfn](https://github.com/caltechlibrary/tmplfn), a package for standardizing template functions across Go template projects
+ [cli](https://github.com/caltechlibrary/cli), a package for standardizing common cli options across Go based projects
+ [rss2](https://github.com/caltechlibrary/rss2), a package that can be used to work with RSS2 content

## PHP Libraries

+ [safer-php](https://github.com/caltechlibrary/safer-php), a little library for vetting input values in PHP based on pseudo types
+ [ep-php](https://github.com/caltechlibrary/ep-php), an EPrint 3.3 REST API library for easily retrieval of XML or JSON EPrint records based on EPrint ID
+ [eprintsDepositHelper](https://github.com/caltechlibrary/eprintsDepositHelper) a fork of https://github.com/davidfkane/eprintsDepositHelper

### Virtual machines and containers

+ [ArchivesSpace under Vagrant](https://github.com/caltechlibrary/archivesspace_vagrant)
+ [Caltech Library on Docker Hub](https://hub.docker.com/u/caltechlibrary)
+ [test-vm](https://github.com/caltechlibrary/test-vm), a minimal Vagrant VM based on Ubuntu Server 16.04 LTS
    + [setup-vireo.sh](https://raw.githubusercontent.com/caltechlibrary/test-vm/master/setup-vireo.sh), setup Vireo ETD 3
    + [setup-archivesspace.sh](https://raw.githubusercontent.com/caltechlibrary/test-vm/master/setup-archivesspace.sh), setup ArchivesSpace 1.4.2
    + [setup-eprints.sh](https://raw.githubusercontent.com/caltechlibrary/test-vm/master/setup-eprints.sh), setup EPrints 3.3.15

