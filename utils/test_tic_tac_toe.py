import pytest
from main import validate_size
from tic_tac_toe import BaseTicTacToe


@pytest.mark.parametrize("size", [4, 8, 16])
def test_tic_tac_toe_board_initialized(size):
    game = BaseTicTacToe(size)
    assert game.size == size
    assert game.current_player == "X"  # default current_player is X
    assert game.board == [[" " for _ in range(size)] for _ in range(size)]
    assert game.available_moves == set(
        (r, c) for r in range(1, size + 1) for c in range(1, size + 1)
    )


@pytest.mark.parametrize("size", [4, 8, 16])
def test_initial_board_state(size):
    game = BaseTicTacToe(size)
    for row in game.board:
        assert all(cell == " " for cell in row)


@pytest.mark.parametrize("size", ["2", "5", "10"])
def test_invalid_board_size(size):
    with pytest.raises(ValueError):
        validate_size(size)


@pytest.mark.parametrize("size", ["k", "a", "h"])
def test_invalid_board_size_not_an_integer(size):
    with pytest.raises(ValueError):
        validate_size(size)


@pytest.mark.parametrize("size", [4, 8, 16])
def test_make_move(size):
    game = BaseTicTacToe(size)
    assert game.make_move(1, 1, game.current_player) is True
    assert game.board[0][0] == game.current_player
    assert (1, 1) not in game.available_moves


@pytest.mark.parametrize("size", [4, 8, 16])
def test_make_move_already_taken(size):
    game = BaseTicTacToe(size)
    game.make_move(1, 1, game.current_player)
    assert game.make_move(1, 1, "O") is False


@pytest.mark.parametrize("size", [4, 8, 16])
def test_make_move_invalid(size):
    game = BaseTicTacToe(size)
    assert game.make_move(size + 1, size + 1, game.current_player) is False
    assert game.make_move(0, 0, "O") is False


@pytest.mark.parametrize("size", [4, 8, 16])
def test_any_moves_left(size):
    game = BaseTicTacToe(size)
    assert len(game.any_moves_left()) == size * size
    game.make_move(1, 1, game.current_player)
    game.make_move(2, 2, "O")
    assert len(game.any_moves_left()) == size * size - 2


@pytest.mark.parametrize("size", [4, 8, 16])
def test_check_winner_horizontally(size):
    game = BaseTicTacToe(size)
    for i in range(1, size + 1):
        game.make_move(1, i, game.current_player)
    assert game.check_winner(game.current_player) is True


@pytest.mark.parametrize("size", [4, 8, 16])
def test_check_winner_vertically(size):
    game = BaseTicTacToe(size)
    for i in range(1, size + 1):
        game.make_move(i, 1, game.current_player)
    assert game.check_winner(game.current_player) is True


@pytest.mark.parametrize("size", [4, 8, 16])
def test_check_winner_diagonal_top_left_to_bottom_right(size):
    game = BaseTicTacToe(size)
    for i in range(1, size + 1):
        game.make_move(i, i, game.current_player)
    assert game.check_winner(game.current_player) is True


@pytest.mark.parametrize("size", [4, 8, 16])
def test_check_winner_diagonal_top_right_to_bottom_left(size):
    game = BaseTicTacToe(size)
    for i in range(1, size + 1):
        game.make_move(i, size - i + 1, game.current_player)
    assert game.check_winner(game.current_player) is True


@pytest.mark.parametrize("size", [4, 8, 16])
def test_check_winner_four_corners(size):
    game = BaseTicTacToe(size)
    corners = [(1, 1), (1, size), (size, 1), (size, size)]
    for r, c in corners:
        game.make_move(r, c, game.current_player)
    assert game.check_winner(game.current_player) is True


@pytest.mark.parametrize("size", [4, 8, 16])
def test_check_winner_nxn_box(size):
    game = BaseTicTacToe(size)
    box_size = size // 2

    fixed_start_row, fixed_start_col = 1, 1
    for r in range(fixed_start_row, fixed_start_row + box_size):
        for c in range(fixed_start_col, fixed_start_col + box_size):
            game.make_move(r, c, game.current_player)

    assert game.check_winner(game.current_player) is True
    assert game.check_winner("O") is False


@pytest.mark.parametrize("size", [4, 8, 16])
def test_partial_winner_detection(size):
    game = BaseTicTacToe(size)
    # scenario where no one has won yet
    for i in range(1, size // 2):
        game.make_move(i, i, game.current_player)
    assert game.check_winner(game.current_player) is False


@pytest.mark.parametrize("size", [4, 8, 16])
def test_game_over_draw(size):
    game = BaseTicTacToe(size)
    for r in range(1, size + 1):
        for c in range(1, size + 1):
            game.make_move(r, c, "X" if (r + c) % 2 == 0 else "O")
    game.is_game_over()  # print "It's a draw!"
