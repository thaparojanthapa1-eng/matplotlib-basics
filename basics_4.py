"""
Matplotlib Foundations: Feature Scatter Plot
-------------------------------------------
Demonstrating bivariate relationship analysis (Hours Studied vs. Marks)
using plt.scatter(), custom marker styling, axis labels, gridlines,
and visual trend representation.
"""

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # ---------------------------------------------------------
    # 1. Initialize Feature & Target Data
    # ---------------------------------------------------------
    hrs_studied = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
    marks = np.array([12, 15, 19, 19, 27, 30, 31, 32, 36])

    # ---------------------------------------------------------
    # 2. Configure Figure & Plot
    # ---------------------------------------------------------
    plt.figure(figsize=(8, 5))

    # Render scatter plot with custom color, size, and edge outline
    plt.scatter(
        hrs_studied,
        marks,
        color="#2b5c8f",
        edgecolor="black",
        s=70,  # Marker size
        alpha=0.85,
        label="Students",
    )

    # Set title and axis labels
    plt.title("Study Hours vs. Exam Marks", fontsize=14, fontweight="bold")
    plt.xlabel("Hours Studied", fontsize=11)
    plt.ylabel("Marks Obtained", fontsize=11)

    # Add background grid for readability
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    # Set integer ticks for study hours
    plt.xticks(np.arange(0, 9, 1))

    plt.tight_layout()

    # Render display
    plt.show()


if __name__ == "__main__":
    main()
