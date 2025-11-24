from game import TicTacToe
from stats import save_game_result
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_int_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Пожайлуста введите число в диапазоне от {min_val} до {max_val}")
        except ValueError:
            print("Ошибка. Введите число.")

def print_board(board):
    size = len(board)
    for i in range(size):
        print(" | ".join(board[i]))
        if i < size - 1:
            print("-" * (size * 4 - 3))

def main():
    while True:
        clear_screen()
        print("Игра Крестики-Нолики")
        
        board_size = get_int_input("Введите размер игрового поля (3-10): ", 3, 10)
        
        print("\nВыберите режим игры:")
        print("1. Игрок против Игрока")
        print("2. Игрок против Компьютера")
        mode = get_int_input("Введите число (1-2): ", 1, 2)
        
        game = TicTacToe(board_size)
        game.random_first_player()
        game.game_mode = "PvP" if mode == 1 else "PvE"
        
        while True:
            clear_screen()
            print(f"Ход игрока: {game.current_player}")
            print_board(game.board)
            
            if game.game_mode == "PvE" and game.current_player == 'O':
                row, col = game.bot_move()
                print(f"\nХод компьютера: ({row}, {col})")
            else:
                row = get_int_input(f"\nИгрок {game.current_player} выберите ряд (0-{board_size-1}): ", 0, board_size-1)
                col = get_int_input(f"Игрок {game.current_player} выберите колонку (0-{board_size-1}): ", 0, board_size-1)
            
            if game.make_move(row, col):
                if game.check_winner():
                    clear_screen()
                    print_board(game.board)
                    print(f"\nИгрок {game.current_player} победил!")
                    save_game_result(board_size, game.current_player, game.move_history, game.game_mode)
                    break
                elif game.is_draw():
                    clear_screen()
                    print_board(game.board)
                    print("\nНичья")
                    save_game_result(board_size, "Draw", game.move_history, game.game_mode)
                    break
                game.switch_player()
            else:
                print("Недопустимый ход. Попробуйте снова.")
        
        play_again = input("\nИграть снова? (д/н): ").lower()
        if play_again != 'д':
            break

if __name__ == "__main__":
    main()