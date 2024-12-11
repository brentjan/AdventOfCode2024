stones = dict()


def blink_rule(current_blinks, amount_blinks, next_stone):
    dynamic_value = stones.setdefault(next_stone, dict()).setdefault(current_blinks + 1, 0)
    if dynamic_value > 0:
        return dynamic_value
    else:
        dynamic_value = blink(next_stone, current_blinks + 1, amount_blinks)
        stones[next_stone][current_blinks + 1] = dynamic_value
        return dynamic_value


def blink(stone, current_blinks, amount_blinks):
    if current_blinks == amount_blinks:
        return 1
    else:
        stone_value = int(stone)
        stone_count = 0

        if stone_value == 0:
            stone_count += blink_rule(current_blinks, amount_blinks, '1')
        elif len(stone) % 2 == 0:
            stone_count += blink_rule(current_blinks, amount_blinks, str(int(stone[:len(stone) // 2])))
            stone_count += blink_rule(current_blinks, amount_blinks, str(int(stone[len(stone) // 2:])))
        else:
            stone_count += blink_rule(current_blinks, amount_blinks, str(stone_value * 2024))

        return stone_count
    

if __name__ == '__main__':
    stone_count = 0

    for stone in open("data/advent11.in").read().rstrip('\n').split(' '):
        stone_count += blink(stone, 0, 75)

    print(stone_count   )
