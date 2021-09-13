import argparse
from utils import read_data
from heuristics import get_heuristic
# define file names

parser = argparse.ArgumentParser("Modified N puzzle solver")
parser.add_argument("--start", type=str, default="Sample_Start_Configuration.txt")
parser.add_argument("--goal", type=str, default="Sample_Goal_Configuration.txt")
parser.add_argument("--output", type=str, default="Output.txt")
parser.add_argument("--heuristic", type=str, default="misplaced",choices=['misplaced', 'manhattan'])
parser.add_argument("--print_path",action='store_true')
args = parser.parse_args()
output_file_name = args.output




# read from input files
start_state = read_data(args.start)
goal_state = read_data(args.goal)

size = len(start_state)


# return hamming distance (number of misplaced tiles)



# return manhattan distance



# return total manhattan distance



# heuristic value --> return total manhattan distance or hamming distance




h = get_heuristic(args.heuristic)


class Node:
    def __init__(self, state, parent, g):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h(state=state,goal_state=goal_state,size=size)

    def f(self):
        return self.g + self.h


open_set = [Node(start_state, None, 0)]
closed_set = []


# return the state in OPEN which has the minimum f value
def get_min_node():
    min_node = open_set[0]
    min_f = open_set[0].f()
    for state in open_set[1:]:
        if state.f() < min_f:
            min_node = state
            min_f = state.f()
    return min_node


# return the state in OPEN which has the same configuration given in parameter
def get_open_node(node):
    for open_node in open_set:
        if open_node.state == node.state:
            return open_node


# return possible next states

def get_dash_locations(current_node):
    dash_one = None
    dash_two = None
    for row in range(size):
        for col in range(size):
            if current_node.state[row][col] == '-':
                if dash_one == None:
                    dash_one = (row, col)
                else:
                    dash_two = (row, col)
    return dash_one, dash_two


def next_nodes(current_node):
    dash_one, dash_two = get_dash_locations(current_node)
    nodes = []

    if dash_one[0] - 1 >= 0 and current_node.state[dash_one[0] - 1][dash_one[1]] != '-':
        temp_conf = [x[:] for x in current_node.state]
        temp_conf[dash_one[0]][dash_one[1]], temp_conf[dash_one[0] - 1][dash_one[1]] = \
            temp_conf[dash_one[0] - 1][dash_one[1]], temp_conf[dash_one[0]][dash_one[1]]
        nodes.append(Node(temp_conf, current_node, current_node.g + 1))
    if dash_one[0] + 1 <= (size - 1) and current_node.state[dash_one[0] + 1][dash_one[1]] != '-':
        temp_conf = [x[:] for x in current_node.state]
        temp_conf[dash_one[0]][dash_one[1]], temp_conf[dash_one[0] + 1][dash_one[1]] = \
            temp_conf[dash_one[0] + 1][dash_one[1]], temp_conf[dash_one[0]][dash_one[1]]
        nodes.append(Node(temp_conf, current_node, current_node.g + 1))
    if dash_one[1] - 1 >= 0 and current_node.state[dash_one[0]][dash_one[1] - 1] != '-':
        temp_conf = [x[:] for x in current_node.state]
        temp_conf[dash_one[0]][dash_one[1]], temp_conf[dash_one[0]][dash_one[1] - 1] = \
            temp_conf[dash_one[0]][dash_one[1] - 1], temp_conf[dash_one[0]][dash_one[1]]
        nodes.append(Node(temp_conf, current_node, current_node.g + 1))
    if dash_one[1] + 1 <= (size - 1) and current_node.state[dash_one[0]][dash_one[1] + 1] != '-':
        temp_conf = [x[:] for x in current_node.state]
        temp_conf[dash_one[0]][dash_one[1]], temp_conf[dash_one[0]][dash_one[1] + 1] = \
            temp_conf[dash_one[0]][dash_one[1] + 1], temp_conf[dash_one[0]][dash_one[1]]
        nodes.append(Node(temp_conf, current_node, current_node.g + 1))

    if dash_two[0] - 1 >= 0 and current_node.state[dash_two[0] - 1][dash_two[1]] != '-':
        temp_conf = [x[:] for x in current_node.state]
        temp_conf[dash_two[0]][dash_two[1]], temp_conf[dash_two[0] - 1][dash_two[1]] = \
            temp_conf[dash_two[0] - 1][dash_two[1]], temp_conf[dash_two[0]][dash_two[1]]
        nodes.append(Node(temp_conf, current_node, current_node.g + 1))
    if dash_two[0] + 1 <= (size - 1) and current_node.state[dash_two[0] + 1][dash_two[1]] != '-':
        temp_conf = [x[:] for x in current_node.state]
        temp_conf[dash_two[0]][dash_two[1]], temp_conf[dash_two[0] + 1][dash_two[1]] = \
            temp_conf[dash_two[0] + 1][dash_two[1]], temp_conf[dash_two[0]][dash_two[1]]
        nodes.append(Node(temp_conf, current_node, current_node.g + 1))
    if dash_two[1] - 1 >= 0 and current_node.state[dash_two[0]][dash_two[1] - 1] != '-':
        temp_conf = [x[:] for x in current_node.state]
        temp_conf[dash_two[0]][dash_two[1]], temp_conf[dash_two[0]][dash_two[1] - 1] = \
            temp_conf[dash_two[0]][dash_two[1] - 1], temp_conf[dash_two[0]][dash_two[1]]
        nodes.append(Node(temp_conf, current_node, current_node.g + 1))
    if dash_two[1] + 1 <= (size - 1) and current_node.state[dash_two[0]][dash_two[1] + 1] != '-':
        temp_conf = [x[:] for x in current_node.state]
        temp_conf[dash_two[0]][dash_two[1]], temp_conf[dash_two[0]][dash_two[1] + 1] = \
            temp_conf[dash_two[0]][dash_two[1] + 1], temp_conf[dash_two[0]][dash_two[1]]
        nodes.append(Node(temp_conf, current_node, current_node.g + 1))

    return nodes


