def main():
    screen_height = 6
    screen_width = 50

    screen = []
    for i in range(screen_height):
        row = []
        for j in range(screen_width):
            row.insert(j, False)
        screen.insert(i, row)

    # with open("testinput.txt") as file:
    with open("input.txt") as file:
        input = file.read().split("\n")

    for command in input:
        command = command.split()
        print(command)
        if command[0] == "rect":
            width, height = map(int, command[1].split("x"))
            rect(width, height, screen)
        elif command[0] == "rotate":
            # rotate column x=1 by 1
            if command[1] == "column":
                column = int(command[2].split("=")[1])
                distance = int(command[4])
                rotate_col(column, distance, screen)
            # rotate row y=0 by 4
            elif command[1] == "row":
                row = int(command[2].split("=")[1])
                distance = int(command[4])
                rotate_row(row, distance, screen)

    print("\n\n\n\n=======================================")
    show_screen(screen)
    print("A total of {} pixels are lit.".format(count_lit(screen)))

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n=======================================")
    show_letters(screen)

def show_letters(screen):
    height = len(screen)
    width = len(screen[0])
    for y in range(height):
        for x in range(width):
            if x == width - 1:
                if screen[y][x]:
                    print("#")
                else:
                    print(".")
            elif (x + 1) % 5 == 0:
                if screen[y][x]:
                    print("#", end="\t")
                else:
                    print(".", end="\t")
            else:
                if screen[y][x]:
                    print("#", end="")
                else:
                    print(".", end="")


def show_screen(screen):
    height = len(screen)
    width = len(screen[0])
    for y in range(height):
        for x in range(width):
            if x == width - 1:
                if screen[y][x]:
                    print("#")
                else:
                    print(".")
            else:
                if screen[y][x]:
                    print("#", end="")
                else:
                    print(".", end="")
    print("\n")

def count_lit(screen):
    count = 0
    for row in screen:
        for pixel in row:
            if pixel:
                count += 1
    return count

def rect(width, height, screen):
    #print("Lighting {}x{} rectangle in top-left corner.".format(width, height))
    for i in range(height):
        for j in range(width):
            screen[i][j] = True

def rotate_col(col, distance, screen):
    #print("Rotating column {} by {} row(s).".format(col, distance))
    screen_height = len(screen)
    current_lights = []
    for i in range(screen_height):
        current_lights.append(screen[i][col])
    for row in range(screen_height):
        """
        print("Row: {}".format(row))
        print("Distance: {}".format(distance))
        print("Height: {}".format(screen_height))
        print("Row - distance: {}".format(row-distance))
        print("Row - distance % height: {}".format((row-distance)%screen_height))
        print("Lit at r - d % h? {}".format(current_lights[(row - distance) % screen_height]))
        """
        screen[row][col] = current_lights[(row - distance) % screen_height]

def rotate_row(row, distance, screen):
    #print("Rotating row {} by {} column(s).".format(row, distance))
    screen_width = len(screen[0])
    current_lights = []
    for i in range(screen_width):
        current_lights.append(screen[row][i])
    for col in range(screen_width):
        screen[row][col] = current_lights[(col - distance) % screen_width]


if __name__ == "__main__":
    main()