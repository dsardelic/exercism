def find_fewest_coins(coins, target):
    if not target:
        return []
    if target < 0:
        raise ValueError("target can't be negative")
    if target < min(coins):
        raise ValueError("can't make target with given coins")
    if target in coins:
        return [target]
    coin_groups = [[] for i in range(target + 1)]
    for coin in coins:
        if coin <= target:
            coin_groups[coin] = [coin]
    sorted_coins = sorted(coins)
    for amount in range(sorted_coins[0] + 1, target + 1):
        for coin in sorted_coins:
            if amount - coin < 0:
                break
            if prev_coin_group := coin_groups[amount - coin]:
                if not coin_groups[amount] or len(prev_coin_group) + 1 < len(
                    coin_groups[amount]
                ):
                    coin_groups[amount] = prev_coin_group + [coin]
    if coin_groups[target]:
        return sorted(coin_groups[target])
    raise ValueError("can't make target with given coins")
