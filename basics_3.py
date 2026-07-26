"""
Matplotlib Foundations: Proportional Pie Chart
----------------------------------------------
Demonstrating categorical proportional visualization using plt.pie(), 
percentage formatting (autopct), custom color palettes, slice separation (explode), 
drop shadows, and rotational orientation (startangle).
"""

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # ---------------------------------------------------------
    # 1. Initialize Data
    # ---------------------------------------------------------
    categories = np.array(["Freshmen", "Juniors", "Seniors"])
    values = np.array([33, 25, 28])
    colors = ["#ff6b6b", "#4d96ff", "#6bc36b"]  # Slightly softer red, blue, green shades

    # ---------------------------------------------------------
    # 2. Configure Figure & Plot
    # ---------------------------------------------------------
    plt.figure(figsize=(7, 7))

    # Render pie chart with custom slice separation and percentages
    plt.pie(
        values,
        labels=categories,
        autopct="%.1f%%",
        colors=colors,
        explode=[0, 0, 0.1],  # Pull out the 'Seniors' slice for emphasis
        shadow=True,
        startangle=180,
        textprops={"fontsize": 11, "fontweight": "bold"},
    )

    # Set title
    plt.title("Class Distribution", fontsize=14, fontweight="bold")

    # Tight layout ensures labels don't clip
    plt.tight_layout()

    # Render display
    plt.show()


if __name__ == "__main__":
    main()
