def main():
    file = open("input.txt")
    input = file.read().split(", ")
    file.close()
    
    #TEST DATA
    #input = "R8, R4, R4, R8".split(", ")
    
    dir_degrees = 90
    x, y = (0, 0)
    twice_x, twice_y = (0, 0)
    visited = []
    found = False
    
    for step in input:
        dir = step[0]
        distance = int(step[1:])
        new_visits = []
        
        if dir == "R":
            dir_degrees -= 90
        elif dir == "L":
            dir_degrees += 90
        dir_degrees = dir_degrees % 360
        
        old_x, old_y = x, y
        if dir_degrees == 0:
            old_x = x
            x += distance
            for i in range(old_x, x+1):
                new_visits.append((i, y))
        elif dir_degrees == 90:
            old_y = y
            y += distance
            for i in range(old_y, y+1):
                new_visits.append((x, i))
        elif dir_degrees == 180:
            old_x = x
            x -= distance
            for i in range(x, old_x+1):
                new_visits.append((i, y))
        elif dir_degrees == 270:
            old_y = y
            y -= distance
            for i in range(y, old_y+1):
                new_visits.append((x, i))
        new_visits.remove((old_x, old_y))
        
        if not found:
            for (new_x, new_y) in new_visits:
                if (new_x, new_y) in visited:
                    found = True
                    twice_x, twice_y = new_x, new_y
                    visited.sort()
                    break
                else:
                    visited.append((new_x, new_y))
    
    print("Final position: {}".format((x, y)))
    print("Distance from start: {}".format(abs(x)+abs(y)))
    print("First visited twice: {}".format((twice_x, twice_y)))
    print("Distance from start: {}".format(abs(twice_x)+abs(twice_y)))
    
if __name__ == "__main__":
    main()