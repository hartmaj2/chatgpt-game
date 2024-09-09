# My first prompt:
Give me code for a computer game where I will control a player with a sword and have to fight incoming enemies. I want the player to be able to level up and buy items

ChatGPT suggested Python Pygame module right away. (Maybe my history)


# Side quest 1 - Virtual Environments

## What are they for
- Don't rely on global system packages and can install my own and use them, I can safely test new packages and how my program will run with them
- Sharing code - I can `pip freeze` to send somebody information about packages they need to have in their own environment to run their program
- Can use different versions of my interpreter in my environment

## Usage
- Created by running `pip -m venv <environment_name>` (the -m stands for module option, runs a module as a script)
- Shows you list of all installed packages including the one already there by default `pip list` 
- `pip freeze` doesn't show the default packages but only the newly installed ones
- When I want to recreate I use `python3 -m pip install` with `-r, --requirement <file>    Install from the given requirements file. This option can be used multiple times. ` option

# Side quest 2 - brew

## What is brew for
- Brew manages software installed on my machine 
- `brew update` downloads the metadata for what software should be updated etc. it doesn't download any package data, just metadata
- `brew upgrade` uses the metadata to download the actual packages or remove old ones