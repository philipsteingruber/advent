def step1():
    file = open("input.txt")
    input = file.readlines()
    file.close()
    
    count = 0
    
    for line in input:
        sides = list(map(int, line.strip().split()))
        sides.sort()
        
        if sides[0] + sides[1] > sides[2]:
            count += 1
        
    print("Valid triangles: {}".format(count))
        
def step2():
    file = open("input.txt")
    input = file.read().split("\n")
    file.close()
    
    count = 0
           
    for i in range(0, len(input), 3):
        l1 = list(map(int, input[i].strip().split()))
        l2 = list(map(int, input[i+1].strip().split()))
        l3 = list(map(int, input[i+2].strip().split()))
        for j in range(3):
            triangle = [l1[j], l2[j], l3[j]]
            triangle.sort()
            if triangle[0] + triangle[1] > triangle[2]:
                count += 1
                
    print("Valid triangles (column): {}".format(count))
        
if __name__ == "__main__":
    step1()
    step2()