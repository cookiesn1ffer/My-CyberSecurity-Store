# Python Key Logger (pynput-based)

## Overview

This project is a simple keystroke logging utility built using Python and the `pynput` library. It captures keyboard input events and stores them in a local log file.

This project is intended strictly for educational purposes and personal system monitoring.

## Features

* Logs alphanumeric and special keys
* Writes output to a local file (`log.txt`)
* Runs continuously until manually stopped
* Minimal and easy-to-understand implementation

## Tech Stack

* Python 3
* pynput

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/cookiesn1ffer/Scripts.git
cd Scripts/Python/Key-Logger
pip install pyinstaller
pip install pynput
pyinstaller --onefile --windowed file.py
```

This will create an executable

* Keystrokes will be recorded in `log.txt`
* Stop execution using `Taskmanager > file.exe > end task`

## Output Example

```
alphanumeric key a pressed
alphanumeric key b pressed
special key Key.space pressed
special key Key.enter pressed
```

## Disclaimer

This tool is developed for:

* Learning keyboard event handling

## How It Works

* Uses `pynput.keyboard.Listener` to capture keypress events
* Differentiates between:

  * `key.char` for alphanumeric input
  * `key` for special keys
* Appends captured events to `log.txt`

## Author

CookieSn1ffer

## License

MIT License
