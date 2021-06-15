@ECHO OFF
for /R "C:\Grypter\" %%G in (*.png) do copy "%%G" "%userprofile%\Desktop\Grypter"
