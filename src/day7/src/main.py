from pprint import pprint
from typing import TypedDict
import sys


class File(TypedDict):
    name: str
    size: int


class Directory(TypedDict):
    name: str
    size: int
    directories: list["Directory"]
    files: list[File]


class FileSystem:
    def __init__(self):
        root: Directory | None = None

    def parse_bash_logs(self, bash_log: list[str]):
        self.root, _ = self._parse_bash_logs(
            dir_name="/",
            bash_log=bash_log[1:]
        )

    def _parse_bash_logs(self, dir_name: str, bash_log: list[str]) -> tuple[Directory, int]:

        dirs: list[Directory] = []
        files: list[File] = []

        line_index = 0
        while line_index < len(bash_log):
            
            if bash_log[line_index].strip() == "$ cd ..":
                break
            
            if bash_log[line_index].startswith("$ cd"):
                args = bash_log[line_index].split(" ")
                dir, sub_line_index = self._parse_bash_logs(
                    dir_name=args[-1].strip(), 
                    bash_log=bash_log[line_index+1:]
                )
                dirs.append(dir)
                # while line_index < len(bash_log) \
                #     and not bash_log[line_index].strip() == "$ cd ..":
                #     line_index += 1
                line_index += sub_line_index + 2
                continue

            if bash_log[line_index].startswith("$ ls"):
                line_index += 1
                while line_index < len(bash_log) \
                    and not bash_log[line_index].startswith("$"):
                    
                    args = bash_log[line_index].split(" ")
                    if args[0] != "dir":
                        files.append(
                            File(
                                name=args[1].strip(),
                                size=int(args[0])
                            )
                        )
                    line_index += 1
        
        size = \
            sum([file["size"] for file in files]) \
            + sum([dir["size"] for dir in dirs])
        current_dir = Directory(
            name=dir_name,
            size=size,
            directories=dirs,
            files=files
        )
        return current_dir, line_index




def main():
    input_filepath = sys.argv[1]
    with open(input_filepath, 'r') as fp:
        input_data = fp.readlines()

    fs = FileSystem()
    fs.parse_bash_logs(input_data)

    # pprint(fs.root)

    # part1
    all_dirs = []
    process_dirs = [fs.root]
    while len(process_dirs) > 0:
        dir = process_dirs.pop()
        all_dirs.append(dir)
        process_dirs.extend(dir["directories"])


    dirs_sizes_with_size_less_then_100k = [
        dir["size"]
        for dir in all_dirs
        if dir["size"] <= 100000
    ]
    print(sum(dirs_sizes_with_size_less_then_100k))


    # part2
    total_memory = 70000000
    need_free_memory = 30000000
    current_free_memory = total_memory - fs.root["size"]

    all_dirs = []
    process_dirs = [fs.root]
    while len(process_dirs) > 0:
        dir = process_dirs.pop()
        all_dirs.append(dir)
        process_dirs.extend(dir["directories"])
    all_dirs = sorted(all_dirs, key=lambda x: x["size"])
    
    for dir in all_dirs:
        if dir["size"] >= need_free_memory - current_free_memory:
            print(dir["size"])
            break


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
