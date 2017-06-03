from operator import itemgetter

def main():
    with open("testinput.txt") as file:
        input = file.read().split("\n")

    repetition_message = []
    mod_repetition_message = []
    for i in range(len(input[0])):
        letter_counts = {}
        for line in input:
            if line[i] in letter_counts:
                letter_counts[line[i]] += 1
            else:
                letter_counts[line[i]] = 1

        sorted_letters = sorted(letter_counts.items(), key=itemgetter(1))[::-1]
        repetition_message.append(sorted_letters[0][0])
        mod_repetition_message.append(sorted_letters[len(sorted_letters)-1][0])

    print("Repetition message: {}".format("".join(repetition_message)))
    print("Modified repetition message: {}".format("".join(mod_repetition_message)))

if __name__ == "__main__":
    main()