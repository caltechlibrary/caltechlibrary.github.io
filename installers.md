
# Installers

Most of our Golang software can be installed easily on Linux, macOS and Windows from the command line. For macOS and Linux you open a "terminal" and use the curl command. For Windows you open a Powershell and use it's commands to perform a similar role. Here's an example of the commands for [datatools](https://github.com/caltechlibrary/datatools).

Installing datatools on Linux or macOS using first open the Terminal application so you can execute comand line programs. Then use curl to install datatools.

~~~shell
curl https://caltechlibrary.github.io/datatools/installer.sh | sh
~~~

On Windows you open Powershell either directly or via Window's Terminal application. Then use the Powershell commands `irm` and `iex` to retrieve
and execute the Powershell install script.

~~~pwsh
irm https://caltechlibrary.github.io/datatools/installer.ps1 | iex
~~~

If you have problems with the installer you should report the issue to the respective issure tracker for the repositories.

Repository                                                         Install for Linux and macOS using curl
----------------------------------------------------------------   -------------------------------------------------------------------
[datatools](https://github.com/caltechlibrary/datatools/issues)    `curl https://caltechlibrary.github.io/datatools/installer.sh | sh`
[dataset](https://github.com/caltechlibrary/dataset/issues)        `curl https://caltechlibrary.github.io/dataset/installer.sh | sh`
[irdmtools](https://github.com/caltechlibrary/irdmtools/issues)    `curl https://caltechlibrary.github.io/irdmtools/installer.sh | sh`
[cold](https://github.com/caltechlibrary/cold/issues)              `curl htpps://caltechlibrary.github.io/cold/installer.sh | sh`
[CMTools](https://github.com/caltechlibrary/CMTools/issues)         `curl htpps://caltechlibrary.github.io/CMTools/installer.sh | sh`

Repository                                                         Install for Windows using Powershell, irm and iex
----------------------------------------------------------------   -------------------------------------------------------------------
[datatools](https://github.com/caltechlibrary/datatools/issues)    `irm https://caltechlibrary.github.io/datatools/installer.ps1 | iex` 
[dataset](https://github.com/caltechlibrary/dataset/issues)        `irm https://caltechlibrary.github.io/dataset/installer.ps1 | iex`   
[irdmtools](https://github.com/caltechlibrary/irdmtools/issues)    `irm https://caltechlibrary.github.io/irdmtools/installer.ps1 | iex`  
[cold](https://github.com/caltechlibrary/cold/issues)              `irm https://caltechlibrary.github.io/cold/installer.ps1 | iex`
[CMTools](https://github.com/caltechlibrary/CMTools/issues)        `irm https://caltechlibrary.github.io/CMTools/installer.ps1 | iex`

