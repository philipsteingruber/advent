import re
import collections

def main():
    bot = collections.defaultdict(list)
    output = collections.defaultdict(list)

    with open("input.txt") as file:
        data = file.read().split("\n")

    commands = {}
    for line in data:
        if line.startswith("value"):
            val, b = map(int, re.findall(r"\d+", line))
            bot[b].append(val)
        if line.startswith("bot"):
            source, no_low, no_high = map(int, re.findall(r"\d+", line))
            type_low, type_high = re.findall(r" (bot|output)", line)
            commands[source] = (type_low, no_low), (type_high, no_high)

    while bot:
        for k, v in dict(bot).items():
            if len(v) == 2:
                val1, val2 = sorted(bot.pop(k))
                if val1 == 17 and val2 == 61:
                    print("Answer:", k)
                (type1, target1), (type2, target2) = commands[k]
                eval(type1)[target1].append(val1)
                eval(type2)[target2].append(val2)

    prod = 1
    for i in range(3):
        prod *= output[i][0]
    print("Product:", prod)

if __name__ == "__main__":
    main()
