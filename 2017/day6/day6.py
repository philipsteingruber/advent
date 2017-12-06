def main(step2):
    input = [0, 2, 7, 0]
    with open('input.txt') as file:
        input = list(map(int, file.read().split()))

    configurations = [list(input)]
    first_seen = {}

    redistributions = 0

    while True:
        redistributions += 1
        bank_to_redistribute = input.index(max(input))

        blocks_to_redistribute = input[bank_to_redistribute]

        input[bank_to_redistribute] = 0

        current_bank = (bank_to_redistribute + 1) % len(input)

        while blocks_to_redistribute > 0:
            input[current_bank] += 1
            current_bank = (current_bank + 1) % len(input)
            blocks_to_redistribute -= 1

        if not step2:
            if input in configurations:
                print('Step 1 solution:', redistributions)
                break
            else:
                configurations.append(list(input))
        else:
            input_tuple = tuple(input)
            if input_tuple in first_seen:
                print('Step 2 solution:', redistributions - first_seen[input_tuple])
                break
            else:
                first_seen[input_tuple] = redistributions


if __name__ == '__main__':
    main(False)
    main(True)
