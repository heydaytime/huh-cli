import os
import argparse

def get_last_command(n=1):
    # Get the user's home directory
    home = os.path.expanduser('~')
    history_file = os.path.join(home, '.zsh_history')
    try:
        with open(history_file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            cmds = []
            # Find the last n non-empty lines, skipping invocations of lastcmd
            for line in reversed(lines):
                line = line.strip()
                if line:
                    # zsh history lines may start with a colon and metadata, e.g. ': 1681234567:0;ls -l'
                    if ';' in line:
                        cmd = line.split(';', 1)[1]
                    else:
                        cmd = line
                    # Skip if the command is a lastcmd invocation
                    if cmd.strip().startswith('lastcmd'):
                        continue
                    cmds.append(cmd)
                    if len(cmds) == n:
                        break
            if cmds:
                for cmd in reversed(cmds):
                    print(cmd)
            else:
                print('No command found in history.')
    except FileNotFoundError:
        print('Could not find zsh history file.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print the last n commands from your zsh history.')
    parser.add_argument('-n', type=int, default=None, help='Number of last commands to print')
    parser.add_argument('dashn', nargs='?', type=str, help='Alternative way to specify number of commands, e.g., -5')
    args = parser.parse_args()

    n = 1
    if args.n is not None:
        n = args.n
    elif args.dashn and args.dashn.startswith('-') and args.dashn[1:].isdigit():
        n = int(args.dashn[1:])
    get_last_command(n)