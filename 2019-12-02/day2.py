OPCODES = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
}


TERMINATION_CODE = 99


def split_codes(op_codes, start):
    start_op_code = op_codes[start]
    if (start_op_code == TERMINATION_CODE):
        return [start_op_code]
    return op_codes[start:start+4]


def intcode_reader(initial_state):
    split_op_codes = []
    program = [int(x) for x in initial_state.split(',')]
    for i in range(0, len(program), 4):
        intcode = split_codes(program, i)
        if (intcode == [99]):
            break
        split_op_codes.append(intcode)
    return split_op_codes


def get_value_and_index(code, intcodes):
    opcode, input1, input2, output_position = code
    return OPCODES[opcode](intcodes[input1], intcodes[input2]), output_position


def run_code(intcodes):
    i = 0
    while (i < len(intcodes)):
        code = split_codes(intcodes, i)
        if code == [TERMINATION_CODE]:
            break
        val, index = get_value_and_index(code, intcodes)
        intcodes[index] = val
        i += 4
    return ','.join((str(x) for x in intcodes))


def part_1(initial_state, noun, verb):
    intcodes = [int(x) for x in initial_state.split(',')]
    intcodes[1] = noun
    intcodes[2] = verb
    return run_code(intcodes).split(',')[0]


if __name__ == "__main__":
    with open('input.txt') as f:
        initial_state = f.read()
        for noun in range(100):
            for verb in range(100):
                output = part_1(initial_state, noun, verb)
                if output == 19690720:
                    print(output, noun, verb, 100*noun+verb)
        
        output = part_1(initial_state, 12, 2)
        print(output, 12, 2, 100*12+2)
