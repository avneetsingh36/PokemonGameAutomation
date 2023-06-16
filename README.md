# Pokémon Automation Script

This Python script is designed to automate repetitive tasks for leveling up Pokémon characters in a daycare setup. The script leverages libraries like `pyautogui` and `keyboard` for GUI automation, and `time` for controlling the delay between actions. This reduces the manual intervention required and allows for efficient and streamlined leveling of your Pokémon.

## Key Features

**Screen Size Determination**: The script captures the size of the current screen to adapt to various display sizes and resolutions. This feature is not necessary, but it's there in case you want to test that it is sending keystrokes to the right desktop/monitor.

**Automated Clicks and Key Presses**: The script automatically clicks on specific portions of the screen and simulates key presses. It runs in a loop to simulate repeated 'up' and 'down' keystrokes, mimicking the character's movement in the game.

## Usage

1. Clone the repository to your local machine and navigate to the repository's directory.

2. Run the script using Python3: `python3 script.py`

## Requirements
- Python3
- pyautogui
- keyboard

## Installation
1. Install Python3.
2. Install the required Python libraries with pip: `pip3 install pyautogui keyboard`

## Caution

This script takes control of your computer to some extent while it is running. Make sure you have saved all your work and closed any unnecessary applications before running the script. If you want to stop the script, kill the terminal window or press `control + c`.

### Contributor
- [Avneet Singh](https://github.com/avneetsingh36)
