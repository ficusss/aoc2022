import sys


TInputLine = list[tuple[tuple[int, int], tuple[int, int]]]


def main():
    input_filepath = sys.argv[1]
    with open(input_filepath, 'r') as fp:
        input_data = [
            line.strip().split(",") 
            for line in fp.readlines()
        ]

    data: TInputLine = [
        (
            tuple([int(x) for x in first_sections.split("-")]),
            tuple([int(x) for x in second_sections.split("-")])
        )
        for first_sections, second_sections in input_data
    ]

    #part1
    ifc = is_fully_contains(data)
    print("Fully contains in %s pairs" % sum(ifc))

    #part1
    ic = is_contains(data)
    print("Contains in %s pairs" % sum(ic))


def is_fully_contains(data: TInputLine) -> list[bool]:
    result = []
    for first_sections, second_sections in data:
        first_diff = first_sections[0] - second_sections[0]
        second_diff = first_sections[1] - second_sections[1]
        if first_diff == 0 \
            or second_diff == 0 \
            or first_diff / abs(first_diff) != second_diff / abs(second_diff):
            result.append(True)
        else:
            result.append(False)
    return result


def is_contains(data: TInputLine) -> list[bool]:
    result = []
    for first_sections, second_sections in data:
        first_diff = first_sections[1] - second_sections[0]
        second_diff = second_sections[1] - first_sections[0]
        if first_diff < 0 or second_diff < 0:
            result.append(False)
        else:
            result.append(True)
    return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
