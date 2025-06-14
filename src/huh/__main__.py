#!/usr/bin/env python3

# from huh.cli import app
#
# if __name__ == "__main__":
#     app()

import sys
def print_alias():
    print("""
          huhcli () {
                LAST_CMD=$(fc -ln -1)
                ~/ProgrammingProjects/huh-cli/src/huh/__main__.py "$LAST_CMD"
          }
          """)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please provide a command to store or use the --alias option to print the alias.")
    elif '--alias' in sys.argv:
        print_alias()
    else:
        with open('storage.txt', 'a') as f:
            f.write(' '.join(sys.argv[1:]) + '\n')
