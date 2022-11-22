@echo off
TITLE Backup Job
SET diretorio=%~dp0

python "%currentdir%job_backup.py" %*
pause
