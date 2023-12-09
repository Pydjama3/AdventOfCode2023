from utils import LogManager


def get_input():
    with open('input') as file:
        raw = file.read().splitlines()
        possib = "23456789TJQKA"
        points = {possib[i]: i + 1 for i in range(len(possib))}
        return [line.split(' ') for line in raw], points


def func_part_i(_input, ref):
    rank = [{} for i in range(7)]
    for cards, bid in _input:
        card_counts = {}
        for card in cards:
            card_counts[card] = card_counts.get(card, 0) + 1
        if len(card_counts.keys()) == 1:
            rank[6][cards] = int(bid)
        elif len(card_counts.keys()) == 2:
            if max(card_counts.values()) == 4:
                rank[5][cards] = int(bid)
            else:
                rank[4][cards] = int(bid)
        elif len(card_counts.keys()) == 3:
            if max(card_counts.values()) == 3:
                rank[3][cards] = int(bid)
            else:
                rank[2][cards] = int(bid)
        elif len(card_counts.keys()) == 4:
            rank[1][cards] = int(bid)
        else:
            rank[0][cards] = int(bid)

    tot = 0
    current_rank = 1
    for category in rank:
        for key in sorted(list(category.keys()),
                          key=lambda char: sum([ref.get(char[i]) * (14 ** (4 - i)) for i in range(5)])):
            tot += current_rank * category.get(key)
            current_rank += 1
    return tot


def func_part_ii(_input, ref):
    log_manager.test_log(ref)
    rank = [{} for i in range(7)]
    for cards, bid in _input:
        card_counts = {}
        for card in cards:
            card_counts[card] = card_counts.get(card, 0) + 1

        jokers = card_counts.get("J", 0)

        if jokers != 0:
            del card_counts["J"]
            if jokers != 5:
                greatest_in_num = max(card_counts.keys(), key=lambda char: card_counts.get(char)*13 + ref.get(char))
                card_counts[greatest_in_num] += jokers
            else:
                card_counts["A"] = jokers

        if len(card_counts.keys()) == 1:
            rank[6][cards] = int(bid)
            log_manager.test_log()
        elif len(card_counts.keys()) == 2:
            if max(card_counts.values()) == 4:
                rank[5][cards] = int(bid)
                log_manager.test_log()
            else:
                rank[4][cards] = int(bid)
                log_manager.test_log()
        elif len(card_counts.keys()) == 3:
            if max(card_counts.values()) == 3:
                rank[3][cards] = int(bid)
                log_manager.test_log()
            else:
                rank[2][cards] = int(bid)
                log_manager.test_log()
        elif len(card_counts.keys()) == 4:
            rank[1][cards] = int(bid)
            log_manager.test_log()
        else:
            rank[0][cards] = int(bid)
            log_manager.test_log()

        log_manager.test_log(cards, bid, card_counts, jokers)

    log_manager.test_log(rank)

    tot = 0
    current_rank = 1
    for category in rank:
        for key in sorted(list(category.keys()),
                          key=lambda char: sum([ref.get(char[i]) * (13 ** (4 - i)) for i in range(5)])):
            tot += current_rank * category.get(key)
            current_rank += 1
    return tot


if __name__ == "__main__":
    log_manager = LogManager(f"{__file__.split('/')[-2]:-^22s}")
    data, scores = get_input()
    log_manager.heading()
    log_manager.answer("Part I - Result: ", func_part_i(data, scores))
    scores["J"] = 0
    log_manager.answer("Part II - Result: ", func_part_ii(data, scores))  # 244846263
