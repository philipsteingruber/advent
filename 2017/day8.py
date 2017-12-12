from collections import defaultdict
import re
import operator

def main():
    with open('input.txt') as file:
        instructions = file.readlines()

    comparison_ops = {
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
        '>=': operator.ge,
        '>': operator.gt
    }

    math_ops = {
        'inc': operator.add,
        'dec': operator.sub
    }

    registers = {}
    instruction_pattern = re.compile(r'(\w+) (inc|dec) (-?\d+) if (.+)')
    condition_pattern = re.compile(r'(\w+) (!=|==|>=|<=|<|>) (-?\d+)')

    highest_value = -1
    for instruction in instructions:
        register, operation, value, condition = re.match(instruction_pattern, instruction).groups()
        operation = math_ops.get(operation)
        condition_register, condition_operator, condition_value = re.match(condition_pattern, condition).groups()

        condition_operator = comparison_ops.get(condition_operator)

        if register not in registers:
            registers[register] = 0
        if condition_register not in registers:
            registers[condition_register] = 0

        if execute(registers[condition_register], condition_operator, int(condition_value)):
            registers[register] = execute(registers[register], operation, int(value))
            if registers[register] > highest_value:
                highest_value = registers[register]


    print('Step 1 solution:', max(registers.values()))
    print('Step 2 solution:', highest_value)


def execute(arg1, op, arg2):
    return op(arg1, arg2)


if __name__ == '__main__':
    main()