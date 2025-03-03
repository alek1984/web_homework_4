import socket
import json
from storage import save_message
from config import SOCKET_PORT

def start_socket_server():
    """Запускає UDP-сервер для прийому повідомлень."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", SOCKET_PORT))

    print(f"Socket сервер запущено на порту {SOCKET_PORT}")

    while True:
        data, addr = sock.recvfrom(1024)
        try:
            message = json.loads(data.decode("utf-8"))
            save_message(message["username"], message["message"])
            print(f"Отримано повідомлення: {message}")
        except json.JSONDecodeError:
            print("Помилка обробки JSON")
