#!/usr/bin/env python3

import sys
import os
import subprocess

def print_alias():
    print("""
function huhcli() {
  source "$HUHCLI_PATH/venv/bin/activate"
  python -m huh "$@"
}
""")

if __name__ == "__main__":
    if '--alias' in sys.argv:
        print_alias()
    else:
        main_path = os.path.join(os.path.dirname(__file__), "main.py")
        subprocess.run([sys.executable, main_path] + sys.argv[1:])
