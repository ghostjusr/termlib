import curses as _curses

stdscr = _curses.initscr()
_curses.noecho()
_curses.cbreak()
stdscr.keypad(True)

