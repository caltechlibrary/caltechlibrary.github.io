
### Harvesters and systems integration 

+ [eprinttools](https://caltechlibrary.github.io/eprinttools), is a Go package for working with EPrints API and EPrints XML
    + _ep_, a tool to harvest EPrints via EPrint REST API design specifically to work with [CaltechAUTHORS](http://authors.library.caltech.edu) and [CaltechTHESIS](http://thesis.library.caltech.edu)
    + _eputil_, a tool to harvest EPrints via EPrints REST API returning JSON output
    + _epfmt_, a tool for formatting validating/pretty printing/converting EPrint metadata to/from XML and JSON
    + _doi2eprintxml_, a command line tool that queries CrossRef and DataCite APIs for metadata returning EPrints XML output
    + _eprintxml2json_, a command line tool that transform EPrints 3.x EPrint XML to JSON
+ [eprints2bags](https://github.com/caltechlibrary/eprints2bags), is a Python program for downloading records from an EPrints server and creating [BagIt](https://en.wikipedia.org/wiki/BagIt)-style packages out of them
+ [orcidtools](https://caltechlibrary.github.io/orcidtools), is a Go package and provides _orcid_, an ORCID harvesting tool, for v2.0 of the [ORCID API](https://orcid.org/organizations/integrators/API)
+ [crossrefapi](https://caltechlibrary.github.io/crossrefapi), is a Go package for working politely with the public [CrossRef API](https://api.crossref.org). A command line tool returning JSON is also included in this repository.
+ [dataciteapi](https://caltechlibrary.github.io/dataciteapi), is a Go package for working with the public [DataCite API](https://api.datacite.org). A command line tool returning JSON is also included in this repository.

