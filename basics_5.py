"""
Matplotlib Foundations: Score Distribution Histogram
-----------------------------------------------------
Demonstrating univariate continuous data distribution analysis using plt.hist(),
Gaussian noise generation with np.random.default_rng(), boundary clipping 
with np.clip(), explicit bin edges, and density styling.
"""

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # ---------------------------------------------------------
    # 1. Generate Synthetic Score Data
    # ---------------------------------------------------------
    rng = np.random.default_rng(seed=42)  # Seed for reproducible results

    # Normal distribution with Mean = 70, Std Dev = 25
    scores = rng.normal(loc=70, scale=25, size=100)

    # Restrict scores to valid percentage range [0, 100]
    scores = np.clip(scores, 0, 100)

    # ---------------------------------------------------------
    # 2. Configure Figure & Histogram Plot
    # ---------------------------------------------------------
    plt.figure(figsize=(8, 5))

    # Define 10 uniform bins covering the 0-100 range (e.g., 0-10, 10-20, ..., 90-100)
    bin_edges = np.linspace(0, 100, 11)

    # Render histogram
    n, bins, patches = plt.hist(
        scores,
        bins=bin_edges,
        color="#4a90e2",
        edgecolor="black",
        alpha=0.8,
        rwidth=0.9,
    )

    # Add titles and labels
    plt.title("Exam Score Distribution (n = 100)", fontsize=14, fontweight="bold")
    plt.xlabel("Score Interval", fontsize=11)
    plt.ylabel("Frequency (Number of Students)", fontsize=11)

    # Align ticks with bin boundaries for readability
    plt.xticks(bin_edges)
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    plt.tight_layout()

    # Render display
    plt.show()


if __name__ == "__main__":
    main()
