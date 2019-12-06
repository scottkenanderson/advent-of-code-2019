def move_right(last_coordinate, movement):
    last_x, last_y = last_coordinate
    return [(i, last_y) for i in range(last_x+1, last_x+movement+1)]


def move_left(last_coordinate, movement):
    last_x, last_y = last_coordinate
    return [(i, last_y) for i in range(last_x-1, last_x-movement-1, -1)]


def move_up(last_coordinate, movement):
    last_x, last_y = last_coordinate
    return [(last_x, i) for i in range(last_y+1, last_y+movement+1)]


def move_down(last_coordinate, movement):
    last_x, last_y = last_coordinate
    return [(last_x, i) for i in range(last_y-1, last_y-movement-1, -1)]


MOVE = {
    'R': move_right,
    'L': move_left,
    'U': move_up,
    'D': move_down,
}


def get_wire_coordinates(path):
    coordinates = [(0,0)]
    for p in path.split(','):
        operation = MOVE[p[0]]
        coordinates.extend(operation(coordinates[-1], int(p[1:])))
    return coordinates


def get_manhattan_distance(origin, coordinate):
    dist_x = abs(origin[0]) + abs(coordinate[0])
    dist_y = abs(origin[1]) + abs(coordinate[1])
    return dist_x + dist_y


def get_wires(wire_paths):
    wire1 = get_wire_coordinates(wire_paths[0])
    wire2 = get_wire_coordinates(wire_paths[1])
    return wire1, wire2


def get_intersections(wire1, wire2):
    return list(set(wire1).intersection(set(wire2)))[1:]


def run_code(wire_paths):
    wire1, wire2 = get_wires(wire_paths)
    intersections = get_intersections(wire1, wire2)
    distances = [get_manhattan_distance((0,0), intersection) for intersection in intersections]
    return min(filter(lambda x: x > 0, distances))


def get_initial_state(filename):
    with open(filename) as f:
        return f.read()


def part_1(initial_state):
    return run_code(initial_state.split('\n'))


def part_2(initial_state):
    wire1, wire2 = get_wires(initial_state.split('\n'))
    intersections = get_intersections(wire1, wire2)
    return min(filter(lambda x: x > 0, [wire1.index(i) + wire2.index(i) for i in intersections]))


if __name__ == "__main__":
    initial_state = get_initial_state('input.txt')
    print(part_1(initial_state))
    print(part_2(initial_state))

