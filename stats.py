import os
from datetime import datetime

STATS_DIR = "game_stats"

def ensure_stats_dir():
    if not os.path.exists(STATS_DIR):
        os.makedirs(STATS_DIR)

def save_game_result(board_size, winner, moves, mode):
    ensure_stats_dir()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{STATS_DIR}/game_{timestamp}.txt"
    
    with open(filename, 'w') as f:
        f.write(f"Размер игрового поля: {board_size}\n")
        f.write(f"Режим игры: {mode}\n")
        f.write(f"Победитель: {winner}\n")
        f.write(f"Количество ходов: {len(moves)}\n")
        f.write("История ходов:\n")
        for move in moves:
            f.write(f"  {move[2]} -> ({move[0]}, {move[1]})\n")