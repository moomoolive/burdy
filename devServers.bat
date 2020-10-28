@echo off
title Burdy development servers
echo This script initiates burdy development servers.
echo Do you want to run the script?
set /p Response= Please enter response[y/n]:
if %Response%==y goto:start
if %Response%==n goto:end

:start
    cls
    echo Type 'all' to run all servers, and code editor.
    echo Type 'serve' to run all servers, and not open code editor.
    echo Type 'one' to run only burdy.
    echo Type 'no' to exit script.

    cd dev_server_scripts

    set /p Response= please enter response:
    if %Response%==all goto:all
    if %Response%==one goto:one
    if %Response%==no goto:end

    :all
        start tensorflow_API.bat
        start scraper.bat

    :one
        start burdy.bat

:end