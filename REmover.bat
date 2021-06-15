@ECHO OFF
for /R "%userprofile%\Desktop\Grypter\" %%G in (*.png) do copy "%%G" "C:\Grypter\"
