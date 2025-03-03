import json
import os
from datetime import datetime
from config import DATA_FILE

def save_message(username, message):
    """Зберігає повідомлення у JSON-файл."""
    if not os.path.exists("storage"):
        os.makedirs("storage")
    
    data = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

    timestamp = str(datetime.now())
    data[timestamp] = {"username": username, "message": message}

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
