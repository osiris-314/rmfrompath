#!/usr/bin/env python3
import subprocess
import os
from colorama import Fore
from pathlib import Path
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Remove a file from the PATH.")
parser.add_argument('-c', '-command', type=str, required=True, help='The file name to be removed from /usr/local/bin')

args = parser.parse_args()
file_name = args.c

# Resolve path
file_path = Path(f'/usr/local/bin/{file_name}')

if file_path.is_file():
    try:
        subprocess.run(f'sudo rm {file_path}', shell=True, check=True)
        print(Fore.LIGHTGREEN_EX + 'Successfully Removed ' + Fore.LIGHTBLUE_EX + str(file_name) + Fore.LIGHTGREEN_EX + ' From The ' + Fore.LIGHTYELLOW_EX + 'PATH' + Fore.WHITE)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + 'Error: ' + Fore.LIGHTRED_EX + str(e) + Fore.WHITE)
else:
    print(Fore.RED + 'File ' + Fore.LIGHTBLUE_EX + str(file_name) + Fore.RED + ' Does Not Exist in /usr/local/bin' + Fore.WHITE)
