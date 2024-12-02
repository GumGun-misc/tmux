#!/bin/python3.12

import os
import subprocess

def main():
    print("hook")
    window_id_2 = subprocess.run(["tmux", "display", "6666", "new-window", "-dP", "-t", session_id, "-F","#{window_id}", "python"], capture_output=True)


if __name__ == '__main__':
    main()
