@echo off
copy /V /-Y "Win64\openal32.dll" %systemroot%\syswow64
cd\
cd %systemroot%\syswow64
regsvr32  openal32.dll /s
