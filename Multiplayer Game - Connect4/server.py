import socket
import threading
import json
from utils import load_scoreboard, save_scoreboard, update_score

HOST = '127.0.0.1'
PORT = 65432

scoreboard = load_scoreboard()
clients = []
lock = threading.Lock()

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()

            # If message is player name (winner)
            print(f"[RECEIVED] {message} from {addr}")

            with lock:
                update_score(scoreboard, message)
                save_scoreboard(scoreboard)

            # Broadcast updated scoreboard to all clients
            broadcast_scoreboard()
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        print(f"[DISCONNECTED] {addr} disconnected.")
        conn.close()
        with lock:
            clients.remove(conn)

def broadcast_scoreboard():
    scoreboard_json = json.dumps(scoreboard).encode()
    with lock:
        for client in clients:
            try:
                client.sendall(scoreboard_json)
            except:
                pass

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        with lock:
            clients.append(conn)
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()
