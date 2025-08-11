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
            {
                bundlePath: "https://caltechlibrary.github.io/datatools/pagefind",
                baseUrl: "/datatools/",
            },
            {
                bundlePath: "https://caltechlibrary.github.io/dataset/pagefind",
                baseUrl: "/dataset/",
            },
            {
                bundlePath: "https://caltechlibrary.github.io/irdmtools/pagefind",
                baseUrl: "/irdmtools/",
            },
            {
                bundlePath: "https://caltechlibrary.github.io/cold/pagefind",
                baseUrl: "/cold/",
            },
            {
                bundlePath: "https://caltechlibrary.github.io/CMTools/pagefind",
                baseUrl: "/CMTools/",
            },
            {
                bundlePath: "https://caltechlibrary.github.io/metadatatools/pagefind",
                baseUrl: "/metadatatools/",
            },
            {
                bundlePath: "https://caltechlibrary.github.io/CL-web-components/pagefind",
                baseURL: "/CL-web-components/",
            },
            {
                bundlePath: "https://caltechlibrary.github.io/CL-Pandoc-filters/pagefind",
                baseURL: "/CL-Pandoc-filters/",
            }
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

