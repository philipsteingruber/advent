import re
from collections import OrderedDict, defaultdict
import sys


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

            new_tower = Tower(weight=int(weight), parent=None, children=children)
        else:
            new_tower = Tower(weight=int(weight))

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
            top_tower = name
            break

    print('Step 1 solution:', top_tower)
    is_balanced(top_tower, towers)




def is_balanced(tower_name, towers_dict):
    tower_children = towers_dict[tower_name].children

    if not tower_children:
        return True
    else:
        for child in tower_children:
            child_balanced = is_balanced(child, towers_dict)
            if not child_balanced:
                return child_balanced
        tower_weights = {}
        for name in tower_children:
            tower_weights[name] = tower_weight(name, towers_dict)
        if len(set(tower_weights.values())) <= 1:
            return True
        else:
            tower_needing_change, operation = tower_to_balance(tower_weights)
            amount_to_rebalance = abs(max(tower_weights.values())-min(tower_weights.values()))
            current_weight = towers_dict[tower_needing_change].weight

            if operation == '+':
                new_weight = current_weight + amount_to_rebalance
            else:
                new_weight = current_weight - amount_to_rebalance

            print('To rebalance the tower, change weight of {} to {}'.format(tower_needing_change, new_weight))
            return False

def tower_weight(tower_name, towers_dict):
    tower = towers_dict[tower_name]

    sum = tower.weight

    if tower.children:
        for child in tower.children:
            sum += tower_weight(child, towers_dict)
        return sum
    else:
        return sum

def tower_to_balance(tower_weights):
    print(tower_weights)
    reverse_dict = defaultdict(list)
    for tower, weight in tower_weights.items():
        reverse_dict[weight].append(tower)
    min_len = sys.maxsize
    least_common = None
    for weight, towers in reverse_dict.items():
        if len(towers) < min_len:
            least_common = towers[0]
            min_len = len(towers)
    if tower_weights[least_common] < average(tower_weights.values()):
        return (least_common, '+')
    else:
        return (least_common, '-')
    return least_common[0]


def average(numbers):
    return sum(numbers)/len(numbers)

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
