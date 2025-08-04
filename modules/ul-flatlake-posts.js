/**
 * ul-flatlake-posts.js is a module that uses a FlatLake JSON API to display recent posts.
 */

// Helper function to extract the name from an author field
function nameFromAuthorField(author) {
    const regex = /\(([^)]+)\)/;
    const match = author.match(regex);
    return match ? match[1] : author;
}

// Helper function to create a byline from author and date
function byLine(author, datePublished) {
    let parts = [];
    if (author !== '') {
        parts.push(nameFromAuthorField(author));
    }
    if (datePublished !== '') {
        parts.push(`(${datePublished})`);
    }
    if (parts.length > 0) {
        parts.unshift('by');
    }
    return parts.join(' ').trim();
}

// Web component class definition
class UlFlatLakePosts extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
    }

    async connectedCallback() {
        this.hrefApi = this.getAttribute('href-api') || 'api/posts/all/page-1.json';
        this.maxItems = parseInt(this.getAttribute('max-items')) || 5;
        this.hrefCss = this.getAttribute('href-css');
        this.listIntro = this.getAttribute('list-intro') || '';

        await this.loadStylesheet();
        await this.fetchPosts();
    }

    async loadStylesheet() {
        if (this.hrefCss) {
            try {
                const response = await fetch(this.hrefCss);
                if (!response.ok) {
                    throw new Error(`Failed to fetch stylesheet: ${response.status} ${response.statusText}`);
                }
                const cssText = await response.text();
                const style = document.createElement('style');
                style.textContent = cssText;
                this.shadowRoot.appendChild(style);
            } catch (error) {
                console.error('Error loading stylesheet:', error);
            }
        }
    }

    async fetchPosts() {
        try {
            const response = await fetch(this.hrefApi);
            if (!response.ok) {
                throw new Error(`Failed to fetch posts: ${response.status} ${response.statusText}`);
            }
            const data = await response.json();
            this.renderPosts(data.values.slice(0, this.maxItems));
        } catch (error) {
            console.error('Error fetching posts:', error);
            this.shadowRoot.innerHTML = `<p>Error loading posts: ${error.message}</p>`;
        }
    }

    renderPosts(posts) {
        const ul = document.createElement('ul');
        if (this.listIntro) {
            const listIntro = document.createElement('div');
            listIntro.innerHTML = this.listIntro; 
            ul.appendChild(listIntro)
        }

        posts.forEach(post => {
            const datePublished = post.data?.datePublished || '';
            const title = post.data?.title || '';
            const url = post.url ? post.url.replace(/\.json$/g, '.html') : '#';
            const li = document.createElement('li');

            let titleElement;
            if (url && title) {
                const a = document.createElement('a');
                a.href = url;
                a.textContent = title;
                titleElement = a;
            } else {
                titleElement = document.createElement('span');
                titleElement.textContent = title || url || 'No title';
            }

            li.appendChild(titleElement);

            const byLineElem = document.createElement('div');
            byLineElem.textContent = byLine(post.data?.author || '', datePublished);
            li.appendChild(byLineElem);

            if (post.data?.abstract) {
                const abstract = document.createElement('div');
                abstract.textContent = post.data.abstract;
                li.appendChild(abstract);
            }

            if (post.data?.keywords && post.data.keywords.length > 0) {
                const keywords = document.createElement('div');
                keywords.textContent = `tags: ${post.data.keywords.join(", ")}`;
                li.appendChild(keywords);
            }

            ul.appendChild(li);
        });

        this.shadowRoot.appendChild(ul);
    }
}

// Define the custom element
customElements.define('ul-flatlake-posts', UlFlatLakePosts);
