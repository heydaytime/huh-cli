import os
import platform
from typing import List

def get_last_command(n:int =1) -> List[str]:
    platform_name = platform.system().lower();
    shell_env = os.environ.get('SHELL', '')

    if platform_name == 'darwin' or platform_name == 'linux':
        if 'zsh' in shell_env:
            return zsh_history(n)
        elif 'bash' in shell_env:
            # REMEMBER TO RUN enable_active_logging_bashrc() ONCE to enable active logging
            return bash_history(n)  # Assuming bash history is similar to zsh for this example
        else:
            raise NotImplementedError(f"Unsupported shell: {shell_env}")
    else:
        raise NotImplementedError(f"Unsupported platform: {platform_name}")



def zsh_history(n:int =1) -> List[str]:
    history_file = os.path.join(os.path.expanduser('~'), f'.zsh_history')
    cmds:List[str] = []
    try:
        with open(history_file, 'r', encoding='utf-8', errors='ignore') as shell_history_file:
            lines:List[str] = shell_history_file.readlines()
            # We assume that the first line indicates whether the history has timestamps
            HAS_TIMESTAMP: bool = lines[0].startswith(':')
            print(f"Has timestamp: {HAS_TIMESTAMP}")

            lines = list(reversed(lines))
            current_cmd: List[str] = []

            for i, line in enumerate(lines):
                line = line.rstrip('\\\n')
                current_cmd.insert(0, line)
                if(lines[i+1].endswith('\\\n')):
                    print(f"Continuing multi-line command: {line}")
                    continue

                command = " ".join(current_cmd)
                current_cmd = []
                cmds.append(remove_timestamp_zsh(command) if HAS_TIMESTAMP else command)

                if len(cmds) == n:
                    break

    except FileNotFoundError:
        print('Could not find zsh history file.')
    return list(reversed(cmds))


def bash_history(n:int =1) -> List[str]:
    history_file = os.path.join(os.path.expanduser('~'), '.bash_history')
    cmds:List[str] = []
    try:
        with open(history_file, 'r', encoding='utf-8', errors='ignore') as shell_history_file:
            lines:List[str] = shell_history_file.readlines()
            lines = list(reversed(lines))
            current_cmd: List[str] = []

            for i, line in enumerate(lines):
                line = line.rstrip('\\\n')
                current_cmd.insert(0, line)
                if(lines[i+1].endswith('\\\n')):
                    print(f"Continuing multi-line command: {line}")
                    continue

                cmds.append(" ".join(current_cmd))
                current_cmd = []

                if len(cmds) == n:
                    break

    except FileNotFoundError:
        print('Could not find bash history file.')
    return list(reversed(cmds))

def remove_timestamp_zsh(line: str) -> str:
  return line[line.find(';') + 1:] if ';' in line else line

# Bash does not actively log commands to the history file by default.
# must run this ONCE only for to read latest commands from bash history
def enable_active_logging_bashrc():
    print("Enabling active logging in .bashrc")

    bashrc_path = os.path.join(os.path.expanduser('~'), '.bashrc')
    try:
        with open(bashrc_path, 'a') as bashrc_file:
            bashrc_file.write("\n# Append to history file immediately after each command\n")
            bashrc_file.write("export PROMPT_COMMAND='history -a; history -n'\n")
            bashrc_file.write("shopt -s histappend\n")
    except (OSError, IOError) as e:
        print(f"Error updating {bashrc_path}: {e}")
