/**
 * prototyp1.js - adding keyboard nave to CSS hover events.
 */
(function (document) {
    'use strict';
    var navAnchor = document.querySelector('nav a'),
        asideAnchor = document.querySelector('aside a'),
        caltechAuthorsURL = 'http://authors.library.caltech.edu/cgi/search/archive/advanced/export_caltechauthors_RSS2.xml?screen=Search&dataset=archive&_action_export=1&output=RSS2&exp=0%7C1%7C-date%2Fcreators_name%2Ftitle%7Carchive%7C-%7Cispublished%3Aispublished%3AANY%3AEQ%3Apub%7Ctype%3Atype%3AANY%3AEQ%3Aarticle+book+book_section+monograph+conference_item%7C-%7Ceprint_status%3Aeprint_status%3AANY%3AEQ%3Aarchive%7Cmetadata_visibility%3Ametadata_visibility%3AANY%3AEQ%3Ashow&n=5',
        libraryNewsURL = 'http://library.caltech.edu/news/index.php/feed';

    console.log('DEBUG prototype1.js');

    function removeClassName(staleClassName) {
        var elem = document.querySelectorAll('.' + staleClassName),
            className = '',
            i = 0;
        
        for (i = 0; i < elem.length; i += 1) {
            className = elem[i].className || '';

            if (className !== '') {
                elem[i].className = className.replace(staleClassName, '').trim();
            } 
        }
    }

    function openNav(ev) {
        var navUl = document.querySelectorAll('nav ul'),
            className = '',
            i = 0;
        
        for (i = 0; i < navUl.length; i += 1) {
            className = navUl[i].className;
            if (className === '' || className.indexOf('cl-nav-ul-display-inline-block') < 0) {
                navUl[i].className = (className + ' cl-nav-ul-display-inline-block').trim();
            } 
        }
    }

    function openAside(ev) {
        var asideUl = document.querySelectorAll('aside div ul'),
            className = '',
            i = 0;

        console.log('DEBUG asideUl', asideUl);
        for (i = 0; i < asideUl.length; i += 1) {
            className = asideUl[i].className;
            console.log("DEBUG className before", className);
            if (className === '' || className.indexOf('cl-aside-display-block') < 0) {
                asideUl[i].className = (className + ' cl-aside-display-block').trim();

            } 
            console.log("DEBUG className after", asideUl[i].className);
        }
        console.log('DEBUG openAside');
    }


    function appendRSS(url, selector, className) {
        var elem = document.querySelector(selector),
            request = new XMLHttpRequest();

        function response() {
            var doc = this.responseXML,
                items = doc.querySelectorAll('item'), 
                i = 0,
                title = '',
                url = '',
                description = '',
                parts = [];
            console.log('DEBUG appendRSS() responseXML', this.responseXML, ' item count ', items.lenght);
            for (i = 0; i < items.length; i += 1) {
                console.log('DEBUG item', items[i]);
                title = items[i].getElementsByTagName("title")[0].textContent || '';
                url = items[i].getElementsByTagName("link")[0].textContent || '';
                description = items[i].getElementsByTagName("description")[0].textContent || '';
                //FIXME: when template strings are support in IE and Edge then convert to template strings.
                parts.push([
                    '<div class="', 
                    className,
                    '"><h1><a href="', 
                    url, 
                    '">', 
                    title, 
                    '</a></h1><div>', 
                    description, 
                    '</div></div>'
                ].join(''));
            }
            elem.innerHTML = parts.join('');
        }

        request.addEventListener('load', response);
        request.open('GET', url);
        request.responseType = 'document';
        request.send();
        console.log('DEBUG appending ', url, ' to ', selector);
    }

    navAnchor.addEventListener('focus', openNav, false);
    asideAnchor.addEventListener('focus', openAside, false);
    appendRSS(caltechAuthorsURL, '#cl-caltech-authors', 'cl-authors-item');
    appendRSS(libraryNewsURL, '#cl-library-news', 'cl-news-item');
}(document));
