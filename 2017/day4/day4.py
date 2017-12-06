from collections import Counter
from operator import itemgetter

def main():
    with open('input.txt') as file:
        phrases = list(map(str.split, file.readlines()))

    valid_phrases_step1 = 0
    valid_phrases_step2 = 0

    for phrase in phrases:
        # Step 1
        if sorted(list(Counter(phrase).items()), key=itemgetter(1), reverse=True)[0][1] == 1:
            valid_phrases_step1 += 1

        # Step 2
        sorted_words = list(map(''.join, map(sorted, phrase)))
        if sorted(list(Counter(sorted_words).items()), key=itemgetter(1), reverse=True)[0][1] == 1:
            valid_phrases_step2 += 1

    print('Step 1:', valid_phrases_step1)
    print('Step 2:', valid_phrases_step2)

if __name__ == '__main__':
    main()
