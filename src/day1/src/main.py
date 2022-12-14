import sys
from collections import defaultdict


def main():
    input_filepath = sys.argv[1]
    with open(input_filepath, 'r') as fp:
        input_data = fp.readlines()

    elf_baggage = parse_input_data(input_data)
    elf_sum_calories = [(k, sum(v)) for k, v in elf_baggage.items()]
    sorted_elf_sum_calories = sorted(
        elf_sum_calories, 
        key=lambda x: x[1], 
        reverse=True
    )
    # part1
    print(f"Elf carrying the most Calories is {sorted_elf_sum_calories[0]}")

    # part2
    sum_calories_of_top_three_elf = sum(
        [v for k, v in sorted_elf_sum_calories[:3]]
    )
    print(f"Total of the top three Elves " \
          f"carrying the most Calories is {sum_calories_of_top_three_elf}")


def parse_input_data(data: list[str]) -> dict[int, list[int]]:
    result = defaultdict(list)
    key = 1
    for line in data:
        line = line.strip()
        if line == "":
            key += 1
            continue
        result[key].append(int(line))
    return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
