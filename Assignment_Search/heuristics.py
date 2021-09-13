def number_of_misplaced_tiles(state, goal_state, size):
    total = 0
    for row in range(size):
        for col in range(size):
            if goal_state[row][col] != state[row][col]:
                total += 1
    return total


def manhattan_distance(tile, r, c, size, goal_state):
    if tile == '-':
        return 0
    for row in range(size):
        for col in range(size):
            if goal_state[row][col] == tile:
                return abs(row - r) + abs(col - c)


def total_manhattan_distance(state, size,goal_state):
    total = 0
    for r in range(size):
        for c in range(size):
            total += manhattan_distance(state[r][c], r, c,size,goal_state)
    return total


def get_heuristic(name):
    if name == 'misplaced':
        return number_of_misplaced_tiles
    elif name == 'manhattan':
        return total_manhattan_distance
    else:
        raise NotImplementedError("Given heuristic is not implemented")
