def step1():
    with open("input.txt") as file:
        input = file.read()

    res = []
    i = 0
    while i in range(len(input)):
        char = input[i]
        if char != "(":
            res.append(char)
        else:
            for j in range(i, len(input)):
                end_char = input[j]
                if end_char == ")":
                    marker = input[i+1:j]
                    num, reps = map(int, marker.split("x"))
                    repeat_letters = input[j+1:j+num+1]
                    res.extend(repeat_letters * reps)
                    i += num + len(marker) + 1
                    break
        i += 1
    res = "".join(res)
    print("Length is {}.".format(len(res)))


if __name__ == "__main__":
    step1()
