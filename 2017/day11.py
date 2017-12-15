def main():
    # with open('input.txt') as file:
    with open('challenge_input.txt') as file:
        lines = list(map(str.strip, file.readlines()))

    farthest_distance = -1
    for line in lines:
        line = line.split(',')
        # Positive for NE, negative for SW
        ne_steps = 0
        # Positive for N, negative for S
        n_steps = 0
        # Positive for NW, negative for SE
        nw_steps = 0

        for step in line:
            if step == 'ne':
                ne_steps += 1
            elif step == 'sw':
                ne_steps -= 1
            elif step == 'n':
                n_steps += 1
            elif step == 's':
                n_steps -= 1
            elif step == 'nw':
                nw_steps += 1
            elif step == 'se':
                nw_steps -= 1

            temp_nw_steps, temp_ne_steps, temp_n_steps = simplify_position(nw_steps, ne_steps, n_steps)

            distance = abs(sum((temp_nw_steps, temp_n_steps, temp_ne_steps)))
            if distance > farthest_distance:
                farthest_distance = distance

        final_distance = abs(sum(simplify_position(nw_steps, n_steps, ne_steps)))
        print('Step 1 solution:', final_distance)
        print('Step 2 solution:', farthest_distance)

def simplify_position(nw_steps, ne_steps, n_steps):
    # NE + NW = N
    while ne_steps > 0 and nw_steps > 0:
        n_steps += 1
        ne_steps -= 1
        nw_steps -= 1
    # SW (-NE) + SE (-NW) = S (-N)
    while ne_steps < 0 and nw_steps < 0:
        n_steps -= 1
        ne_steps += 1
        nw_steps += 1

    # NE + S = SE (-NW)
    while ne_steps > 0 and n_steps < 0:
        nw_steps -= 1
        ne_steps -= 1
        n_steps += 1
    # SW (-NE) + N = NW
    while ne_steps < 0 and n_steps > 0:
        nw_steps += 1
        ne_steps += 1
        n_steps -= 1

    return nw_steps, ne_steps, n_steps


if __name__ == '__main__':
    main()