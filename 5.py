from multiprocessing import Pool

key_order = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def parse_seeds(seeds_line: str) -> list:
    return [int(x) for x in seeds_line.split(" ") if x[0] != "s"]


def parse_to_dict(data: list) -> dict:
    output_dict = {}
    curr_key = ""
    for line in data:
        if line == "":
            continue
        d = line.split(" ")
        if d[-1] == "map:":
            curr_key = d[0]
            output_dict[curr_key] = []
        elif d[0].isdigit() and curr_key != "":
            output_dict[curr_key].append([int(x) for x in d])
    return output_dict


def seeds_to_locations(seeds: list, formulae: dict) -> list:
    output_list = []
    for seed in seeds:
        for key in key_order:
            for mapping in formulae[key]:
                if seed in range(mapping[1], mapping[1] + mapping[2]):
                    # print(
                    #    "mapping",
                    # seed,
                    # "to",
                    # mapping[0] + (seed - mapping[1]),
                    # "for",
                    # key,
                    # )
                    seed = mapping[0] + (seed - mapping[1])
                    break
        output_list.append(seed)
    return output_list


def parse_seeds_two(seeds_line: str) -> list:
    seeds_raw = [int(x) for x in seeds_line.split(" ") if x[0] != "s"]
    output_seeds = []
    for idx in range(0, len(seeds_raw), 2):
        output_seeds.append((seeds_raw[idx], seeds_raw[idx + 1]))
    return output_seeds


def seeds_to_locations_two(seeds: list, formulae: dict) -> int:
    minimum = 100000000000
    for tup in seeds:
        for seed in range(tup[0], tup[0] + tup[1]):
            for key in key_order:
                for mapping in formulae[key]:
                    if seed in range(mapping[1], mapping[1] + mapping[2]):
                        # print(
                        #    "mapping",
                        # seed,
                        # "to",
                        # mapping[0] + (seed - mapping[1]),
                        # "for",
                        # key,
                        # )
                        seed = mapping[0] + (seed - mapping[1])
                        break
            minimum = min(minimum, seed)
    return minimum


def seeds_to_locations_three(seeds: tuple) -> int:
    minimum = 100000000000
    for seed in range(seeds[0], seeds[0] + seeds[1]):
        for key in key_order:
            for mapping in global_formula_dict[key]:
                if seed in range(mapping[1], mapping[1] + mapping[2]):
                    # print(
                    #    "mapping",
                    # seed,
                    # "to",
                    # mapping[0] + (seed - mapping[1]),
                    # "for",
                    # key,
                    # )
                    seed = mapping[0] + (seed - mapping[1])
                    break
        minimum = min(minimum, seed)
    return minimum


def part_one(input_file: str) -> int:
    with open(input_file, "r") as f:
        read_data = f.readlines()
    read_data = [x.strip() for x in read_data if x.strip() != ""]
    seeds = read_data[0]
    seeds = parse_seeds(seeds)
    formula_dict = parse_to_dict(read_data)
    return min(seeds_to_locations(seeds, formula_dict))


def part_two(input_file: str):
    with open(input_file, "r") as f:
        read_data = f.readlines()
    read_data = [x.strip() for x in read_data if x.strip() != ""]
    seeds = read_data[0]
    seeds = parse_seeds_two(seeds)
    global global_formula_dict
    global_formula_dict = parse_to_dict(read_data)
    with Pool(10) as p:
        return min(p.map(seeds_to_locations_three, seeds))


if __name__ == "__main__":
    # print(part_one("5input.txt"))
    # print(part_one("test.txt"))
    # print(part_two("test.txt"))
    print(part_two("5input.txt"))
