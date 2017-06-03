def main():
    # with open("input.txt") as file:
    with open("testinput.txt") as file:
        input = file.read()

    res = []
    i = 0
    while i in range(len(input)):
        char = input[i]
        if char != "(":
            res.append(char)
        else:
            decompressed = []
            for j in range(i, len(input)):
                end_char = input[j]
                if end_char == ")":
                    marker = input[i+1:j]
                    print("i: {}, j: {}".format(i, j))
                    print("input[i]: {}".format(input[i]))
                    print("input[j]: {}".format(input[j]))
                    # print(marker)
                    num, reps = map(int, marker.split("x"))
                    res.extend(input[j+1:j+num+1] * (reps - 1))
                    i += num + len(marker)
                    break
        i += 1
    res = "".join(res)
    print("Decompressed line is {}.".format(res))
    print("Length is {}.".format(len(res)))

if __name__ == "__main__":
    main()