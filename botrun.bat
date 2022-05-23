@echo off

call %~dp0Bot\venv\Scripts\activate

cd %~dp0Bot

set TOKEN=5137200405:AAFJuhmg-gtHIn7PUiQIQhxT3_pZPb4QOLU

python telegram.py

pause 