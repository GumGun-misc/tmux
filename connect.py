#!/bin/python3.12

import os

def main():
    os.execv("/usr/bin/tmux", ["tmux", "-L", "6666", "attach", "-t", "test"]);



if __name__ == "__main__":
    main()
