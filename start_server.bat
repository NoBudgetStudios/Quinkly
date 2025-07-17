@echo off
echo Starting FastAPI server...
uvicorn App.main:app --reload --port 8666 --log-level debug
pause
