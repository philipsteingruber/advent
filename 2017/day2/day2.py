from itertools import combinations

def main():
    with open('input.txt') as file:
        rows = list(map(str.split, file.readlines()))

    rows = int_list(rows)

    checksum = sum([abs(max(row) - min(row)) for row in rows])

    checksum2 = 0
    for row in rows:
        combs = combinations(row, 2)
        for comb in combs:
            if max(comb) % min(comb) == 0:
                checksum2 += max(comb) // min(comb)
                break

    print('Part 1 solution:', checksum)
    print('Part 2 solution:', checksum2)


def int_list(li):
    res = []

    for sublist in li:
        res.append(list(map(int, sublist)))

    return res


if __name__ == '__main__':
    main()
