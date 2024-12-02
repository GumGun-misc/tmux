#!/bin/python3.12

import os
import shutil

def main():
    tmux_path = shutil.which('tmux')
    os.execv(tmux_path, ["tmux", "-L", "6666", "attach", "-t", "test"]);



if __name__ == "__main__":
    main()
