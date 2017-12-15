def knot_hash(iterations, list_size, lengths):

    numbers = list(range(list_size))

    current_pos = 0
    skip_size = 0
    for _ in range(iterations):
        for length in lengths:
            if length > len(numbers) or length == 1 or length == 0:
                current_pos, skip_size = move_position_and_skip(current_pos, skip_size, length, len(numbers))
                continue
            start, end = current_pos, (current_pos + length) % len(numbers)

            orig_list = numbers.copy()

            # List has wrapped around
            if end <= start:
                reversed_list = (orig_list[start:] + orig_list[:end])[::-1]
                loop_indexes = list(range(start, len(numbers))) + list(range(0, end))

                for index, new_element in zip(loop_indexes, reversed_list):
                    numbers[index] = new_element
            # List hasn't wrapped around
            else:
                for i in range(start, end):
                    numbers[i] = orig_list[start+end-i-1]

            current_pos, skip_size = move_position_and_skip(current_pos, skip_size, length, len(numbers))
    return numbers


def move_position_and_skip(current_pos, current_skip, length, len_numbers):
    pos = (current_pos + length + current_skip) % len_numbers
    skip = current_skip + 1
    return pos, skip

if __name__ == '__main__':
    step1_lengths = list(map(int, '102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216'.split(',')))
    step1_solution = knot_hash(iterations=1, list_size=256, lengths=step1_lengths)
    print('Step 1 solution:', step1_solution[0] * step1_solution[1])

    step2_input = '102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216'
    step2_lengths = []
    for character in step2_input:
        step2_lengths.append(ord(character))

    step2_lengths += [17, 31, 73, 47, 23]

    sparse_hash = knot_hash(iterations=64, list_size=256, lengths=step2_lengths)

    dense_hash = []
    for i in range(16):
        numbers = sparse_hash[16*i:16*i+16]
        rolling_sum = numbers[0]
        for number in numbers[1:]:
            rolling_sum = rolling_sum ^ number
        dense_hash.append(rolling_sum)

    hex_string = []
    for number in dense_hash:
        hex_string.append(hex(number)[2:].zfill(2))

    print('Step 2 solution:', ''.join(hex_string))
