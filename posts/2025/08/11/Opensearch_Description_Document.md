---
title: OpenSearch Description Documents
abstract: >
  This post explains the OpenSearch Description Document and how to integrate it
  for a website using PageFind. It touches on how to use site search defined by
  the OpenSearch Description Document in Firefox, Safari and Chrome. 
author: rsdoiel@caltech.edu (R. S. Doiel)
dateCreated: 2025-08-08T00:00:00.000Z
dateModified: '2025-08-11'
keywords:
  - site search
  - opensearch description document
  - pagefind
  - web browser
datePublished: '2025-08-11'
copyrightYear: 2025
copyrightHolder: California Institute of Technology
---

# OpenSearch Description Documents: What, Why and How

By R. S. Doiel, 2025-08-11

With the steady declining most commercial search engines over the last decade my interest in site specific search has been grown. When the web was young search meant site search.  Overtime search as a service arrived where it is considered an integral part of the web. The trouble now is that commercial search isn't about finding the thing you are looking forward it is about selling attention and surveillance. While systems like Google Scholar still exist the question that nags at me is for how long? What are out options today?

Site search didn't disappear. It lives in content management systems like Drupal and WordPress. It lives in library systems like ArchivesSpace and Invenio RDM. It isn't the new hotness but it works pretty good. As libraries and archives continue the trend of taking advantage of static web site implementations site search can live there too.  This begs the question, how can we make it more convenient than maintaining a bookmark list and always going directly to the site to retrieve results?

We're in luck! An old solution to exposing site search in the web browser remains supported today. [OpenSearch Description Documents](https://en.wikipedia.org/wiki/OpenSearch_(specification) "this is about the OpenSearch Description document to not the Amazon sponsored Open Source project") is a specification that dates back to 2005. It is not a coincidence that the Omnibox arrives by 2008. The humble URL box is the thing we use to navigate the web. It's the on ramp. It's also where search starts for most people. The specification for OpenSearch Description Documents is a specification to make that possible.

It is important not to confuse **OpenSearch Description Document** with OpenSearch the fork by Amazon of ElasticSearch. It is a simple XML document that can be used by Firefox, Safari and Chrome to include your site search as a search engine (NOTE: Safari and Chrome browser make you jump through a few hoops before it sites along side Google, DuckDuckGo and the others).  The really nice thing about take the effort with Safari and Chrome is that you don't need to navigate to the website to take advantage of site search. Anytime you are in the URL box (Omnibox) it's right there ready to be used.

There are three parts to the dance of making your URL Box (Omnibox) gain first class status along side commercial search.

1. You need an OpenSearch Description Document (XML file) on your site
2. You need to include a link to it in the head element of your search web page (or other HTML pages)
3. You need to have a search engine to link to that can response to a URL and return results

## What does the OpenSearch Description Document Look Like?

The OpenSearch Description Document is a short XML document with a few required fields. Here's a short version.

~~~XML
<?xml version="1.0" encoding="UTF-8"?>
<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
  <ShortName>DLDLabs</ShortName>
  <Description>Search Caltech Library DLD Labs</Description>
  <Url type="text/html" method="get" template="https://caltechlibrary.github.io/search.html?q={searchTerms}"/>
  <InputEncoding>UTF-8</InputEncoding>
  <Image height="16" width="16">https://caltechlibrary.github.io/favicon.ico</Image>
</OpenSearchDescription>
~~~

The outer XML element is the **OpenSearchDescription**. Inside it you include a **ShortName**, **Description**, **Url**,
**InputEncoding** and **Image** elements. The last two are optional but I think are helpful.  In the DLD Labs website I've called this document "osd.xml" but you can name it whatever you like. The link element you include in the head element of HTML pages is what lets the web browser know it is available.

**OpenSearchDescription**
: The outer XML element holding the details about your search service.

**ShortName**
: This is a short, less than 14 alpha numeric characters used to refer to your search service.

**Description**
: This is an up to 1024 character description of your search service.

