@echo off
Rem Runs the setup.py file which will prompt the user for inputs to change the values of config.txt which are passed to the akizuki.py file for the bot to run.
Rem Lines below this will: Move the working directory one directory up, move to Akizuki, and run setup.py

cd..
cd %CD%\Akizuki
python setup.py
echo The program is done.
timeout /t 10
