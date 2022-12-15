import sys


def main():
    input_filepath = sys.argv[1]
    with open(input_filepath, 'r') as fp:
        input_data = fp.readlines()

    # part1
    marker_indexs = find_marker_end_index(input_data, marker_len=4)
    print(marker_indexs)

    # part2
    marker_indexs = find_marker_end_index(input_data, marker_len=14)
    print(marker_indexs)


def find_marker_end_index(data: list[str], marker_len: int) -> list[int]:
    result = []
    for line in data:
        index = 0
        for index in range(len(line) - marker_len):
            marker_set = set(line[index:index + marker_len])
            if len(marker_set) == marker_len:
                break
        result.append(index + marker_len)
    return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
