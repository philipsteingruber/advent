from collections import deque

def main():
    with open('input.txt') as file:
        streams = file.readlines()


    garbage = False
    for stream in streams:
        nested_level = 0
        stream = stream.strip()
        group_scores = []
        characters_to_skip = 0
        garbage_characters = 0

        for character in stream:
            if not characters_to_skip:
                if character == '!':
                    characters_to_skip += 1
                    continue
                if not garbage:
                    if character == '{':
                        nested_level += 1
                    elif character == '}':
                        if nested_level:
                            group_scores.append(nested_level)
                            nested_level -= 1
                    elif character == '<':
                        garbage = True
                else:
                    if character == '>':
                        garbage = False
                    else:
                        garbage_characters += 1
            else:
                characters_to_skip -= 1
        # print(stream, 'has', len(group_scores), 'groups. Score is', sum(group_scores))
        print('Step 1 solution:', sum(group_scores))
        print('Step 2 solution:', garbage_characters)


if __name__ == '__main__':
    main()