---
title: Google Chrome and DNS problems
author: rsdoiel@caltech.edu (R. S. Doiel)
abstract: |
  Quick notes on a "DNS" problem specific to Google Chrome
  and it got solved.
keywords:
  - DNS
  - Chrome
dateCreated: 2025-04-01
datePublished: 2025-04-01
dateModified: 2025-08-04
---

# Google Chrome and DNS problems

Chrome can be problematic. It is not as reliable as it used to be.  Recently we've run into issues where you can't reach Caltech Library web resources even through they are up and available via other browsers like Safari. There are a couple things you can try before resorting to a clean reinstall of Google Chrome.

1. Clear you browser caches, this is accomplished from the "settings" page. Google seems to change its contents an layout regularly. You'll have to open the "settings" and visual inspect the elements to see how to empty your caches.
2. Chrome's less obvious chrome://net-internals settings page. This page contains additional caches you can try to clear
3. If that doesn't work remove Chrome completely then try a fresh install (the solution that ultimately worked)

## Removing Google Chrome on macOS completely

Basic idea.

1. Quit Chrome if running, you can check the "Force Quit" list to make sure it's not running
2. Locate the Chrome related directories and remove them.

Below is a description of using your mouse and finder to do the work. The first part is easy the latter part more challenging as macOS really doens't like making this easy (shame on them).

### Finder approach

Start up the Terminal App. Changing into the "Library" directory (aka folder) open the folder in finder using the open command, open .. This will let you see what is inside the Library folder (often hidden in the regular finder view of folders).

~~~shell
cd Library
open .
~~~

Remove the main application. You can use finder to find "Google Chrome" and drag it to the trash.

- "/Applications/Google Chrome.app"

You need to find and remove the following "Google" folders. Normally the "Library" folder isn't listed in your finder window. What I do is start up "Terminal" then change directory into the library folder and use the "open ." command.
cd Library
open .

Now we should be able to find these three folders and drag them to the trash.

- "$HOME/Library/Google"
- "$HOME/Library/Application Support/Google"
- "$HOME/Library/Caches/Google/"

The next back of folders are trickier. They may more may not exist. The first two can be found using the finder and dragged to the trash. The lasts two you have to search for. The "*" is a wild card. I find it easier to locate them
using the terminal and the old fashioned Unix "find" command.

- "$HOME/Library/Caches/chrome_crashpad_handler"
- "$HOME/Library/HTTPStorages/chrome_crashpad_handler"
- "$HOME/Library/Application Support/Code/CachedData/*/chrome"
- "$HOME/Library/HTTPStorages/com.google.*"

Once these folders are all in the trash you can empty the trash (make take a little while). 

### Using the shell commands

While this is more typing (which you can minimize by cutting and pasting) I found it less frustrating. These commands are all executed from your Terminal window. You can cut and paste the lines one by one or you can save them in a plain text file, e.g. "remove_chrome.bash" and run them with the command "sh remove_chrome.bash".

If you run the script is can a while (30 to 120 seconds).

~~~shell
#!/bin/bash

sudo rm -r /Applications/Google\\ Chrome.app/
sudo rm -fR "$HOME/Library/Google"
sudo rm -fR "$HOME/Library/Application Support/Google"
sudo rm -fR "$HOME/Library/Caches/Google/"

sudo rm -fR "$HOME/Library/Caches/chrome_crashpad_handler"
sudo rm -fR "$HOME/Library/HTTPStorages/chrome_crashpad_handler"
sudo rm -fR "$HOME/Library/Application Support/Code/CachedData/*/chrome"
sudo rm -fR "$HOME/Library/HTTPStorages/com.google.*"
~~~

You can check to make sure everything is gone with the script.

~~~shell
sudo ls /Applications/Google\\ Chrome.app/
sudo ls "$HOME/Library/Google"
sudo ls "$HOME/Library/Application Support/Google"
sudo ls "$HOME/Library/Caches/Google/"

sudo ls "$HOME/Library/Caches/chrome_crashpad_handler"
sudo ls "$HOME/Library/HTTPStorages/chrome_crashpad_handler" 
sudo ls "$HOME/Library/Application Support/Code/CachedData/*/chrome"
sudo ls "$HOME/Library/HTTPStorages/com.google.*"
~~~
