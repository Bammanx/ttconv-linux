python3 -m venv ./buildinghere
source ./buildinghere/bin/activate
pip install -r requirements.txt
pyinstaller --onefile --name ttconv --collect-all ttconv launcher.py