# get move between two given states
def get_move(from_node, to_node):
    move = "("
    for row in range(size):
        for col in range(size):
            if from_node.state[row][col] != to_node.state[row][col] and from_node.state[row][col] != '-':
                move += from_node.state[row][col] + ","
                if row - 1 >= 0 and from_node.state[row][col] == to_node.state[row - 1][col]:
                    move += "up)"
                if row + 1 <= (size - 1) and from_node.state[row][col] == to_node.state[row + 1][col]:
                    move += "down)"
                if col - 1 >= 0 and from_node.state[row][col] == to_node.state[row][col - 1]:
                    move += "left)"
                if col + 1 <= (size - 1) and from_node.state[row][col] == to_node.state[row][col + 1]:
                    move += "right)"
                break
    return move


# return the total path
def reconstruct_path(current_node):
    total_path = []
    while current_node.parent != None:
        total_path.append(get_move(current_node.parent, current_node))
        current_node = current_node.parent
    total_path.reverse()
    return total_path


# check whether given state is in OPEN
def is_in_OPEN(node):
    for open_node in open_set:
        if open_node.state == node.state:
            return True
    return False


# check whether given state is in CLOSED
def is_in_CLOSED(node):
    for closed_node in closed_set:
        if closed_node.state == node.state:
            return True
    return False


# A* search
def A():
    solution_lenth = 0
    while len(open_set) > 0:
        solution_lenth += 1
        current_node = get_min_node()
        if current_node.state == goal_state:
            print(solution_lenth)
            return reconstruct_path(current_node)
        open_set.remove(current_node)
        closed_set.append(current_node)
        for next_state in next_nodes(current_node):
            if is_in_CLOSED(next_state):
                continue
            if not (is_in_OPEN(next_state)):
                open_set.append(next_state)
            else:
                open_state = get_open_node(next_state)
                if next_state.g < open_state.g:
                    open_state.g = next_state.g
                    open_state.parent = next_state.parent


# write to output file
# fo = open(output_file_name, "w")
PATH = A()
if args.print_path:
    print(PATH)
# fo.write(", ".join(PATH))
# fo.close()
