from typing import final
import requests
import os

TEST_INPUT = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
SESSION_ID = os.environ["AOC_2021_SESSION"]
URL = "https://adventofcode.com/2021/day/2/input"


def get_input_data(url: str) -> list[str]:
   return [item for item in requests.get(url, cookies={"session": SESSION_ID}).text.split("\n")]


def get_horizontal_and_vertical_position(command_list: list[str]) -> list[int]:
    final_position = [0, 0]
    for command in command_list:
            if command.startswith("down"):
                final_position[1] += int(command[-1])
            elif command.startswith("up"):
                final_position[1] -= int(command[-1])
            elif command.startswith("forward"):
                final_position[0] += int(command[-1])

    return final_position


def get_hori_vert_and_aim(command_list: list[str]) -> list[int]:
    final_position = [0,0,0]
    for command in command_list:
        if command.startswith("down"):
            final_position[2] += int(command[-1])
        elif command.startswith("up"):
            final_position[2] -= int(command[-1])
        elif command.startswith("forward"):
            final_position[0] += int(command[-1])
            final_position[1] += (int(command[-1]) * final_position[2])

    return final_position        



if __name__ == '__main__':
    command_list = get_input_data(URL)
    result_1 = get_horizontal_and_vertical_position(command_list)
    print(f"Part 1 Answer: {result_1}, {result_1[0] * result_1[1]}")
    result_2 = get_hori_vert_and_aim(command_list)
    print(f"Part 2 Answer: {result_2}, {result_2[0] * result_2[1]}")    