**Url**
: This describes the URL template needed to form a search URL. The `{searchTerms}` is replaced with the query terms taken from the URL box or Omnibox

**InputEncoding**
: This sets the character encoding your search engine supports, UTF-8 is the likely choice you want.

**Image**
: This is the image associated with your search. Browser may display it when you URL Box/Omnibox is set to search your site.

## How do I link your OpenSearch Description Document to your web page?

If you have an **OpenSearch Description Document** available you need to point to it from a web page. All you need is a simple link element in the head of the HTML page. Here's the link used on the DLD Labs site.

~~~html
<link rel="search" type="application/opensearchdescription+xml" href="https://caltechlibrary.github.io/osd.xml" title="Search DLD Labs">
~~~

In the link we use the "rel", "type", "href" and "title" attributes to connect the page with the OpenSearch Description Document (abbr. OSD). Once the OSD document is linked it can be discovered by the web browser. In this case it tells the browser the OSD document can be found at "https://caltechlibrary.github.io/osd.xml".

### Trouble shooting OSD

An important think to remember of the OpenSearch Description Document is that it is XML. XML, unlike HTML, isn't forgiving. If you have a mismatched quote or a type in an element name it's not going to work. 

The Mozilla Developer Network maintains excellent documentation on the specification at <https://developer.mozilla.org/en-US/docs/Web/XML/Guides/OpenSearch>.

## Adding your site search to your web browser

### Firefox

Firefox works seamlessly with OSD documents.  You land on a web page where it is linked in. If you clear the URL Box and pull down the list of available search engines, newly discovered on appear at the top.

![Picture of the pull down for search choices](FireFox_URL_Box.png)

The image on the left with the downward caret is the menu that exposes the search options. Click on it and you'll see the list. If you see an icon with a plus symbol overlayed in the upper right of the icon it's a new search you can add to the ones available. Clicking on it will add it as an option to your web browser.

You can also add a search engine by going to <about:preferences#search>, scroll down to Search Shortcuts and press the "add" button. This will let you add the search manually.

### Safari

Safari has locked down this feature but still supports it. Apple just makes it hard to find and change it.

1. Open the URL of the page that links to the OpenSearch Description Document
2. Go to the Safari menu, click on settings
3. Click on Search
4. Make sure "Enable Quick Website Search" is checked

If this is enabled you can now type in the host-name of the website, a space followed by your search terms. Bingo you're now search the website.

### Chrome

Chrome requires the most steps to enable your site search. This is not surprising given the parent company. 

1. Open the URL of the page that links to the OpenSearch Description Document
2. Click on Chrome's menu and open the settings
3. Click on Search Engine
4. Just below the box where you set your default search engine is a box labeled "Manage search engines and site search", click on it.
5. Scroll way down on the page and you should see the new site search in the "Inactive Shortcuts" list. Click the button labeled "activate" for your site search.

The last step will move the site search list. There will be a pencil icon on the right side. You can give it a shortcut name by clicking on the pencil, e.g. "@dldlbs" is what I use for searching DLD Labs site from Chrome's Omnibox.


## Integrating site search for static websites

If you have Solr, ElasticSearch, Drupal, WordPress, ArchivesSpace, Invenio RDM or EPrints search is running on your server someplace. What about your static website?  Do you have to run a separate search service?  No unless your site has multiple hundreds of thousands of pages to search.

