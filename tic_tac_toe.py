from typing import Optional

from utils.base_tic_tac_toe import BaseTicTacToe


class TicTacToe(BaseTicTacToe):
    """
    A Tic-Tac-Toe game implementation that inherits from BaseTicTacToe
    """

    def __init__(self, size: int):
        """
        Initializes the TicTacToe game with the given board size

        Args:
            size (int): size of the board
        """
        super().__init__(size)

    def play_game(
        self, use_ai: Optional[bool] = False, api_key: Optional[str] = None
    ) -> None:
        """
        Starts the game loop, allowing players to take turns until there is a winner or the game ends in a draw
        Args:
            use_ai: Optional if True, uses AI for player X's moves. Defaults to False.
            api_key (str): API key for OpenAI (if using AI)
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

            if not self.any_moves_left():
                self.print_board()
                print("It's a draw!")
                return

            self.switch_player()
