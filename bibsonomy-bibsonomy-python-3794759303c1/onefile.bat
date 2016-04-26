
REM use this file to automate downloading of publications on Windows

@echo off

REM change paths and credentials here
set bindir=C:\Progra~1\BibSonomy-Python
set datadir=C:\BibSonomy
set username=b
set apikey=apikey

python %bindir%\onefile.py --user %username% --no-bookmarks --documents --directory %datadir% %username% %apikey%

