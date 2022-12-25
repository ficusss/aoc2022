import sys
from copy import deepcopy


def main():
    input_filepath = sys.argv[1]
    with open(input_filepath, 'r') as fp:
        input_data = fp.readlines()

    base_map = [
        [int(x) for x in line.strip()]
        for line in input_data
    ]

    # part1
    bool_map = get_bool_map_first_task(base_map)
    count_true = sum([sum(row) for row in bool_map])
    print(count_true)

    # part2
    see_map = get_see_map_second_task(base_map)
    max_of_max = max([max(l) for l in see_map])
    print(max_of_max)


def get_bool_map_first_task(base_map: list[list[int]]) -> list[list[bool]]:
    if len(base_map) == 0:
        return [[]]

    bool_max_map = [
        [[True, v] for v in bm]
        for bm in base_map
    ]
    for i in range(1, len(bool_max_map)-1):
        for j in range(1, len(bool_max_map[i])-1):
            bool_max_map[i][j][0] = False

    # проход слева направо
    for i in range(1, len(bool_max_map)-1):
        for j in range(1, len(bool_max_map[i])-1):
            if base_map[i][j] > bool_max_map[i][j-1][1]:
                bool_max_map[i][j] = [True, base_map[i][j]]
            else:
                bool_max_map[i][j][1] = bool_max_map[i][j-1][1]

    # проход справа налево
    for i in range(len(bool_max_map)-2, 0, -1):
        for j in range(len(bool_max_map[i])-2, 0, -1):
            if base_map[i][j] > bool_max_map[i][j+1][1]:
                bool_max_map[i][j] = [True, base_map[i][j]]
            else:
                bool_max_map[i][j][1] = bool_max_map[i][j+1][1]
    
    # проход сверху вниз
    for i in range(1, len(bool_max_map)-1):
        for j in range(1, len(bool_max_map[i])-1):
            if base_map[i][j] > bool_max_map[i-1][j][1]:
                bool_max_map[i][j] = [True, base_map[i][j]]
            else:
                bool_max_map[i][j][1] = bool_max_map[i-1][j][1]

    # проход снизу вверх
    for i in range(len(bool_max_map)-2, 0, -1):
        for j in range(len(bool_max_map[i])-2, 0, -1):
            if base_map[i][j] > bool_max_map[i+1][j][1]:
                bool_max_map[i][j] = [True, base_map[i][j]]
            else:
                bool_max_map[i][j][1] = bool_max_map[i+1][j][1]

    bool_map = []
    for i in range(len(bool_max_map)):
        bool_map.append([])
        for j in range(len(bool_max_map[i])):
            bool_map[i].append(bool_max_map[i][j][0])
    
    return bool_map


def get_see_map_second_task(base_map: list[list[int]]) -> list[list[int]]:
    if len(base_map) == 0:
        return [[]]

    base_bool_map = [  # [count_see_trees, max_size_tree]
        [[0, v] for v in bm]
        for bm in base_map
    ]
    from_left_map = deepcopy(base_bool_map)
    from_right_map = deepcopy(base_bool_map)
    from_top_map = deepcopy(base_bool_map)
    from_down_map = deepcopy(base_bool_map)


    # проход слева направо
    for i in range(0, len(from_left_map)):
        for j in range(1, len(from_left_map[i])):

            if base_map[i][j] <= base_map[i][j-1]:
                from_left_map[i][j] = [1, from_left_map[i][j-1][1]]
            else:
                counter = 0
                for k in range(j-1, -1, -1):
                    if base_map[i][j] > base_map[i][k]:
                        counter+=1
                        continue
                    counter+=1
                    break
                from_left_map[i][j] = [counter, base_map[i][j]]

    # проход справа налево
    for i in range(0, len(from_right_map)):
        for j in range(len(from_right_map[i])-2, -1, -1):

            if base_map[i][j] <= base_map[i][j+1]:
                from_right_map[i][j] = [1, from_right_map[i][j+1][1]]
            else:
                counter = 0
                for k in range(j+1, len(from_right_map[i])):
                    if base_map[i][j] > base_map[i][k]:
                        counter+=1
                        continue
                    counter+=1
                    break
                from_right_map[i][j] = [counter, base_map[i][j]]

    # проход сверху вниз
    for i in range(1, len(from_top_map)):
        for j in range(0, len(from_top_map[i])):

            if base_map[i][j] <= base_map[i-1][j]:
                from_top_map[i][j] = [1, from_top_map[i-1][j][1]]
            else:
                counter = 0
                for k in range(i-1, -1, -1):
                    if base_map[i][j] > base_map[k][j]:
                        counter+=1
                        continue
                    counter+=1
                    break
                from_top_map[i][j] = [counter, base_map[i][j]]

    # проход снизу вверх
    for i in range(len(from_down_map)-2, -1, -1):
        for j in range(0, len(from_down_map[i])):

            if base_map[i][j] <= base_map[i+1][j]:
                from_down_map[i][j] = [1, from_down_map[i+1][j][1]]
            else:
                counter = 0
                for k in range(i+1, len(from_down_map)):
                    if base_map[i][j] > base_map[k][j]:
                        counter+=1
                        continue
                    counter+=1
                    break
                from_down_map[i][j] = [counter, base_map[i][j]]

    result_map = []
    for i in range(len(base_map)):
        result_map.append([])
        for j in range(len(base_map[i])):
            result_map[i].append(
                from_left_map[i][j][0]
                * from_right_map[i][j][0]
                * from_top_map[i][j][0]
                * from_down_map[i][j][0]
            )
    
    return result_map


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
