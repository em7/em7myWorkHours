@echo off
rem the script to show console and run the myWorkHours_cli, then wait
rem should have the .py extension associated with pythonw.exe

echo myWorkHours version 1.0.1
echo distributed under the terms and conditions of WTFPL www.wtfpl.net
echo.
echo USAGE: past the work hour report copied from the WebTerm website
echo one per line. When done with the pasting, press ENTER key and then
echo CTRL+Z and ENTER again (= the end of standard input
echo in DOS/Windows environment).
echo The actual time is printed. 
echo.
echo If the LEAVE is not the last event, it will count the time in work till NOW.

myWorkHours_cli.py
@pause
