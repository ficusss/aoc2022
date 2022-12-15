from copy import deepcopy
import sys


TInputLine = list[tuple[tuple[int, int], tuple[int, int]]]


def main():
    input_filepath = sys.argv[1]
    with open(input_filepath, 'r') as fp:
        input_data = fp.readlines()
        

    stacks, manipulations = parse_input_data(input_data)

    #part1
    manipulated_stack = execute_manipulation(stacks, manipulations)
    print(
        "Boxes on the top (single manipulations): %s" % 
        "".join([stack[-1] for stack in manipulated_stack])
    )

    #part2
    manipulated_stack = execute_manipulation(
        stacks,
        manipulations,
        single_manipulation=False
    )
    print(
        "Boxes on the top (multiply manipulations): %s" % 
        "".join([stack[-1] for stack in manipulated_stack])
    )


def parse_input_data(data: list[str]) -> tuple[list[list[str]], list[tuple[int, int, int]]]:
    input_stack_data = []
    index_manipulation_start = 0
    for index_manipulation_start, line in enumerate(data):
        if line.strip() == "":
            index_manipulation_start += 1
            break
        input_stack_data.append(line)

    stack_count = int(input_stack_data[-1].strip().split()[-1])
    input_stack = [[] for _ in range(stack_count)]
    for line in input_stack_data[-2::-1]:
        for index_stack, value in enumerate(line[1::4]):
            if value != " ":
               input_stack[index_stack].append(value)
        
    input_manipulations = []
    for line in data[index_manipulation_start:]:
        input_manipulation = tuple(
            int(value) 
            for value in line.split(" ")[1::2]
        )
        input_manipulations.append(input_manipulation)

    return input_stack, input_manipulations


def execute_manipulation(
    stacks:list[list[str]],
    manipulations: list[tuple[int, int, int]],
    single_manipulation: bool = True
) -> list[list[str]]:
    result_stacks = deepcopy(stacks)
    for manipulation in manipulations:
        count = manipulation[0]
        stack_from = manipulation[1] - 1
        stack_to = manipulation[2] - 1
        if single_manipulation:
            for _ in range(count):
                result_stacks[stack_to].append(
                    result_stacks[stack_from].pop()
                )
        else:
            result_stacks[stack_to].extend(
                [
                    result_stacks[stack_from].pop()
                    for _ in range(count)
                ][::-1]
            )
    return result_stacks


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
