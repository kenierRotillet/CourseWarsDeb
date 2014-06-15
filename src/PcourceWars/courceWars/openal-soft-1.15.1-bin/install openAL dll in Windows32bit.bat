@echo off
copy /V /-Y "Win32\openal32.dll" %systemroot%\system32
cd\
cd %systemroot%\system32
regsvr32 openal32.dll /s
