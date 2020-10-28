@echo off
title Turning on dev servers
echo this script will turn on dev servers, press any key to initiate
echo type 'all' to run all servers
echo type 'one' to run only burdy
echo type no to exit script
pause
cd dev_server_scripts

set /p Response= please enter response:
if %Response%==all goto:all
if %Response%==one goto:one
if %Response%==no goto:end

:all
    start burdy.bat
    start tensorflow_API.bat
    start scraper.bat
    goto:end

:one
    start burdy.bat

:end