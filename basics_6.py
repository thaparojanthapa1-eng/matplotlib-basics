"""
Matplotlib Foundations: Subplot Grids & Multi-Axis Layouts
---------------------------------------------------------
Demonstrating 2x2 grid initialization using plt.subplots(), 2D array 
indexing across axes (axes[row, col]), individual plot customization,
and automatic spacing via plt.tight_layout().
"""

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # ---------------------------------------------------------
    # 1. Initialize Base Domain Data
    # ---------------------------------------------------------
    x = np.array([1, 2, 3, 4, 5])

    # ---------------------------------------------------------
    # 2. Initialize 2x2 Subplot Grid
    # ---------------------------------------------------------
    fig, axes = plt.subplots(2, 2, figsize=(9, 7))

    # Top-Left (Row 0, Col 0): Linear slope y = 2x
    axes[0, 0].plot(x, x * 2, color="blue", marker="o")
    axes[0, 0].set_title("Plot 1: y = 2x")
    axes[0, 0].set_xlabel("x")
    axes[0, 0].set_ylabel("2x")
    axes[0, 0].grid(True, linestyle="--", alpha=0.5)

    # Top-Right (Row 0, Col 1): y = (2/3)x transform
    axes[0, 1].plot(x * 3, x * 2, color="green", marker="s")
    axes[0, 1].set_title("Plot 2: 3x vs 2x")
    axes[0, 1].set_xlabel("3x")
    axes[0, 1].set_ylabel("2x")
    axes[0, 1].grid(True, linestyle="--", alpha=0.5)

    # Bottom-Left (Row 1, Col 0): y = (1/3)x transform
    axes[1, 0].plot(x * 3, x, color="orange", marker="^")
    axes[1, 0].set_title("Plot 3: 3x vs x")
    axes[1, 0].set_xlabel("3x")
    axes[1, 0].set_ylabel("x")
    axes[1, 0].grid(True, linestyle="--", alpha=0.5)

    # Bottom-Right (Row 1, Col 1): Steep slope y = 4x
    axes[1, 1].plot(x, x * 4, color="red", marker="d")
    axes[1, 1].set_title("Plot 4: y = 4x")
    axes[1, 1].set_xlabel("x")
    axes[1, 1].set_ylabel("4x")
    axes[1, 1].grid(True, linestyle="--", alpha=0.5)

    # Automatically adjust subplot padding to prevent overlapping labels
    plt.tight_layout()

    # Render display
    plt.show()


if __name__ == "__main__":
    main()
