# checks if there is a winning sequence on the board

def check_if_win(placements):
    row_win = check_row(placements, 0) or check_row(placements, 1) or check_row(placements, 2)
    col_win = check_col(placements, 0) or check_col(placements, 1) or check_col(placements, 2)
    diag_win = check_diag(placements)
    return row_win or col_win or diag_win


def check_col(placements, col):
    return placements[0][col] == placements[1][col] and placements[0][col] == placements[2][col]


def check_row(placements, row):
    return placements[row][0] == placements[row][1] and placements[row][0] == placements[row][2]


def check_diag(placements):
    front = placements[0][0] == placements[1][1] and placements[0][0] == placements[2][2]
    back = placements[2][0] == placements[1][1] and placements[2][0] == placements[0][2]
    return front or back