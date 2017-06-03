import hashlib


def step1():

    door_id = "reyedfim"

    i = 0
    password = []

    while len(password) < 8:
        m = hashlib.md5((door_id + str(i)).encode('utf-8')).hexdigest()
        if m.startswith("00000"):
            password.append(m[5])
        i += 1

    password = "".join(password)
    print("Password: {}".format(password))


def step2():
    door_id = "reyedfim"
    password = [None] * 8

    i = 0
    while None in password:
        test = (door_id + str(i)).encode("utf-8")
        m = hashlib.md5(test).hexdigest()

        if m.startswith("00000"):
            pos = int(m[5], 16)
            value = m[6]
            if pos in range(8) and password[pos] == None:
                password[pos] = value
        i += 1

    password = "".join(password)
    print("Password: {}".format(password))

if __name__ == "__main__":
    step1()
    step2()
