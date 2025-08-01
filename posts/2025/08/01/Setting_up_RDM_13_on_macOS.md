---
dateCreated: '2025-08-01'
title: Setting up RDM 13 on macOS M1 Mac Mini
author: rsdoiel@caltech.edu (R. S. Doiel)
abstract: >
  This is a summary of the steps I took to successfully setup RDM 13 on my M1
  Mac Mini running macOS 15.6. I use Mac Ports for dependencies.
datePublished: '2025-08-01'
keywords:
  - Invenio
  - RDM
dateModified: '2025-08-01'
---

# Setting up RDM 13 on macOS

This is a summary of my experience bringing up a vanilla Developer Invenio RDM 13 experience on macOS 15.6 running on a M1 Mac Mini. I use Mac Ports for supporting development.  I use uv to manage Python.

The instructions I was following are found at <https://inveniordm.docs.cern.ch/install/>. I am doing a "developer" setup.

If you run into problems I highly recommend making sure you have a "clean" system before proceeding. This is especially true if you've had more than one version of Python on your machine (regardless of how), installed RDM in the past or have had older versions of Docker Desktop before. RDM is complicated and brittle even run in containers. Having a clean system is essential to a positive RDM experience.

## Make sure you have a clean system

- removed Docker Desktop and all related files
- removed all Mac Ports pythons
- removed all pythons via uv
- removed uv
- remove ImageMagick and it's dependencies via Mac Ports, make sure your PATH and LD_LIBRARY_PATH are clean
- make sure any stale environment (e.g. .bashrc, .profile, etc) are removed
- rebooted system
- Confirm there is no Docker, non-system Python, ImageMagick
- Confirm your environment is clean (do you have references to removed things in your PATH or LD_LIBRARY_PATH?)

## Preparing your machine

Once I had a clean system here's the steps I took.

1. Install of [uv](https://docs.astral.sh/uv/getting-started/installation/)
2. Install python3.12 as default using uv, `uv python install 3.12 --default`
3. Install Docker Desktop
4. Install ImageMagick7 via Mac Ports, `sudo port install ImageMagick7`
5. Install cairo via Mac Ports, `sudo port install cairo`
6. Make sure that Mac Ports `libcairo.2.dylib` is symbolically linked to `/usr/local/lib`
7. Install openssl via Mac Ports, `sudo port install openssl`

## Installing RDM 13

You should now be prepared to follow the instructions at <https://inveniordm.docs.cern.ch/install/#quick-start>.

When you follow the Quick Install pick the `uv` example under **Install the CLI tool** heading.

- Make a directory to hold your install
- Run the setup sequence from Quick Start

What follows are the commands (with comments) that I ran to bring RDM 13 up on my machine after I cleaned it up and prepared

~~~
mkdir rdm_test                  # this is my test directory
cd rdm_test
uv tool install invenio-cli
invenio-cli check-requirements  # If this doesn't pass you probably have a dirty system still
invenio-cli init rdm            # Accept all the defaults for testing
cd my-site
invenio-cli check-requirements --development  # If this doesn't pass ...
# Install Python and Javascript packages, you'll see warns about depreciated packages and Node stuff (that's normal)
invenio-cli install
# Set up containerized database, cache, OpenSearch, etc. You'll see warnings about depreciated stuff
invenio-cli services setup
# Serve the application locally through a development server. This will result in a bunch of logged output
# and continue for a while. Be patient. There will be warning sprinkled in there too.
invenio-cli run
~~~

In another terminal windows point your browser at <https://127.0.0.1:5000/>, click through the warnings about the self signed cert.

~~~
open https://127.0.0.1:5000/
~~~

You should now have a running vanilla RDM 13 instance up. To bring it down do that following.

~~~
# To stop the application server:
# in terminal running invenio-cli run
^C [CTRL+C]
# ---
# To stop the service containers:
invenio-cli services stop
# ---
# To destroy the service containers
# (this will lose ALL data):
invenio-cli services destroy
~~~
