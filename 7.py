def order_hands(input: list) -> list:
    


def part_one(input: str) -> int:
    with open(input, "r") as f:
        read_data = f.readlines()

    hands = [x.split(" ")[0].strip() for x in read_data]
    bids = [int(x.split(" ")[1].strip()) for x in read_data]
    hands = order_hands(hands)
    return 0


if __name__ == "__main__":
    print(part_one("test.txt"))
