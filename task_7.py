import random
from collections import Counter
import matplotlib.pyplot as plt
from typing import Dict, List


def roll_two_dice() -> int:
    """
    Simulate rolling two six-sided dice and return their sum.

    Returns:
        int: The sum of two dice rolls (from 2 to 12).
    """
    return random.randint(1, 6) + random.randint(1, 6)


def monte_carlo_simulation(num_trials: int) -> Dict[int, float]:
    """
    Perform Monte Carlo simulation of rolling two dice.

    Args:
        num_trials (int): Number of dice rolls to simulate.

    Returns:
        Dict[int, float]: Dictionary mapping each possible sum (2-12)
                          to its estimated probability.
    """
    sums: List[int] = [roll_two_dice() for _ in range(num_trials)]
    counts: Counter = Counter(sums)
    probabilities: Dict[int, float] = {
        total: counts[total] / num_trials for total in range(2, 13)
    }
    return probabilities


def analytical_probabilities() -> Dict[int, float]:
    """
    Analytical probabilities for the sum of two dice.

    Returns:
        Dict[int, float]: Dictionary mapping each possible sum (2-12)
                          to its analytical probability.
    """
    outcomes: Dict[int, int] = {
        2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6,
        8: 5, 9: 4, 10: 3, 11: 2, 12: 1
    }
    total_outcomes: int = 36
    return {k: v / total_outcomes for k, v in outcomes.items()}


def plot_probabilities(
        mc_probs: Dict[int, float], an_probs: Dict[int, float]) -> None:
    """
    Plot Monte Carlo and analytical probabilities for comparison.

    Args:
        mc_probs (Dict[int, float]): Monte Carlo probabilities.
        an_probs (Dict[int, float]): Analytical probabilities.
    """
    sums = list(range(2, 13))
    mc_values = [mc_probs[s] for s in sums]
    an_values = [an_probs[s] for s in sums]

    plt.figure(figsize=(10, 6))
    plt.bar([s - 0.2 for s in sums], mc_values, width=0.4,
            label='Monte Carlo', color='skyblue')
    plt.bar([s + 0.2 for s in sums], an_values,
            width=0.4, label='Analytical', color='orange')
    plt.xlabel('Sum')
    plt.ylabel('Probability')
    plt.title('Probabilities of Sums When Rolling Two Dice')
    plt.xticks(sums)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def print_probability_table(
        mc_probs: Dict[int, float], an_probs: Dict[int, float]) -> None:
    """
    Print a table comparing Monte Carlo and analytical probabilities.

    Args:
        mc_probs (Dict[int, float]): Monte Carlo probabilities.
        an_probs (Dict[int, float]): Analytical probabilities.
    """
    print(f"{'Sum':>3} | {'Monte Carlo':>12} | {'Analytical':>12}")
    print('-' * 36)
    for s in range(2, 13):
        print(f"{s:>3} | {mc_probs[s]:12.4%} | {an_probs[s]:12.4%}")


def main() -> None:
    """
    Main function to run the simulation and display results.
    """
    num_trials = 1_000_000  # Number of dice rolls
    mc_probs = monte_carlo_simulation(num_trials)
    an_probs = analytical_probabilities()

    print_probability_table(mc_probs, an_probs)
    plot_probabilities(mc_probs, an_probs)


if __name__ == "__main__":
    main()
