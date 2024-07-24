from typing import Optional

import openai
from utils.base_tic_tac_toe import BaseTicTacToe


class AITicTacToe(BaseTicTacToe):
    """
    A Tic-Tac-Toe game implementation using OpenAI API
    """

    def __init__(self, size: int, api_key: str):
        super().__init__(size)
        openai.api_key = api_key

    def play_game(
        self, use_ai: Optional[bool] = False, api_key: Optional[str] = None
    ) -> None:
        """
        Starts the game loop, allowing players to take turns until there is a winner or the game ends in a draw
        Args:
            use_ai: Optional if True, uses AI for player X's moves, defaults to False
        """
        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn")

            if self.current_player == "X":
                self.player_move(use_ai, api_key)
            else:
                self.opponents_move(self.current_player)

            if self.check_winner(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                return
            elif self.is_game_over():
                return

            self.switch_player()