With the rise in popularity of static websites since 2010s browser side search has become an option. Around 2011 [Oliver Nightingale](https://github.com/olivernn) pioneered browser side search with [LunrJS](https://lunrjs.com). More recently [CloudCannon](https://cloudcannon.com/), created an Open Source tool called [PageFind](https://pagefind.app). This takes the LunrJS approach and adds rockets. LunrJS could support up to about 10,000 pages before it really bogged down. PageFind goes way beyond that. PageFind can even integrated search indexes across multiple website! Here's an example of the MDN website's search implemented with PageFind, <https://mdn.pagefind.app/>.

PageFind has good [documents](https://pagefind.app/docs) for setting up a simple search page. It works well. Open the URL of the search page, you are presented with a search box, type in a search and you get results.  The problem is the page's URL doesn't let you go straight to search results.  There's an easy fix for that.   When the page loads the same JavaScript you use to enable the search page to work can also check the URL's query parameters for a query field and search term. Example <https://caltechlibrary.github.io/search.html?q=dataset%20web%20components>. This has two benefits

1. You can use it as a pattern as a template in the OpenSearch Description Document in the **Url** element. 
2. You can bookmark search results

### Setting up PageFind to support URL search queries

Basically want to implement two things beyond the default PageFind example.  We need to retrieve the query parameter. I'm using the field "q" because that is a common idiom for most site search systems.  If that field is present and populated then we need to "triggerSearch" in the PageFindUI object.  The second thing is when we're typing in the web form the URL should update just before the search results are fetched. That is done by adding a "processTerm" hook when we configure the PageFundUI object.

Here's a simple version of the JavaScript we run on DLD Lab's search.html page.

~~~JavaScript
// Import PageFindUI

// Function to extract query parameters from the URL
function getQueryParam(name) {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get(name);
}

// Extract the query parameter
const searchQuery = getQueryParam('q');

// Function to update the URL with the search query
function updateURLWithQuery(query) {
  const newUrl = new URL(window.location.href);
  newUrl.searchParams.set('q', query);
  window.history.pushState({ path: newUrl.href }, '', newUrl.href);
}

// When the page is fully loaded setup the PageFindUI object
window.addEventListener('DOMContentLoaded', (event) => {
    const searchUI = new PagefindUI({
        element: "#search",
        highlightParam: "highlight",
        mergeIndex: [
            {
                bundlePath: "https://caltechlibrary.github.io/pagefind",
                baseUrl: "/"
            },
        ],
        processTerm: (term) => {
            updateURLWithQuery(term);
            return term;
        }
    });

    if (searchQuery) {
        searchUI.triggerSearch(searchQuery);
    }
});
~~~

If you wanted to integrate you're own PageFind search that supports query URL you could use this code but replace the "bundlePath" with the URL to your website's PageFind indexes. You can see the expanded version of our implementation at <https://caltechlibrary.github.io/modules/search.js>. In our implementation we also support searching the documentation sites for some of our projects.

## More arguments for browser side search

When the search engine runs on the server you're at the mercy of the people who control the server. Searches are a treasure trove for the surveillance economy. With PageFind the search runs in your browser. It only leaves your browser to select the next partial index needed.  This significantly reduces the exposed data. You might be able to infer a set of search terms but you're not going to see the specific search string typed in.
 
### What is Page Find doing differently?

PageFind, the command line program, is run after you stage your website but before you publish it. It crawls the HTML pages on disk and extracts the content you identified to be in included in your search indexes. PageFind, unlike LunrJS, does not encode the index as JSON. Instead is includes the indexes as a sequence of WASM (Web Assembly) files. This allows for dense indexes. Another step that sets PageFind apart is the indexes generated are partitioned. You don't download all indexes to the browser only the ones you need to based on the search terms.  When you stop typing for a moment PageFind JavaScript running in your web browser figures out which indexes are useful next and retrieves.  Clever stuff.

When we add support for using a query URL PageFind only sends the query on page load. This does mean you're going to wait for the indexes to be retrieved based on the completed query string. That delay is noticeable but I think a reasonable trade off.

## Why is the OpenSearch description document important?

As researchers, archivist, librarians and users of the research materials skipping the ad-tech of Google et el means smoother workflows when looking things up on line. It also means websites that are focused on our specific research interests can be used as a primary search resource if they include the description of their site search.  While being able to type in the URL Box might seem like   a convenience it's the small user interface improvement that when understood can smooth out flow of retrieving research resources online. This is true regardless of with or not the site is a "dynamic" website (e.g. WordPress, RDM, ArchivesSpace) or a static one (e.g. "cell atlas").