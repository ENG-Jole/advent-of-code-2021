import requests
import os
import copy
from statistics import mode, multimode


TEST_INPUT = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]
SESSION_ID = os.environ["AOC_2021_SESSION"]
URL = "https://adventofcode.com/2021/day/3/input"


def get_input_data(url: str) -> list[str]:
    return [
        item
        for item in requests.get(url, cookies={"session": SESSION_ID}).text.split("\n")
        if item != ""
    ]


def anti_bin_mode(l: list[int]) -> int:
    return 1 if max(multimode(l)) == 0 else 0


def break_input_into_list_of_lists(raw_input: list[str]) -> list[list[int]]:
    byte_list = []

    for elem in raw_input[0]:
        byte_list.append([])

    for data in raw_input:
        for index, elem in enumerate(data):
            byte_list[index].append(int(elem))

    return byte_list


def get_most_common_and_least(byte_list: list[list[int]]) -> tuple[int, int]:
    most_common = []
    least_common = []

    for elem in byte_list:
        most_common.append(mode(elem))

    for elem in byte_list:
        least_common.append(anti_bin_mode(elem))

    return int("".join([str(el) for el in most_common]), 2), int(
        "".join([str(el) for el in least_common]), 2
    )


def get_most_and_least_oneliner(raw_input: list[str]) -> tuple[int, int]:
    most_common = int(
        "".join(
            [
                str(max(multimode(elem[key] for elem in raw_input)))
                for key in range(len(raw_input[0]))
            ]
        ),
        2,
    )

    least_common = int("".join([str(anti_bin_mode([int(elem[key]) for elem in raw_input])) for key in range(len(raw_input[0]))]),2,)

    return most_common, least_common


def get_val_by_bit_criteria(raw_input: list[str]) -> tuple[int, int]:
    mc_working_copy = raw_input.copy()
    lc_working_copy = raw_input.copy()

    mc_index = 0
    while len(mc_working_copy) > 1:
        criteria = max(multimode([int(elem[mc_index]) for elem in mc_working_copy]))
        for elem in mc_working_copy.copy():
            if int(elem[mc_index]) != criteria:
                mc_working_copy.remove(elem)
        mc_index += 1

    lc_index = 0
    while len(lc_working_copy) > 1:
        criteria = anti_bin_mode([int(elem[lc_index]) for elem in lc_working_copy])
        for elem in lc_working_copy.copy():
            if int(elem[lc_index]) != criteria:
                lc_working_copy.remove(elem)
        lc_index += 1

    return int("".join(mc_working_copy), 2), int("".join(lc_working_copy), 2)


if __name__ == "__main__":
    input = get_input_data(URL)
    list_of_byte_vals = break_input_into_list_of_lists(input)
    most_common_1, least_common_1 = get_most_common_and_least(list_of_byte_vals)
    print(f"Part 1 Answer: {most_common_1 * least_common_1}")
    most_common_2, least_common_2 = get_val_by_bit_criteria(input)
    print(f"Part 2 Answer: {most_common_2 * least_common_2}")
    mc_oneline, lc_oneline = get_most_and_least_oneliner(input)
    print(f"{most_common_1 == mc_oneline}, {least_common_1 == lc_oneline}")
