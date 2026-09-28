# VITyarthi canteen project

## Overview
This is my Python project for the VITyarthi evaluation. During short college breaks, students waste a lot of time waiting in line at the canteen just to order food. I built this simple command-line system so students can view the menu, place orders, and get their bills automatically. It also helps the canteen staff track what is ready and see how much money they made today.

**Author:** Athul K Jacob (26BAI10249)  
**Course:** CSE (AI/ML)  

## Features
- **Digital Menu:** Shows all the food items and their prices in a clean text table.
- **Cart & Ordering:** You can select multiple items by typing their ID numbers and quantities.
- **Automatic Billing:** Calculates the total cost and adds a 5% GST tax automatically to print a receipt.
- **Order Tracking:** Staff can update the status to "Preparing" or "Ready", and students can check it.
- **Sales Report:** A hidden admin option to see total orders, total money earned, and the highest sold item of the day.

## Tech Used
- Python 3 (No external libraries required)
- `unittest` module for testing
- Git and GitHub for version control

## How to install and run
1. Download or clone this repository to your computer.
2. Make sure you have Python installed.
3. Open the folder in VS Code or your terminal.
4. Type this command to start the program:
   `python main.py`

## Instructions for testing
I have written some basic tests in a separate file to make sure the math and dictionary lookups work correctly. 
To run the tests, open your terminal and type:
`python -m unittest test_canteen.py`
If everything is fine, it will run without errors and say "OK" at the bottom.

## Screenshots
Here is how the project looks when you run it in the terminal:

**1. Main Menu and Admin Options:**
![Main Menu](Screenshot%202026-09-27%20170824.png)

**2. Viewing the food catalog:**
![Food Menu](Screenshot%202026-09-27%20170735.png)

**3. Placing an order and getting the final bill:**
![Bill](Screenshot%202026-09-27%20170913.png)