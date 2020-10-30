@echo off
title Burdy development servers
echo This script initiates burdy development servers.
echo Do you want to run the script?
set /p Response= Please enter response[y/n]:
if %Response%==y goto:start
if %Response%==n goto:end

:start
    cls
    echo Type 'all' to run all servers.
    echo Type 'back' to run all backend servers.
    echo Type 'one' to run only burdy.
    echo Type 'no' to exit script.

    cd util_scripts/dev_servers

    set /p Response= please enter response:
    if %Response%==all goto:all
    if %Response%==back goto:back
    if %Response%==one goto:one
    if %Response%==no goto:end

    :all
        start frontend.bat

    :back
        start tensorflow_API.bat
        start scraper.bat

    :one
        start burdy.bat

:end