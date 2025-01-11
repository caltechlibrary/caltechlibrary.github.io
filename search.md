
# Search


<link href="/pagefind/pagefind-ui.css" rel="stylesheet">

<script src="/pagefind/pagefind-ui.js"></script>

<p>

<div id="search"></div>

<p>

<script>
new PagefindUI({
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
            bundlePath: "https://caltechlibrary.github.io/ts_dataset/pagefind",
            baseUrl: "/ts_dataset/",
        },
        {
            bundlePath: "https://caltechlibrary.github.io/dataset/pagefind",
            baseUrl: "/dataset/",
        },
        {
            bundlePath: "https://caltechlibrary.github.io/newt/pagefind",
            baseUrl: "/newt/",
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
        }
    ]
})
</script>

This is an experimental search of select Caltech Library GitHub Projects sites.
