from operator import itemgetter

def step1():
    with open("input.txt") as file:
        input = file.read().split("\n")

    message = []
    for i in range(len(input[0])):
        letter_counts = {}
        for line in input:
            if line[i] in letter_counts:
                letter_counts[line[i]] += 1
            else:
                letter_counts[line[i]] = 1

        sorted_letters = sorted(letter_counts.items(), key=itemgetter(1))[::-1]
        message.append(sorted_letters[0][0])

    print("".join(message))

if __name__ == "__main__":
    step1()