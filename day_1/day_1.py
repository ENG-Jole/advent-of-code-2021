import requests
import os

TEST_INPUT = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
SESSION_ID = os.environ["AOC_2021_SESSION"]
URL = "https://adventofcode.com/2021/day/1/input"


def url_to_list_of_ints(url: str) -> list[int]:
    list_of_ints = [
        int(item)
        for item in requests.get(url, cookies={"session": SESSION_ID}).text.split()
    ]
    return list_of_ints


def get_num_of_larger_measurements(measurements: list[int]) -> int:
    larger_measurements = 0
    for index in range(len(measurements) - 1):
        if measurements[index + 1] - measurements[index] > 0:
            larger_measurements += 1

    return larger_measurements


def get_sliding_scale_num_of_larger_measurements(measurements: list[int]) -> int:
    sums = []
    for index in range(len(measurements) - 2):
        sums.append(
            measurements[index] + measurements[index + 1] + measurements[index + 2]
        )

    larger_measurements = get_num_of_larger_measurements(sums)
    return larger_measurements


if __name__ == "__main__":
    input = url_to_list_of_ints(URL)
    result_1 = get_num_of_larger_measurements(input)
    print(f"Part 1 Answer: {result_1}")
    result_2 = get_sliding_scale_num_of_larger_measurements(input)
    print(f"Part 2 Answer: {result_2}")
