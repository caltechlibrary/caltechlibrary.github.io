---
title: "Getting started with Go"
author: "R. S. Doiel, <rsdoiel@caltech.edu>"
abstract: |
  This is a presentation of a blog post I write for a Brown Bag Meetup
institute: |
  Caltech Library,
  Digital Library Development
description: workshop presentation
slidy-url: .
css: styles/sea-and-shore.css
createDate: 2025-09-26
updateDate: 2025-09-26
pubDate: 2025-09-26
place: Caltech Library (Zoom)
date: 2025-09-26
section-titles: false
toc: true
keywords: [ "Go" ]
url: "https://caltechlibrary.github.io/presentations/getting_started_with_go.html"
---

# Welcome to "Getting started with Go"

Welcome everyone,

This presentation is based on a blog post I wrote [Getting started with Go](https://rsdoiel.github.io/blog/2025/09/22/getting_started_with_go.html)

# What we'll learn

- How to install the Go tool chain
- How to use the Go command
- Compile and run three programs
  - hello world
  - a simple web server
  - create a Markdown server

# What you'll need know

- A computer with a Terminal program
- Your favorite text editor
- Basic knowledge of your operating system (you need to be able to install Go)

# Installing Go compiler and tool chain

Go to the URL, the Go for your computer and operating system.

  <https://go.dev/dl/>

Follow the instructions to install it.

# Begin with Hello World

- open a Terminal session
- create a directory called "helloworld"
- change to that directory, `cd helloworld`
- create a file called [helloworld.go](https://rsdoiel.github.io/blog/2025/09/22/helloworld/helloworld.go)

# Source Code

~~~go
package main

import (
    "fmt"
) 

func main() {
    fmt.Println("Hello World!")
}
~~~

# Running Hello World

~~~shell
go run helloworld.go
~~~

# Compiling Hello World

~~~shell
go build helloworld.go
~~~

Congratulations!

# Continuing with a Web Server

- create a new directory called webserver
- change into the directory called webserver
- create a file called [webserver.go](https://pkg.go.dev/net/http#example-FileServer-DotFileHiding)

# Source Code

See <https://pkg.go.dev/net/http#example-FileServer-DotFileHiding>

# Run Web Server

~~~shell
go run webserver.go
~~~

# Compile Web Server

~~~shell
go build webserver.go
~~~

# Things to notice

- documentation website for Go package
- http is a standard package
- Good packages have example code
- You have a handy little (fast) static web server

# Wrapping up, putting things together

- Create our own package
- Create a Markdown server using both a standard and 3rd party package

# mdserver

- open a Terminal session
- create a directory called "mdserver"
- create a directory called "cmd/mdserver"

# Download and create the following files

- [markdown.go](https://rsdoiel.github.io/blog/2025/09/22/mdserver/markdown.go)
  - <https://rsdoiel.github.io/blog/2025/09/22/mdserver/markdown.go>
- [handler.go](https://rsdoiel.github.io/blog/2025/09/22/mdserver/handler.go)
  - <https://rsdoiel.github.io/blog/2025/09/22/mdserver/handler.go>
- [main.go](https://rsdoiel.github.io/blog/2025/09/22/mdserver/cmd/mdserver/main.go)
  - <https://rsdoiel.github.io/blog/2025/09/22/mdserver/cmd/mdserver/main.go>
  - put this in in the "cmd/mdserver/" directory

# Initialize your package

~~~shell
go mod init 'github.com/caltechlibrary/mdserver'
go mod tidy
~~~

# Pull in the goldmark package (Markdown)

~~~shell
go get "github.com/yuin/goldmark"
~~~

We use "go get" because this is not a standard library package.

# Create a Markdown document to test with

~~~Markdown

# Hello World

This isn't HTML but you'll see HTML using mdserver
~~~

Save this as helloworld.md

# Run mdserver

~~~shell
go run cmd/mdserver/main.go
~~~

# Compile mdserver

~~~shell
go build -o bin/mdserver cmd/mdserver/main.go
~~~

# Next steps

- Review this presentation, <https://caltechlibrary.github.io/presentations/getting_started_with_go.html>
- Read blog post, <https://rsdoiel.github.io/blog/2025/09/22/getting_started_with_go.html>
- <https://go.dev/learn/>
- <https://pkg.go.dev/>


