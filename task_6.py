from typing import Dict, List


def greedy_algorithm(
        items: Dict[str, Dict[str, int]], budget: int) -> List[str]:
    """
    Greedy algorithm to select dishes maximizing the calories-to-cost ratio within the budget.

    Args:
        items: Dictionary of dishes with their cost and calories.
        budget: Maximum allowed total cost.

    Returns:
        List of selected dish names.
    """
    # Calculate calories-to-cost ratio for each dish
    ratios = []
    for name, info in items.items():
        ratio = info["calories"] / info["cost"]
        ratios.append((ratio, name))

    ratios.sort(reverse=True)
    total_cost = 0
    chosen = []
    for ratio, name in ratios:
        if total_cost + items[name]["cost"] <= budget:
            chosen.append(name)
            total_cost += items[name]["cost"]
    return chosen


def dynamic_programming(
        items: Dict[str, Dict[str, int]], budget: int) -> List[str]:
    """
    Dynamic programming algorithm to select the optimal set of dishes maximizing total calories within the budget.

    Args:
        items: Dictionary of dishes with their cost and calories.
        budget: Maximum allowed total cost.

    Returns:
        List of selected dish names.
    """
    # Convert dictionary to lists for easier indexing
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(names[i - 1])
            w -= costs[i - 1]
    chosen.reverse()
    return chosen


if __name__ == "__main__":
    test_budget = 100
    test_items: Dict[str, Dict[str, int]] = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    print(
        "Greedy algorithm selection:",
        greedy_algorithm(
            test_items,
            test_budget))
    print(
        "Dynamic programming selection:",
        dynamic_programming(
            test_items,
            test_budget))
