@echo off
Rem Runs the Akizuki.py file. MUST HAVE A COMPLETED config.txt FILE TO WORK.
Rem Lines below this will: Change working directory to Akizuki in order to run the .py file, and echo a timer when bot is turned off.

cd %cd%\main
python Akizuki.py
echo The bot has shut down.
timeout /t 10s
exit
