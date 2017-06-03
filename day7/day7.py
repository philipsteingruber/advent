import regex as re


def main():
    with open("testinput.txt") as file:
        input = file.read().split()

    count_tls = count_ssl = 0
    for line in input:
        outsides = re.split(r"\[\w+\]", line)
        insides = re.findall(r"\[\w+\]", line)
        insides = [x[1:-1] for x in insides]

        if is_tls(outsides, insides):
            count_tls += 1
        if is_ssl(outsides, insides):
            count_ssl += 1

    print("Valid IPs (TLS): {}".format(count_tls))
    print("Valid IPs (SSL): {}".format(count_ssl))


def has_abba(s):
    match = re.search(r"((?P<first>\w)(?P<second>\w))(?P=second)(?P=first)", s)
    if bool(match):
        matched_letters = match.group(1)
        return matched_letters[0] != matched_letters[1]
    else:
        return False


def has_aba(s):
    matches = re.findall(r"((?P<first>\w)(?P<second>\w))(?P=first)", s, overlapped=True)
    final_matches = []
    if (len(matches)):
        for match in matches:
            match = match[0]
            match += match[0]
            if match[0] != match[1]:
                final_matches.append(match)
        return final_matches
    else:
        return None


def is_ssl(outs, ins):
    for item in outs:
        abas = has_aba(item)
        if abas != None:
            for aba in abas:
                bab = aba[1] + aba[0] + aba[1]
                for elem in ins:
                    if elem.find(bab) != -1:
                        return True
    return False



def is_tls(outs, ins):
    tls = False
    for item in outs:
        if has_abba(item):
            tls = True
            break
    if not tls:
        return tls
    for item in ins:
        if has_abba(item):
            return False
    return True

if __name__ == "__main__":
    main()