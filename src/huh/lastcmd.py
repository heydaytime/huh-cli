def get_last_command(n=1):
    import os
    home = os.path.expanduser('~')
    history_file = os.path.join(home, '.zsh_history')
    try:
        with open(history_file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            print(f"Found {len(lines)} lines in history.")
            cmds = []
            for line in reversed(lines):
                line = line.strip()
                if line:
                    if ';' in line:
                        cmd = line.split(';', 1)[1]
                    else:
                        cmd = line
                    # Temporarily disable this to test
                    # if cmd.strip().startswith('lastcmd'):
                    #     continue
                    cmds.append(cmd)
                    if len(cmds) == n:
                        break
            print(f"Collected {len(cmds)} commands.")
            if cmds:
                for cmd in reversed(cmds):
                    print(cmd)
            else:
                print('No command found in history.')
    except FileNotFoundError:
        print('Could not find zsh history file.')
