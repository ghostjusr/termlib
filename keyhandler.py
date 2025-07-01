"""
keyhandler - Terminal Key Input Handler for TermLib

This module provides the KeyHandler class, which simplifies keyboard input
handling in terminal-based applications using the curses library.

Features:
- Supports registration of callback functions for any key
- Detects both regular characters (e.g., "a", "1") and special keys (e.g., arrows, escape)
- Allows setting a per-frame loop function
- Provides a clean abstraction for integrating keypress detection into terminal games
"""

import curses

class KeyHandler:
    def __init__(self):
        self.callbacks = {}
        self._last_key = None
        self._stdscr = None
        self._on_loop = None
        self._running = False

    def register(self, key, callback):
        """Register a callback for a key (character or keycodes constant)."""
        self.callbacks[key] = callback

    def run_loop(self):
        """Start the keyhandler loop."""
        curses.wrapper(self._main)

    def _main(self, stdscr):
        self._stdscr = stdscr
        stdscr.nodelay(True)
        stdscr.keypad(True)
        self._running = True

        while self._running:
            self._handle_input()
            if self._on_loop:
                self._on_loop()
            stdscr.refresh()

    def _handle_input(self):
        try:
            key = self._stdscr.getch()
            if key == -1:
                return

            self._last_key = key

            if key in self.callbacks:
                self.callbacks[key]()
            elif 0 <= key <= 255:
                char = chr(key)
                if char in self.callbacks:
                    self.callbacks[char]()
        except:
            pass

    def stop(self):
        """Stop the main loop."""
        self._running = False
