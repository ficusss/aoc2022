import sys
from enum import Enum
from collections import defaultdict


class RockPaperScissorsGame():

    class Symbols(Enum):
        A = 1  # камень
        B = 2  # бумага
        C = 3  # ножницы
        X = 1  # камень
        Y = 2  # бумага
        Z = 3  # ножницы

    class Results(Enum):
        LOST = 0
        DRAW = 3
        WIN = 6
        X = 0
        Y = 3
        Z = 6

    first_player_symbol: Symbols
    second_player_symbol: Symbols
    first_player_game_result: Results
    second_player_game_result: Results
    first_player_total_score: int
    second_player_total_score: int

    def __init__(self):
        pass

    def set_players_symbol(
        self, 
        first_player_symbol: str, 
        second_player_symbol: str
    ) -> "RockPaperScissorsGame":

        self.first_player_symbol = self.Symbols[first_player_symbol]
        self.second_player_symbol = self.Symbols[second_player_symbol]
        self.first_player_game_result = self.first_player_result()
        self.second_player_game_result = self.second_player_result()
        self.first_player_total_score = (
            self.first_player_game_result.value
            + self.first_player_symbol.value
        )
        self.second_player_total_score = (
            self.second_player_game_result.value
            + self.second_player_symbol.value
        )

        return self
    
    def set_first_player_symbol_and_second_player_result(
        self, 
        first_player_symbol: str, 
        second_player_result: str
    ) -> "RockPaperScissorsGame":

        self.first_player_symbol = self.Symbols[first_player_symbol]
        self.second_player_game_result = self.Results[second_player_result]
        self.first_player_game_result = self.revert_result(
            self.second_player_game_result
        )
        self.second_player_symbol = self.find_second_player_symbol()
        self.first_player_total_score = (
            self.first_player_game_result.value
            + self.first_player_symbol.value
        )
        self.second_player_total_score = (
            self.second_player_game_result.value
            + self.second_player_symbol.value
        )
        
        return self

    def find_second_player_symbol(self) -> Symbols:
        match self.second_player_game_result:
            case self.Results.LOST:
                return self.Symbols(
                    (self.first_player_symbol.value + 2) 
                    if self.first_player_symbol.value == 1
                    else (self.first_player_symbol.value - 1)
                )
            case self.Results.DRAW:
                return self.first_player_symbol
            case self.Results.WIN:
                return self.Symbols(
                    (self.first_player_symbol.value - 2) 
                    if self.first_player_symbol.value == 3
                    else (self.first_player_symbol.value + 1)
                )
        raise ValueError(
            f"Unexpected value of self.second_player_game_result: " \
            f"{self.second_player_game_result}."
        )

    def first_player_result(self) -> Results:
        diff_value = (
            self.second_player_symbol.value - self.first_player_symbol.value
        )
        match diff_value:
            case 0:
                return self.Results.DRAW
            case 1 | -2:
                return self.Results.LOST
            case 2 | -1:
                return self.Results.WIN
        raise ValueError(
            f"Unexpected diff_value: {diff_value}. Must be 0, 1 or 2."
        )
    
    def second_player_result(self) -> Results:
        return self.revert_result(self.first_player_result())

    def revert_result(self, result):
        match result:
            case self.Results.WIN:
                return self.Results.LOST
            case self.Results.LOST:
                return self.Results.WIN
        return result


def main():
    input_filepath = sys.argv[1]
    with open(input_filepath, 'r') as fp:
        input_data = [
            line.strip().split(" ")
            for line in fp.readlines()
        ]

    # part1
    game_results = [
        RockPaperScissorsGame()
        .set_players_symbol(fp, sp)
        .second_player_total_score
        for fp, sp in input_data
    ]
    print("1 strategy: Total score second playes is %s" % sum(game_results))

    # part2
    game_results = [
        RockPaperScissorsGame()
        .set_first_player_symbol_and_second_player_result(fp, sr)
        .second_player_total_score
        for fp, sr in input_data
    ]
    print("2 strategy: Total score second playes is %s" % sum(game_results))



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
