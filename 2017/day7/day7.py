import re
from collections import OrderedDict


def main():
    with open('input.txt') as file:
        input = file.readlines()

    pattern = re.compile(r'(\w+) \((\d+)\)( -> )?([\w, ]*)')

    towers = OrderedDict()
    towers_found = []
    for line in input:
        name, weight, _, children = re.match(pattern, line).groups()
        towers_found.append(name)

        if children:
            children = children.split(', ')

            new_tower = Tower(weight=weight, parent=None, children=children)
        else:
            new_tower = Tower(weight=weight)

        # Loop through existing towers. If any of them has the new
        # tower as a child, set the found tower as the new tower's parent.
        for tower_name, tower in towers.items():
            if tower.children:
                if name in tower.children:
                    new_tower.parent = tower_name
                    break

        towers[name] = new_tower

    for name, tower in towers.items():
        if tower.children:
            for child in tower.children:
                towers[child].parent = name

    for name, tower in towers.items():
        if not tower.parent:
            print('Step 1 solution:', name)
            break


class Tower:
    def __init__(self, weight, parent=None, children=None):
        self.weight = weight
        self.parent = parent
        self.children = children


if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print('Runtime:', time.time()-start_time, 'seconds.')
