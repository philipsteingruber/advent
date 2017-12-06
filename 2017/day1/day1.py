def part1():
    with open('input.txt') as file:
        numbers = file.read()

    sum = 0
    for index, number in enumerate(numbers):
        if number == numbers[(index+1) % len(numbers)]:
            sum += int(number)

    print('Part 1 solution:', sum)

def part2():
    with open('input.txt') as file:
        numbers = file.read()

    step = len(numbers) // 2

    sum = 0
    for index, number in enumerate(numbers):
        if number == numbers[(index+step) % len(numbers)]:
            sum += int(number)

    print('Part 2 solution:', sum)

if __name__ == '__main__':
    part1()
    part2()
