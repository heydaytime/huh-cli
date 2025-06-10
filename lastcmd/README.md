# lastcmd

A simple Python command-line tool to print the last command(s) you ran in your zsh shell.

## Features
- Prints the last command from your zsh history by default
- Supports printing the last N commands (e.g., `lastcmd -n 5` or `lastcmd -5`)
- Skips its own invocations in the output

## Installation

1. **Clone or download this repository** to your computer.
2. Open a terminal and navigate to the directory containing `setup.py` and `lastcmd.py`.
3. Install the package locally (for your user):
   ```sh
   pip install --user .
   ```

4. **Ensure the Python user scripts directory is in your PATH.**
   Add this line to your `~/.zshrc` (if not already present):
   ```sh
   export PATH="$HOME/Library/Python/3.11/bin:$PATH"
   ```
   This should be the folder the lastcmd.py file is. Replace `3.11` with your Python version if different.

5. **Allow the zsh_history file to update after every command.**
   Add these lines to `~/.zshrc` as well:
   ```sh
   setopt INC_APPEND_HISTORY       # Write every command to the history file immediately
   setopt SHARE_HISTORY            # Share command history across terminals
   setopt HIST_IGNORE_SPACE        # (Optional) Ignore commands starting with space
   setopt HIST_SAVE_NO_DUPS        # Don't write duplicates to file
   ```

6. Reload your shell configuration:
   ```sh
   source ~/.zshrc
   ```

## Usage

- Print the last command:
  ```sh
  lastcmd
  ```
- Print the last 5 commands:
  ```sh
  lastcmd -n 5
  # or
  lastcmd -5
  ```

## Notes
- This tool reads from your `~/.zsh_history` file. It is designed for zsh users.
- If you previously set an alias for `lastcmd`, remove it from your `~/.zshrc` to use the installed command globally.
- If you use a different shell (like bash), you will need to modify the script to read from the appropriate history file.

## Uninstallation
To uninstall, run:
```sh
pip uninstall lastcmd
```