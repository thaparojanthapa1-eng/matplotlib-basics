"""
Data Visualization Foundations: Horizontal Bar Chart with Pandas
------------------------------------------------------------------
Demonstrating categorical frequency analysis using pandas value_counts(),
horizontal bar plotting with plt.barh(), axis styling, and dynamic data annotations.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main() -> None:
    # ---------------------------------------------------------
    # 1. Load Data & Compute Frequencies
    # ---------------------------------------------------------
    # Load dataset
    df = pd.read_csv("pokemon_data.csv")

    # Count frequencies per primary type (sorted ascending for top-to-bottom reading)
    type_counts = df["Type1"].value_counts(ascending=True)

    # ---------------------------------------------------------
    # 2. Configure Figure & Plot
    # ---------------------------------------------------------
    plt.figure(figsize=(10, 7))

    # Render horizontal bar chart
    bars = plt.barh(type_counts.index, type_counts.values, color="#4a90e2", edgecolor="black")

    # Add title and axis labels
    plt.title("Number of Pokémon by Primary Type", fontsize=14, fontweight="bold")
    plt.xlabel("Count", fontsize=11)
    plt.ylabel("Type 1", fontsize=11)

    # Add background gridlines along the x-axis for readability
    plt.grid(axis="x", linestyle="--", alpha=0.6)

    # Annotate bars with exact counts at the end of each horizontal bar
    plt.bar_label(bars, padding=4, fontweight="bold")

    plt.tight_layout()

    # Render display
    plt.show()


if __name__ == "__main__":
    main()
