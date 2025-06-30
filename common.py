import os as _os
import json as _json
import ctypes as _ctypes

class Terminal:
	def __init__(self):
		pass

	def set_windows_terminal_size(cols, rows):
		_os.system(
			f'powershell -Command "$size = New-Object System.Management.Automation.Host.Size {cols},{rows}; '
			f'$Host.UI.RawUI.BufferSize = $size; '
			f'$Host.UI.RawUI.WindowSize = $size"'
		)


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
