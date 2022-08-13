@echo off
python E:\pytask\app\create_task.py
if NOT ["%errorlevel%"]==["0"] pause
