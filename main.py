import os
import re

from ai_tic_tac_toe import AITicTacToe
from dotenv import load_dotenv
from tic_tac_toe import TicTacToe

load_dotenv(".env")
key = os.getenv("OPENAI_API_KEY")


def get_game_mode() -> str:
    """
    Get the game mode from the user input

    Returns:
        selected game mode ('classic' or 'ai')
    """
    while True:
        mode = (
            input("Choose game mode (AI, Classic, or press Enter for Classic): ")
            .strip()
            .lower()
        )
        if mode in ["", "classic", "ai"]:
            return "classic" if mode == "" else mode
        else:
            print(
                "Invalid input. Please enter 'AI', 'Classic', or press Enter for Classic."
            )


def validate_size(size: str) -> int:
    """
    Validate size of the board and ensure its an integer

    Args:
        size (str): size of the board
    Returns:
        int if its a valid board size
    Raises:
        ValueError: if the size is not castable to int or not a multiple of 4
    """
    pattern = re.compile(r"^\s*\d+\s*$")
    match = pattern.match(size)
    if match:
        size = int(size)
        if size < 4 or size % 4 != 0:
            raise ValueError("Board size must be a multiple of 4 and at least 4.")

        return size
    raise ValueError("Board size must be a single integer.")


def main():
    try:
        size = input("Enter the size of the board (must be a multiple of 4): ")
        size = validate_size(size)
        mode = get_game_mode()

        if mode == "ai":
            if not key:
                raise ValueError(
                    "API key is missing. Please set OPENAI_API_KEY in your .env file."
                )
            game = AITicTacToe(size, key)
            game.play_game(use_ai=True, api_key=key)
        else:
            game = TicTacToe(size)
            game.play_game(use_ai=False, api_key=None)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
