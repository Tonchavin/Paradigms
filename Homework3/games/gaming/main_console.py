from gaming import TTTBoard
from Homework3.games.gaming.play_console import TTTConsolePlay as TTTPlay


def main():
	board = TTTBoard(3)
	gameplay = TTTPlay(board)
	# Цикл обработки событий
	msg = None
	while True:
		msg = msg or gameplay.get_default_input_message()
		gameplay.draw_board()
		if gameplay.draw_state():
			break
		inp = input(msg)
		msg = gameplay.handle_input(inp)


if __name__ == "__main__":
	main()