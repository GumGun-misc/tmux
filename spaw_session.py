#!/bin/python3.12

import subprocess

def main():
    session_id = create_subwindows("test")
    set_keys(session_id)


def create_subwindows(session_name):
    session_id = subprocess.run(["tmux", "-L", "6666", "new-session", "-dP", "-s", session_name, "-F","#{session_id}", "-E", "python"], capture_output=True)
    print(session_id)
    if session_id.returncode == 1:
        return None
    session_id = session_id.stdout.decode()[:-1]
    window_id_2 = subprocess.run(["tmux", "-L", "6666", "new-window", "-dP", "-t", session_id, "-F","#{window_id}", "python"], capture_output=True)
    print(window_id_2)
    window_id_3 = subprocess.run(["tmux", "-L", "6666", "new-window", "-dP", "-t", session_id, "-F","#{window_id}", "python"], capture_output=True)
    print(window_id_3)
    window_id_4 = subprocess.run(["tmux", "-L", "6666", "new-window", "-dP", "-t", session_id, "-F","#{window_id}", "python"], capture_output=True)
    print(window_id_4)
    return session_id

def set_keys(session_id):
    keys = subprocess.run(["tmux", "-L", "6666", "set-option", "key-table", "popup"], capture_output=True)
    keys = subprocess.run(["tmux", "-L", "6666", "set-option", "prefix", "None"], capture_output=True)
    print(keys)


if __name__ == "__main__":
    main()

