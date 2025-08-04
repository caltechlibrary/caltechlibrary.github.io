---
title: Language models and "fielded" search
author: rsdoiel@caltech.edu (R. S. Doiel)
datePublished: 2025-04-10
keywords:
 - LLM
 - search
---

# Language models and "fielded" search

By R. S. Doiel, 2025-04-10

This an interesting use of an LLM, it means that the old "advanced search" UI or fielded search UI can be made to feel like a single box search, <https://simonwillison.net/2025/Apr/9/an-llm-query-understanding-service/ >. From Simon Willison's Weblog,

> "Many times, even a small open source LLM will be able to turn a search query into reasonable structure at relatively low cost."

So does this mean the huge Solar/OpenSearch indexes aren't needed?  Probably not but it does mean that we can build much more effective search and retrieval systems before requiring a full text search engine. Running an Ollama instance with an appropriate frugal model is almost trivial.
