def step1():
    file = open("testinput.txt")
    input = file.read().split()
    file.close()
    
    key_positions = {(0, 0) : "1",
                     (1, 0) : "2",
                     (2, 0) : "3",
                     (0, 1) : "4",
                     (1, 1) : "5",
                     (2, 1) : "6",
                     (0, 2) : "7",
                     (1, 2) : "8",
                     (2, 2) : "9"}
    
    key_presses = []
    
    for line in input:
        #start on 5 for the first line
        if len(key_presses) == 0:
            x, y = (1, 1)
        #remaining lines start where the last one ended
        else:
            x, y = key_presses[-1]
        
        for step in line:
            if step == "U" and y != 0:
                y -= 1
            elif step == "D" and y != 2:
                y += 1
            elif step == "L" and x != 0:
                x -= 1
            elif step == "R" and x != 2:
                x += 1
        
        key_presses.append((x, y))
        
    key_presses = [key_positions[x] for x in key_presses]
    print("Keycode is: {}".format("".join(key_presses)))
    
def step2():
    file = open("testinput.txt")
    input = file.read().split()
    file.close()
    
    key_positions = {(0, 0) : "EDGE",
                     (1, 0) : "EDGE",
                     (2, 0) : "1",
                     (3, 0) : "EDGE",
                     (4, 0) : "EDGE",
                     
                     (0, 1) : "EDGE",
                     (1, 1) : "2",
                     (2, 1) : "3",
                     (3, 1) : "4",
                     (4, 1) : "EDGE",
                     
                     (0, 2) : "5",
                     (1, 2) : "6",
                     (2, 2) : "7",
                     (3, 2) : "8",
                     (4, 2) : "9",
                     
                     (0, 3) : "EDGE",
                     (1, 3) : "A",
                     (2, 3) : "B",
                     (3, 3) : "C",
                     (4, 3) : "EDGE",
                     
                     (0, 4) : "EDGE",
                     (1, 4) : "EDGE",
                     (2, 4) : "D",
                     (3, 4) : "EDGE",
                     (4, 4) : "EDGE"}
    
    key_presses = []
    
    for line in input:
        #start at the 5 on the first line
        if len(key_presses) == 0:
            (x, y) = (0, 2)
        else:
            (x, y) = key_presses[-1]
            
        for step in line:
            if step == "U" and key_positions.get((x, y-1)) and key_positions.get((x, y-1)) != "EDGE":
                y -= 1
            elif step == "D" and key_positions.get((x, y+1)) and key_positions.get((x, y+1)) != "EDGE":
                y += 1
            elif step == "L" and key_positions.get((x-1, y)) and key_positions.get((x-1, y)) != "EDGE":
                x -= 1
            elif step == "R" and key_positions.get((x+1, y)) and key_positions.get((x+1, y)) != "EDGE":
                x += 1
                
        key_presses.append((x, y))
        
    key_presses = [key_positions[item] for item in key_presses]
    print("Keycode to toilet is: {}".format("".join(key_presses)))
    
if __name__ == "__main__":
    step1()
    step2()