import socket
import threading
import pygame
import json
from game import Connect4Game
from utils import load_scoreboard

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect4 Multiplayer")
font = pygame.font.SysFont("monospace", 30)

# Assets
coin_red = pygame.image.load('Assets/images/coin_red.png')
coin_yellow = pygame.image.load('Assets/images/coin_yellow.png')
drop_sound = pygame.mixer.Sound('Assets/sounds/drop.wav')

# Socket setup
HOST = '127.0.0.1'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((HOST, PORT))
    print("[CONNECTED] Connected to the server.")
except ConnectionRefusedError:
    print("[ERROR] Cannot connect to the server.")
    exit()

scoreboard = {}
lock = threading.Lock()

def receive_scoreboard():
    global scoreboard
    while True:
        try:
            data = client_socket.recv(4096)
            if not data:
                break
            new_scoreboard = json.loads(data.decode())
            with lock:
                scoreboard = new_scoreboard
        except Exception as e:
            print(f"[ERROR] {e}")
            break

# Start receiving scoreboard updates
threading.Thread(target=receive_scoreboard, daemon=True).start()

game = Connect4Game()

def draw_scoreboard():
    y_offset = 10
    with lock:
        if scoreboard:
            label = font.render("Scoreboard:", True, (255, 255, 255))
            screen.blit(label, (10, y_offset))
            y_offset += 40
            for player, score in scoreboard.items():
                text = font.render(f"{player}: {score}", True, (255, 255, 255))
                screen.blit(text, (10, y_offset))
                y_offset += 30

def main():
    running = True
    game.draw_board(screen)
    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                col = posx // 100

                if game.is_valid_location(col):
                    game.drop_piece(col)
                    drop_sound.play()

                    winner = 1 if game.turn == 2 else 2  # Because turn flips after drop
                    if game.check_winner(winner):
                        print(f"Player {winner} wins!")
                        # Send player name as winner to server
                        player_name = f"Player{winner}"
                        try:
                            client_socket.sendall(player_name.encode())
                        except Exception as e:
                            print(f"[ERROR] {e}")

                screen.fill((0, 0, 0))
                game.draw_board(screen)
                draw_scoreboard()
                pygame.display.update()

    pygame.quit()
    client_socket.close()

if __name__ == "__main__":
    main()
