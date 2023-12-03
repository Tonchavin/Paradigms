from curses import wrapper

from gaming import TTTBoard
from Homework3.games.gaming.play_curses import TTTCursesPlay as TTTPlay


def main(scr):
	board = TTTBoard(3)
	gameplay = TTTPlay(scr, board)
	msg = None
	# Цикл обработки событий
	while True:
		msg = msg or gameplay.get_default_input_message()
		gameplay.draw_board()
		if gameplay.draw_state():
			break
		inp = scr.getkey()
		msg = gameplay.handle_input(inp)
	inp = scr.getkey()


if __name__ == "__main__":
	wrapper(main)