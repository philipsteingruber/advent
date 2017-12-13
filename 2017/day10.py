from collections import Counter

def main():
    # lengths = list(map(int, '3,4,1,5'.split(',')))
    lengths = list(map(int, '102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216'.split(',')))

    list_size = 256
    numbers = list(range(list_size))

    current_pos = 0
    skip_size = 0

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
    print(numbers)
    print('Step 1 solution:', numbers[0] * numbers[1])

def move_position_and_skip(current_pos, current_skip, length, len_numbers):
    pos = (current_pos + length + current_skip) % len_numbers
    skip = current_skip + 1
    return pos, skip

if __name__ == '__main__':
    main()