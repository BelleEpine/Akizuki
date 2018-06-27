@echo off
Rem Runs the Akizuki.py file. MUST HAVE A COMPLETED config.txt FILE TO WORK.
Rem Lines below this will: Change working directory to Akizuki in order to run the .py file, and echo a timer when bot is turned off.

cd %cd%\main

%SYSTEMROOT%\py.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO attemptPATH
%SYSTEMROOT%\py.exe -3 akizuki.py
PAUSE
GOTO terminate

:attemptPATH
py.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO attemptLAST
py.exe -3 akizuki.py
PAUSE
GOTO terminate

:attemptLAST
python.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO throwerror
python.exe akizuki.py
PAUSE
GOTO terminate

:throwerror
echo There was an unexpected error. Most likely, Python is not included as a PATH variable.

:terminate
exit

Rem Certain info pulled from https://ss64.com/nt/syntax-variables.html
