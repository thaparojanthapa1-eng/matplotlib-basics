"""
Matplotlib Foundations: Categorical Bar Chart
----------------------------------------------
Demonstrating categorical visualization using plt.bar(), custom styling,
axis labels, gridlines, and data annotations.
"""

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # ---------------------------------------------------------
    # 1. Initialize Data
    # ---------------------------------------------------------
    categories = np.array(["fruits", "vegetables", "meat", "dairy", "fish"])
    values = np.array([3, 5, 4, 3, 1])

    # ---------------------------------------------------------
    # 2. Configure Figure & Plot
    # ---------------------------------------------------------
    plt.figure(figsize=(8, 5))

    # Render bar chart with custom color and edge outline
    bars = plt.bar(categories, values, color="skyblue", edgecolor="navy", width=0.6)

    # Add descriptive titles and labels
    plt.title("Daily Consumption Ratio", fontsize=14, fontweight="bold")
    plt.xlabel("Food Category", fontsize=11)
    plt.ylabel("Quantity", fontsize=11)

    # Y-axis gridlines only (cleaner look for bar charts)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Annotate bar tops with exact numeric values
    plt.bar_label(bars, padding=3, fontweight="bold")

    # Tight layout prevents text clipping
    plt.tight_layout()

    # Render display
    plt.show()


if __name__ == "__main__":
    main()
