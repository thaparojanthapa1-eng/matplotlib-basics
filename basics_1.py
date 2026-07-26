"""
Matplotlib Foundations: Basic 2D Line Plot
------------------------------------------
Demonstrating basic line plotting, axis labeling, plot titles, 
and display configurations using Matplotlib and NumPy.
"""

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # ---------------------------------------------------------
    # 1. Initialize Data
    # ---------------------------------------------------------
    # Note: 2023 is skipped; Matplotlib automatically scales the x-axis linearly
    years = np.array([2020, 2021, 2022, 2023])
    values = np.array([20, 22, 23, 43])

    # ---------------------------------------------------------
    # 2. Configure & Render Plot
    # ---------------------------------------------------------
    plt.figure(figsize=(8, 5))
    
    # Plot line with markers at data points
    plt.plot(years, values, marker="o", linestyle="-", color="b", label="Growth Trend")

    # Add descriptive labels and title
    plt.title("Value Growth Over Time (2020–2024)")
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    # Display integer year ticks on the x-axis
    plt.xticks(np.arange(2020, 2025, 1))

    # Render display
    plt.show()


if __name__ == "__main__":
    main()
