from flask import Flask, render_template, request, send_from_directory
import socket
import json
import threading
from config import HOST, FLASK_PORT, SOCKET_PORT

app = Flask(__name__)

# Головна сторінка
@app.route("/")
def index():
    return render_template("index.html")

# Сторінка з формою
@app.route("/message", methods=["GET", "POST"])
def message():
    if request.method == "POST":
        username = request.form["username"]
        message = request.form["message"]
        
        data = {"username": username, "message": message}
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(json.dumps(data).encode("utf-8"), (HOST, SOCKET_PORT))
        
        return render_template("message.html", success=True)
    
    return render_template("message.html", success=False)

# Обробка статичних ресурсів
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

# Обробка 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

if __name__ == "__main__":
    from socket_server import start_socket_server

    # Запускаємо сокет-сервер у окремому потоці
    threading.Thread(target=start_socket_server, daemon=True).start()

    # Запускаємо Flask
    app.run(host=HOST, port=FLASK_PORT, debug=True)
