def main():
    with open("input.txt") as file:
        input = file.read().split()

    for line in input:
        res = []
        for i in range(len(line)):
            char = line[i]
            if char != "(":
                res.append(char)
            else:
                decompressed = []
                for j in range(i, len(line)):
                    end_char = line[j]
                    if end_char = ")":
                        marker = char[i+1:j]
                        print(marker)

if __name__ == "__main__":
    main()