# huh – AI CLI Syntax Autocorrector (Pre-Pre-Pre Alpha 🚧)

**Ever mistyped a CLI command and got hit with a vague error?**  
*huh* is an experimental (and very early stage) CLI tool that suggests what you might have meant to type.

---
# Updates JUN 16 2025

I finally figured out how to get tab completion working with typer. 
It used to work with the typer command but not the huhcli command. 
It's pretty straightforward actually. I just needed to forward all commands form __main__.py to main.py

Add this to your .zshrc file to enable the tool:

```shell
fpath+=~/.zfunc; autoload -Uz compinit; compinit
export HUHCLI_PATH="$HOME/ProgrammingProjects/huh-cli"
eval "$(python $HUHCLI_PATH/src/huh/__main__.py --alias)"

```


# Updates JUN 14 2025

I found out that the 'lastcmd' tool is already a part of macos/linux. 

You can get the by simply running

```bash
fn -ln -1
```
That simplifies the whole thing a lot. We can now just focus on implementing AI and our fast cache solution. 

To get this new functionality running do the following:

- Append $eval("python /path/to/your/__main__.py --alias") to your ~/.zshrc file
- Run the following command to make the script executable:
```bash
chmod +x /path/to/your/__main__.py
```
- Also source your .zshrc file to make the changes take effect:
```bash
source ~/.zshrc
```

NOW you can run the tool using the command:

```bash
huhcli
```
And then it stores the last command in storage.txt file in your huh-cli project root directory. 

# Updates JUN 13 2025
## RUNNING THE TOOL

I have no idea why, but you have to do this anytime you make a change to the files.
I think it is precompiling stuff and you need to reinstall everything to make the changes known.

```bash
rm -rf build/
pip install .
typer ./src/huh/cli.py run lastcmd --n 3 
```

I also added multiline command support, for eg.
```bash
ls \
-l
```

is actually one command, not two. It is the same as
```bash
ls -l
```
so the lastcmd should treat it as one command.

I also did some basic refactoring. 

Added support for .bash_history too. 
Idk if this was already there, but I hard coded lastcmd to only work on mac and linux.
Windows is 🙅‍♂️

---

## 🔧 Setup Instructions

Follow these steps to set up your development environment.

### 1. Install Ollama (for macOS)

Via Homebrew:

```bash
brew install ollama
```

Or download it directly from [ollama.com](https://ollama.com/download).

> 💡 This tool also supports Linux. Use your preferred package manager to install Ollama.

---

### 2. Set Up Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```
> We assume that you already have python installed and configured on your system
---

### 3. Install Dependencies

Install [Typer](https://github.com/fastapi/typer):

```bash
pip install typer
```

Enable tab completion:

```bash
typer --install-completion
```

---

### 4. Run the CLI Tool (Bare Minimum)

```bash
pip install . 
```

run using Typer (with tab-completetion in args support):

```bash
typer ./src/huh/cli.py run lastcmd --n 3 
```

---

# Old_README.md just for reference from lastcmd

## lastcmd

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

# TODOS

- [] set email in pyproject.toml
- [] spell check name in pyproject.toml and license
- [] make this readme more readable
- [] todo this todo list
