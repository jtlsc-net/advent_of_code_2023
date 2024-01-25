def part_1(input: str):
    with open(input, 'r') as f:
        read_data = f.readlines()

    sum = 0
    for line in read_data:
        temp_score = 0
        temp = line.split(':')[1]
        win_num, my_num = temp.split('|')
        win_num = {x for x in win_num.strip().split(' ') if x != ''}
        my_num = [x for x in my_num.strip().split(' ') if x != '']
        for num in my_num:
            if num in win_num:
                if temp_score == 0:
                    temp_score = 1
                else:
                    temp_score = temp_score * 2
        sum += temp_score
    return sum

def part_2(input: str):
    with open(input, 'r') as f:
        read_data = f.readlines()
    
    cards = [1] * len(read_data)
    for idx, line in enumerate(read_data):
        temp_score = 0
        temp = line.split(':')[1]
        win_num, my_num = temp.split('|')
        win_num = {x for x in win_num.strip().split(' ') if x != ''}
        my_num = [x for x in my_num.strip().split(' ') if x != '']
        for num in my_num:
            if num in win_num:
                temp_score += 1
        for card_idx in range(1,temp_score + 1): # 1 because we don't add to our current index
            if (idx + card_idx < len(cards)):

                cards[idx + card_idx] += 1 * cards[idx]
    return sum(cards)



#print(part_1('4input.txt'))
#print(part_2('test.txt'))
print(part_2('4input.txt'))
