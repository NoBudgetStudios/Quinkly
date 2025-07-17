@echo off
echo 🛠️ Checking for virtual environment...

IF NOT EXIST venv (
    echo 🔧 Creating virtual environment...
    python -m venv venv
)

echo ✅ Activating virtual environment...
call venv\Scripts\activate

echo 📦 Installing requirements...
pip install -r requirements.txt

echo ✅ Setup complete.
pause
