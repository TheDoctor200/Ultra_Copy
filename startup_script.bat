@echo off
setlocal enabledelayedexpansion

rem Get the directory of the batch script
set "batch_dir=%~dp0"

rem Set the path to the executable
set "exe_path=%batch_dir%Scan_and_Copy.exe"

rem Check if the executable exists
if exist "%exe_path%" (
    rem Execute the executable
    start "" "%exe_path%"
) else (
    echo Executable not found.
)

endlocal
