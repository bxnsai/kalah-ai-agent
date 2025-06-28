# Kalah Ai Agent 

## <a href=https://github.com/aimacode/aima-python/>aima-python</a>
The two files used from this repository are **games.py** and **utils.py**. Modified alpha_beta_player method to use alpha_beta_cutoff_search in games.py. An eval_fn method was also developed to score most optimal moves considering the rules of the game. 

## kalah.py 
Utilizes the Game class as a foundation for the Kalah game. The methods provided in the Kalah class override the Game class methods to build out the kalah game. Kalah rules were implemented such as extra turns, captures, and end game sweeps. If running this python file independently, it will play the kalah game in the terminal. 


## ui.py
The KalahUI class makes use of the PyQt6 framework to create the user interface. A simple board is drawn with 2 stores and 12 pits (1 store and 6 pits per player). The user is only allowed to select pits from their side, and given that there are beads in the pit as well. Capture and sweep are implemented, as well as a reset button. Methods are implemented to handle player choices, handle end of game, and resetting the game. 

## main.py 
Initializes Kalah and KalahUI class instances and displays the Qt window. 


## beads/ 
Contains six png files of beads. These files are used as beads to fill the stores and pits on the board in the UI. 

## requirements.txt
Contains the required packages to run the application.  

# Running Application 
- Run command ```pip install -r requirements.txt ``` 
- Run main.py file ```python3 main.py```