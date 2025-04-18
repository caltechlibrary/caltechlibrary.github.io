---
title: Building Web Components using Large Language Models
pubDate: 2025-03-13
author: R. S. Doiel
abstract: |
  A brief overview of an experiment resulting in <https://github.com/caltechlibrary/CL-web-components>.
  Two web components were developed that use a progressive enhancement approach, CSVTextarea and A_to_ZUL.
keywords:
  - web components
  - browsers
  - HTML
  - CSS
  - JavaScript
  - LLM
---

# Building Web Components using Large Language Models

by R. S. Doiel, 2025-03-13

I started playing around with Mitral Chat to create web components for some library applications.  It’s a non-trivial process, not sure it is faster than me just write them from scratch but I am so far happy with the results which you can see <https://github.com/caltechlibrary/CL-web-components>.  There are two, one is called “a_to_z_ul.js” which lets you wrap a simple UL list and have it be an “A to Z” list. The second is call “csvtextarea.js” which is a component that wraps a TEXTAREA input element that contains CSV data and renders a table where you can edit the cells.  The wrapping of existing components was not the LLM’s suggestion, that was my idea but the generated JavaScript is from the LLM based on my prompts.

One of the challenges I ran into was the lack of reproducibility even for the same prompts. The second was I had to use a paid subscription to Mistral as the free one available from DuckDuckGo wasn’t enough. I compared a few other LLM as I learned to use the chat interface and Mistral price for results was the best for my tests.

After getting a feel for using Mistral I tried running the original prompts against Mistral using Ollama. The results are different. It is cleared the “paid” platforms of open sourced models have significant enhancements in the models.

I worry about the energy consumed in running the models let along refining them.

While I like the results I got for this specific test I am on the fence about the general usefulness for libraries, archives and museums.
