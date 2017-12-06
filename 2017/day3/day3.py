from math import floor

def main():
    input = 368078
    print('Input:', input)


    side_length = 1
    while True:
        if side_length ** 2 > input:
            print('Side length:', side_length, 'Bottom right:', side_length ** 2)
            break
        side_length += 2

    middle = side_length ** 2 - floor(side_length // 2)
    print('Middle of bottom row:', middle)

    distance_to_middle_x = abs(input - middle)
    print('Distance to middle (x):', distance_to_middle_x)

    distance_to_middle_y = floor(side_length / 2)
    print('Distance to middle (y):', distance_to_middle_y)

    print('End result:', distance_to_middle_x+distance_to_middle_y)

if __name__ == '__main__':
    main()
