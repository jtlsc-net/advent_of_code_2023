from functools import reduce


def part_one(input: str) -> int:
    with open(input, "r") as file:
        read_data = file.readlines()

    times = [
        int(x.strip()) for x in read_data[0].split(" ") if len(x) > 0 and x[0].isdigit()
    ]
    distances = [
        int(x.strip()) for x in read_data[1].split(" ") if len(x) > 0 and x[0].isdigit()
    ]
    ways = [0 for x in range(0, len(times))]
    for idx, time in enumerate(times):
        for val in range(0, time):
            if (time - val) * val > distances[idx]:
                ways[idx] += 1
    return reduce(lambda x, y: x * y, ways)


def part_two(input: str) -> int:
    with open(input, "r") as file:
        read_data = file.readlines()

    times = int(
        "".join(
            [
                x.strip()
                for x in read_data[0].split(" ")
                if len(x) > 0 and x[0].isdigit()
            ]
        )
    )
    distances = int(
        "".join(
            [
                x.strip()
                for x in read_data[1].split(" ")
                if len(x) > 0 and x[0].isdigit()
            ]
        )
    )
    ways = 0
    for val in range(0, times):
        if (times - val) * val > distances:
            ways += 1
    return ways


if __name__ == "__main__":
    # print(part_one("test.txt"))
    # print(part_one("6input.txt"))
    # print(part_two("test.txt"))
    print(part_two("6input.txt"))
