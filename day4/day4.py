import operator
import re
from string import ascii_lowercase as lower_letters



def main():
    file = open("testinput.txt")
    inputdata = file.read().split("\n")
    # inputdata = "a-b-c-d-e-f-g-h-987[abcde]"
    file.close()

    sum_ids = 0
    valid_rooms = []

    for line in inputdata:
        letters, checksum = re.split(r"\d+", line)

        letter_dict = {}

        for letter in letters:
            if letter.isalpha():
                if letter in letter_dict:
                    letter_dict[letter] += 1
                else:
                    letter_dict[letter] = 1

        sorted_letters = sorted(letter_dict.items(), key=operator.itemgetter(1))[::-1]

        reverse_dict = {}

        for letter, count in sorted_letters:
            if count in reverse_dict:
                reverse_dict[count] += letter
            else:
                reverse_dict[count] = letter

        correct_checksum = ""
        sorted_counts = sorted(reverse_dict.items(), key=operator.itemgetter(0))[::-1]

        for count, letters in sorted_counts:
            if len(letters) == 1:
                correct_checksum += letters
            else:
                correct_checksum += "".join(sorted(letters))
        # Length of checksum is always 5
        correct_checksum = correct_checksum[:5]

        if correct_checksum == checksum[1:-1]:
            sector_id = re.split(r"-", line)
            sector_id = re.split(r"\[", sector_id[-1])
            sum_ids += int(sector_id[0])
            valid_rooms.append(line)

    print(sum_ids)
    print(len(valid_rooms))

    unencrypted_rooms = []

    for room in valid_rooms:
        letters = re.split(r"\d+", room)[0]
        rotated_letters = ""
        sector_id = re.split(r"-", room)
        sector_id = int(re.split(r"\[", sector_id[-1])[0])

        for letter in letters:
            if letter.isalpha():
                rotated_letters += lower_letters[(lower_letters.index(letter) + sector_id) % len(lower_letters)]
            else:
                rotated_letters += " "

        unencrypted_rooms.append(rotated_letters+" "+str(sector_id))

    file = open("output.txt", mode="w")
    for room in unencrypted_rooms:
        file.write(room + "\n")
    file.close()



if __name__ == "__main__":
    main()
