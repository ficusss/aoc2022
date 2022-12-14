import sys
import string


def main():
    input_filepath = sys.argv[1]
    with open(input_filepath, 'r') as fp:
        input_data = [line.strip() for line in fp.readlines()]
    
    
    #part1
    data = parse_input_data_for_first_task(input_data)
    intersections = get_intersections_elements(data)
    print("Sum of compartments intersections prioritets is %s" % sum(intersections))
    
    #part2
    data = parse_input_data_for_second_task(input_data)
    intersections = get_intersections_elements(data)
    print("Sum of group intersections prioritets is %s" % sum(intersections))



def parse_input_data_for_first_task(
    data: list[str]
) -> list[list[list[int]]]:

    lettres_priority_map = {
         l: i+1 for i, l in enumerate(string.ascii_letters)
    }

    splited_data = []
    for line in data:
        line = [lettres_priority_map[symbol] for symbol in line]
        median_index = int(len(line)/2)
        splited_data.append([line[:median_index], line[median_index:]])

    return splited_data


def parse_input_data_for_second_task(
    data: list[str]
) -> list[list[list[int]]]:

    lettres_priority_map = {
         l: i+1 for i, l in enumerate(string.ascii_letters)
    }

    splited_data = []
    for indx in range(0, len(data), 3):
        splited_data.append([
            [lettres_priority_map[symbol] for symbol in data[indx]],
            [lettres_priority_map[symbol] for symbol in data[indx+1]],
            [lettres_priority_map[symbol] for symbol in data[indx+2]]
        ])

    return splited_data


def get_intersections_elements(
    data: list[list[list[int]]]
) -> list[int]:
    intersections = []
    for group in data:
        group_intersections = set(group[0])
        for items in group[1:]:
            group_intersections = group_intersections.intersection(set(items))
        intersections.append(list(group_intersections)[0])

    return intersections


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
