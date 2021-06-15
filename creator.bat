@echo off
@break off
@cls

setlocal EnableDelayedExpansion

if not exist "%userprofile%\Desktop\Grypter" (
  mkdir "%userprofile%\Desktop\Grypter"
  if "!errorlevel!" EQU "0" (
    echo Folder created successfully
  ) else (
    echo Error while creating folder
  )
) else (
  echo Folder already exists
)

exit