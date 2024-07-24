# Tic Tac Toe Game

Looking to play a game of Tic Tac Toe?
Not sure how to play? Fear not!

The game is easy. There are two players that each take turns marking and an nxn grid. The grid or as we call it board, can be marked either with an X or an O. The default symbol for the user player is X and the opponent is O.

There are 5 winnning conditions:

1) mark all the rows with your symbol
2) mark all the columns with your symbol
3) mark all the diagonals (left top corner to right bottom corner)
or (right top corner to left bottom corner)
4) mark all 4 corners
5) mark an nxn//2 box ie. a 4x4 grid would require a 2x2 box to win and an 8x8 grid would require a 4x4 box to win

## Features

- Play Tic Tac Toe against a random opponent
- Option to get move suggestions from OpenAI's GPT-3.5 model
- Configurable board size in increments of 4

## Getting Started

1. Clone the repository:

    ```sh
    git clone https://github.com/Biscuit1020/TicTacToe.git
    ```

2. Install the required packages:

    ```sh
    pip install requirements.txt
    ```

3. Get your OpenAI API key
   **see further instructions at the end of the document**

## Usage

### Classic Version

By default, the game is set to play the classic version:

1. Run the `main.py` script:

    ```sh
    python3 main.py
    ```

2. Enter the size of the board (must be a multiple of 4):
3. Choose the game mode by typing `classic` or nothing (default classic)

### AI-assisted Version

To play the AI-assisted version of the game:

1. Run the `main.py` script:

    ```sh
    python3 main.py
    ```

2. Enter the size of the board (must be a multiple of 4):
3. Choose the game mode by typing `AI`
4. If playing in `AI` mode, you will need to add your openAI_api_key to a .env file

## File Structure

```
TicTacToe/
├────utils/
    └──base_tictactoe.py
├── tic_tac_toe.py
├── ai_tic_tac_toe.py
├── main.py
└── README.md
```

### `base_tic_tac_toe.py`

Contains the base class `BaseTicTacToe` with common game logic

### `tic_tac_toe.py`

Contains the `TicTacToe` class, inheriting from `BaseTicTacToe`, for the classic game mode

### `ai_tic_tac_toe.py`

Contains the `AITicTacToe` class, inheriting from `BaseTicTacToe`, for the AI-assisted game mode
Includes the logic for suggesting moves using OpenAI's GPT-3.5 model

### `main.py`

The main script to run the game
Allows the user to choose specify if they want to use the AI-assisted version


## OpenAI API Key Instructions

 1. Go to the OpenAI website and log in to your account

 2. Navigate to API Keys:
    Once logged in, go to the API section of the dashboard
    This can typically be found under your account settings or a dedicated API section.

 3. Generate or View API Key:
    If you haven't generated an API key yet, you can create. If you have already generated an API key, you should be able to view it.

 4. **Add the API Key to the .env File:**
   Open a `.env` file and copy paste the API key like below

   ```sh
   OPENAI_API_KEY=openai_api_key
   ```

## Code Development

 To run the linters at the directory level run:
    `flake8 .`
    `black .`
    `isort .`
