def main(step2):
    with open('input.txt') as file:
        # input = [0, 3, 0, 1, -3]
        input = list(map(int, file.readlines()))

    steps_taken = 0
    current_index =  0

    while current_index < len(input):
        old_value = input[current_index]
        if not step2:
            input[current_index] += 1
        else:
            if old_value >= 3:
                input[current_index] -= 1
            else:
                input[current_index] += 1

        current_index += old_value

        steps_taken += 1

    if not step2:
        print('Step 1 solution:', steps_taken)
    else:
        print('Step 2 solution:', steps_taken)

if __name__ == '__main__':
    main(False)
    main(True)
