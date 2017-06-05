import re

def _step1(s):
        res = 0
        while "(" in s:
            res += s.find("(")
            s = s[s.find("("):]
            num_to_repeat, reps = s[1:s.find(")")].split("x")
            s = s[s.find(")")+1:]
            res += len(s[:int(num_to_repeat)] * int(reps))
            s = s[int(num_to_repeat):]
        res += len(s)
        return res
        
def decompress(s, step2=False):
    marker = re.search(r"\((\d+)x(\d+)\)", s)
    if not marker:
        return len(s)
    pre_marker = marker.start(0)
    len_to_repeat = int(marker.group(1))
    reps = int(marker.group(2))
    i = pre_marker + len(marker.group())
    if not step2:
        return len(s[:pre_marker]) + len(s[i:i+len_to_repeat]) * reps + decompress(s[i+len_to_repeat:], False)
    else:
        return len(s[:pre_marker]) + decompress(s[i:i+len_to_repeat], True) * reps + decompress(s[i+len_to_repeat:], True)

    

if __name__ == "__main__":
    with open("input.txt") as file:
        inputdata = file.read().strip()
    print("Non-recursive length is {}.".format(decompress(inputdata)))
    print("Recursive length is {}.".format(decompress(inputdata, True)))
