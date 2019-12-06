from collections import defaultdict


def check_password(password):
    if len(password) != 6:
        return False

    last = password[0]
    return_value = False

    for x in password[1:]:
        if last > x:
            return False
        return_value = return_value or last == x
        last = x

    return return_value


def check_extended_password(password):
    if len(password) != 6:
        return False

    last = '-1'
    count = defaultdict(int)

    for x in password:
        if last > x:
            return False
        if (last == x):
            if count[x] == 0:
                count[x] += 1
            count[x] += 1
        last = x
    return any([x == 2 for x in count.values()])


def get_initial_state(filename):
    with open(filename) as f:
        return f.read().split('-')


def part_1(initial_state):
    start, end = initial_state
    nums = [check_password(str(i)) for i in range(int(start), int(end))]
    return len(list(filter(lambda x: x, nums)))


def part_2(initial_state):
    start, end = initial_state
    nums = [check_extended_password(str(i)) for i in range(int(start), int(end))]
    return len(list(filter(lambda x: x, nums)))


if __name__ == "__main__":
    initial_state = get_initial_state('input.txt')
    print(part_1(initial_state))
    print(part_2(initial_state))

