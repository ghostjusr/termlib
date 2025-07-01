import os as _os
import json as _json

COLOR_CODES = {
    "BLACK": "0", "BLUE": "1", "GREEN": "2", "AQUA": "3",
    "RED": "4", "PURPLE": "5", "YELLOW": "6", "WHITE": "7",
    "GRAY": "8", "LIGHT_BLUE": "9", "LIGHT_GREEN": "A",
    "LIGHT_AQUA": "B", "LIGHT_RED": "C", "LIGHT_PURPLE": "D",
    "LIGHT_YELLOW": "E", "BRIGHT_WHITE": "F"
}

ANSI_COLORS = {
    "BLACK": 30, "RED": 31, "GREEN": 32, "YELLOW": 33,
    "BLUE": 34, "PURPLE": 35, "AQUA": 36, "WHITE": 37,
    "BRIGHT_BLACK": 90, "BRIGHT_RED": 91, "BRIGHT_GREEN": 92,
    "BRIGHT_YELLOW": 93, "BRIGHT_BLUE": 94, "BRIGHT_PURPLE": 95,
    "BRIGHT_AQUA": 96, "BRIGHT_WHITE": 97
}

class Terminal:
	def __init__(self, cols=120, rows=30, title="Command Prompt"):
		self.columns = cols
		self.rows = rows
		self.set_size(self.columns, self.rows)
		self.set_title(title)

	def set_size(self, cols, rows):
		self.columns = cols
		self.rows = rows
		_os.system(
			f'powershell -Command "$size = New-Object System.Management.Automation.Host.Size {cols},{rows}; '
			f'$Host.UI.RawUI.BufferSize = $size; '
			f'$Host.UI.RawUI.WindowSize = $size"'
		)

	def set_title(self, title):
		_os.system(f"title {title}")

	def set_theme(fg: str = "WHITE", bg: str = "BLACK"):
		system = _os.name
		fg = fg.upper()
		bg = bg.upper()

		if system == "nt":
			fg_code = COLOR_CODES.get(fg, "7")
			bg_code = COLOR_CODES.get(bg, "0")
			_os.system(f"color {bg_code}{fg_code}")
		else:
			fg_ansi = ANSI_COLORS.get(fg, 37)
			bg_ansi = ANSI_COLORS.get(bg, 40) - 30 + 40
			print(f"\033[{fg_ansi};{bg_ansi}m", end="")

		

_save_path = "save._json"

def set_path(path: str):
	global _save_path
	_save_path = path

def save(data, path=_save_path):
	with open(path, "w", encoding="utf-8-sig") as f:
		_json.dump(data, f)

def load(on_missing=None, path=_save_path):
	if not _os.path.exists(path):
		if on_missing:
			on_missing()
			return
		raise FileNotFoundError(f"Save file '{path}' does not exist.")
	with open(path, "r", encoding="utf-8-sig") as f:
		return _json.load(f)

colors = {
	"RED": "\033[1;31m",
	"BLUE": "\033[1;34m",
	"CYAN": "\033[1;36m",
	"GREEN": "\033[0;32m",
	"YELLOW": "\033[0;33m",
	"WHITE": "\033[1;37m",
	"BLACK": "\033[1;30m",
	"RESET": "\033[0;0m",
	"BOLD": "\033[;1m",
	"REVERSE": "\033[;7m",
	"NORMAL": "\033[0;35m"
}

def cls():
	_os.system("cls" if _os.name == "nt" else "clear")
