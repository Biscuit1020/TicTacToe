import random
import re
from typing import List, Optional, Tuple

import openai


class BaseTicTacToe:
    def __init__(self, size: int):
        """
        Initialize the Tic Tac Toe board with a given size and state variables
        to keep track of available moves and the board dynamically
        """
        self.size = size
        self.players = ["X", "O"]
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.available_moves = {
            (r, c) for r in range(1, size + 1) for c in range(1, size + 1)
        }
        self.current_player = "X"  # default user symbol is X
        self.row_counts = [0] * (size + 1)  # based 1-index
        self.col_counts = [0] * (size + 1)  # based 1-index
        self.diag_left_to_right_counts = 0
        self.diag_right_to_left_counts = 0

    def print_board(self) -> None:
        """
        Print the current state of the board
        """
        for row in self.board:
            print(" | ".join(row))
            print("-" * (self.size * 4 - 1))

    def make_move(self, row: int, col: int, player: str) -> bool:
        """
        Make a move on the board if the move is valid
        Args:
            row (int): row based 1-index
            col (int): column based 1-index
            player (str): Player making the move ('X' or 'O')
        Returns:
            True if the move was valid and completed, False otherwise
        """
        if (row, col) in self.available_moves:
            # board itself is not based 1-index
            self.board[row - 1][col - 1] = player
            self.available_moves.remove((row, col))

            determine_player = 1 if player == "X" else -1
            self.row_counts[row] += determine_player
            self.col_counts[col] += determine_player

            if row == col:
                self.diag_left_to_right_counts += determine_player
            if row == self.size - col + 1:
                self.diag_right_to_left_counts += determine_player

            return True
        return False

    def any_moves_left(self) -> List[Tuple[int, int]]:
        """
        List all available moves on the board
        Returns:
            List of tuples representing available moves
        """
        return list(self.available_moves)

    def is_game_over(self) -> None:
        """
        Check any_moves_left to determine if the game is over
        """
        if len(self.any_moves_left()) == 0:
            self.print_board()
            print("It's a draw!")

    def check_winner(self, player: str) -> bool:
        """
        Check if the current player has won the game

        Args:
            player (str): Player symbol ('X' or 'O')
        Returns:
            True if the player has won, False otherwise
        """
        determine_player = 1 if player == "X" else -1

        for i in range(1, self.size + 1):
            # determine if a row or column is all 1s or -1s
            if (
                self.row_counts[i] == self.size * determine_player
                or self.col_counts[i] == self.size * determine_player
            ):
                return True
        # determine if a diagonal is all 1s or -1s
        if (
            self.diag_left_to_right_counts == self.size * determine_player
            or self.diag_right_to_left_counts == self.size * determine_player
        ):
            return True
        # determine if the 4 corners are all X's or O's
        if (
            self.board[0][0]
            == self.board[0][self.size - 1]
            == self.board[self.size - 1][0]
            == self.board[self.size - 1][self.size - 1]
            == player
        ):
            return True
        # Check nxn box win if box is all X's or O's
        box_size = self.size // 2
        for start_row in range(self.size - box_size + 1):
            for start_col in range(self.size - box_size + 1):
                if all(
                    self.board[r][c] == player
                    for r in range(start_row, start_row + box_size)
                    for c in range(start_col, start_col + box_size)
                ):
                    return True

        return False

    def opponents_move(self, player: str) -> None:
        """
        Make a random move for the opponent
        Args:
            player (str):  Player symbol ('X' or 'O')
        """
        if self.available_moves:
            row, col = random.choice(list(self.available_moves))
            self.make_move(row, col, player)

    def is_valid_move(self, row: int, col: int) -> bool:
        """
        Check if a move is within range of the board
        Args:
            row (int): row based 1-index
            col (int): column based 1-index
        Returns:
            True if the move is valid, False otherwise
        """
        return 1 <= row <= self.size and 1 <= col <= self.size

    def get_player_input(
        self, use_ai: Optional[bool] = False, api_key: Optional[str] = None
    ) -> Tuple[int, int]:
        """
        Get player input specifying the row and column for the move
        Ensures the input is in the form of (row, col) and within the board limits

        Args:
            use_ai (bool): whether to use AI for suggesting a move
            api_key (str): API key for OpenAI (if using AI)

        Returns:
            Tuple[int, int]: representing the row and column selected by the player
        """
        if use_ai and api_key:
            suggestion = self.suggest_move(self.current_player, api_key=api_key)
            if suggestion:
                print(f"Suggested move: {suggestion[0]}, {suggestion[1]}")
                return suggestion[0], suggestion[1]
        while True:
            user_input = input(
                f"Enter your move as 'row,col' (1-{self.size}): "
            ).replace(" ", "")
            if re.match(r"^\d+,\d+$", user_input):
                row_str, col_str = user_input.split(",")
                try:
                    row, col = int(row_str), int(col_str)
                    if self.is_valid_move(row, col):
                        return row, col
                    else:
                        print(f"Coordinates must be between 1 and {self.size}.")
                except ValueError:
                    print("Both row and column must be integers.")
            else:
                print(
                    "Input must be in the form of 'row,col' with row,col as integers."
                )

    def switch_player(self) -> None:
        """
        Switch the current player to the other player
        """
        symbols = self.players
        # find the index of the current player ie. ['X', 'O']
        current_index = symbols.index(self.current_player)
        # add 1 to current_index and use the modulo operator for creating a cycle
        self.current_player = symbols[(current_index + 1) % len(symbols)]

    def player_move(
        self, use_ai: Optional[bool] = False, api_key: Optional[str] = None
    ) -> None:
        """
        Handle the player's move with input validation and error handling
        Args:
            use_ai (bool): whether to use AI for suggesting a move
            api_key (str): API key for OpenAI (if using AI)
        """
        while True:
            try:
                row, col = self.get_player_input(use_ai, api_key)
                if not self.is_valid_move(row, col):
                    raise ValueError(
                        f"Invalid move. Coordinates must be between 1 and {self.size}."
                    )
                if not self.make_move(row, col, self.current_player):
                    raise ValueError("Square already taken. Please choose another.")
                break
            except ValueError as e:
                print(e)

    def suggest_move(self, player: str, api_key: str) -> Tuple[int, int]:
        """
        Use the OpenAI API to suggest a move for the player.

        Args:
            player (str): Player symbol ('X' or 'O')
            api_key (str): API key for OpenAI (if using AI)
        Returns:
            Tuple representing the suggested row and column
        """
        openai.api_key = api_key
        board_str = "\n".join([" ".join(row) for row in self.board])
        prompt = (
            f"Here's the current tic-tac-toe board:\n{board_str}\n"
            f"Player {player}, what's your next move? "
            f"Provide the row and column as two space-separated numbers (e.g., '2 3'): "
        )

        try:
            response = openai.completions.create(
                model="gpt-3.5-turbo", prompt=prompt, max_tokens=10
            )
            move_str = response.choices[0].text.strip()
            row, col = map(int, move_str.split())
            if (row, col) in self.available_moves:
                return row, col
            return random.choice(list(self.available_moves))
        except (ValueError, IndexError, openai.RateLimitError) as e:
            print(
                f"Please check you have not exceeded your API quota. Error suggesting move: {e}"
            )
