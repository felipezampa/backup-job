@echo off
echo ========================== Pentaho  ==========================
set pasta="C:\SAFEGOLD\Job"
set ano=%date:~10,4%
set mes=%date:~7,2%
set dia=%date:~4,2%
set data=%date:~6,4%%date:~3,2%%date:~0,2%
set zip="C:\SAFEGOLD\Backups\BackupJob\JobAgross-%dia%.%mes%.%ano%.zip"
SET logfile="%currentdir%log.txt"

echo. >> %logfile%
echo. >> %logfile%

powershell Compress-Archive -Path %pasta%\* -DestinationPath %zip% >> %logfile%
 
echo ========================== Postgres ==========================

set pg_dump_path="C:\Program Files\PostgreSQL\14\bin\"pg_dump.exe
set dump_file="C:\SAFEGOLD\Backups\BackupDump\dump-agross-%dia%-%mes%-%ano%.sql"
set PGPASSWORD=postgres

%pg_dump_path% -h localhost -p 5432 -U postgres -F c -b -v -f %dump_file% staging_agross >> %logfile%