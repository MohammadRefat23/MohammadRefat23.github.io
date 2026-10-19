#!/usr/bin/env python3
"""Plot the largest August–September VGC weighted-usage changes.

Requirements: pandas, matplotlib

Run from any directory:
    python analysis/plot_usage_comparison.py

By default, reads analysis/monthly_comparison.csv and writes
static/media/vgc-usage-comparison.png relative to the repository root.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV = REPO_ROOT / "analysis" / "monthly_comparison.csv"
DEFAULT_OUTPUT = REPO_ROOT / "static" / "media" / "vgc-usage-comparison.png"


def make_plot(csv_path: Path, output_path: Path) -> None:
    data = pd.read_csv(csv_path)
    shared = data.loc[data["coverage"].eq("both months")].copy()
    if shared.empty:
        raise ValueError("No rows marked 'both months' in the comparison CSV.")

    increases = shared.nlargest(5, "usage_change_pp")
    decreases = shared.nsmallest(5, "usage_change_pp")
    plot_data = pd.concat([increases, decreases], ignore_index=True)

    # 16:9 layout, sized for a portfolio project image.
    plt.rcParams.update({"font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(16, 9), dpi=100, facecolor="#F7F8FA")
    ax = fig.add_axes([0.255, 0.21, 0.58, 0.55])
    ax.set_facecolor("#F7F8FA")

    august = "#68829A"
    september = "#18324A"
    increase_color = "#168779"
    decrease_color = "#C56452"
    ink = "#152D40"
    muted = "#627487"
    grid = "#DDE4E9"

    y_positions = np.arange(len(plot_data))[::-1]
    for y, (_, row) in zip(y_positions, plot_data.iterrows()):
        aug = float(row["aug_usage_pct"])
        sep = float(row["sep_usage_pct"])
        change = float(row["usage_change_pp"])
        direction = increase_color if change > 0 else decrease_color

        ax.plot([aug, sep], [y, y], color=direction, linewidth=4,
                solid_capstyle="round", zorder=1)
        ax.scatter(aug, y, s=82, color=august, edgecolor="#F7F8FA",
                   linewidth=1.4, zorder=3)
        ax.scatter(sep, y, s=92, color=september, edgecolor="#F7F8FA",
                   linewidth=1.4, zorder=4)

        ax.text(69.1, y + 0.28, f"{aug:.1f}% → {sep:.1f}%",
                ha="left", va="center", fontsize=10, color=muted)
        ax.text(69.1, y - 0.25, f"{change:+.2f} pp",
                ha="left", va="center", fontsize=12, fontweight="bold",
                color=direction)

    ax.set_xlim(0, 83)
    ax.set_ylim(-0.65, 9.65)
    ax.set_yticks(y_positions)
    ax.set_yticklabels(plot_data["pokemon"], fontsize=12, color=ink,
                       fontweight="medium")
    ax.tick_params(axis="y", length=0, pad=15)
    ax.set_xticks(np.arange(0, 66, 10))
    ax.set_xticklabels([f"{value}%" for value in range(0, 66, 10)],
                       fontsize=10, color=muted)
    ax.grid(axis="x", color=grid, linewidth=1)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(grid)
    ax.spines["bottom"].set_linewidth(1)
    ax.tick_params(axis="x", length=0, pad=9)
    ax.axhline(4.5, color="#C8D2DA", linewidth=1.2)

    fig.text(0.07, 0.93, "VGC USAGE SHIFTS", fontsize=10,
             fontweight="bold", color=increase_color, ha="left")
    fig.text(0.07, 0.875, "August → September 2026", fontsize=27,
             fontweight="bold", color=ink, ha="left")
    fig.text(0.07, 0.828,
             "Largest weighted-usage changes in Regulation M-B",
             fontsize=14, color=muted, ha="left")
    fig.text(0.255, 0.775, "BIGGEST INCREASES", fontsize=9,
             fontweight="bold", color=increase_color, ha="left")
    fig.text(0.255, 0.473, "BIGGEST DECREASES", fontsize=9,
             fontweight="bold", color=decrease_color, ha="left")

    # Date-color legend.
    legend_y = 0.174
    fig.add_artist(plt.Line2D([0.258, 0.272], [legend_y, legend_y],
                              transform=fig.transFigure, color=august,
                              linewidth=3, solid_capstyle="round"))
    fig.add_artist(plt.Line2D([0.265, 0.265], [legend_y, legend_y],
                              transform=fig.transFigure, marker="o",
                              markersize=7, color=august, linestyle=""))
    fig.text(0.278, legend_y, "August", fontsize=10.5, color=muted,
             va="center")
    fig.add_artist(plt.Line2D([0.344, 0.358], [legend_y, legend_y],
                              transform=fig.transFigure, color=september,
                              linewidth=3, solid_capstyle="round"))
    fig.add_artist(plt.Line2D([0.351, 0.351], [legend_y, legend_y],
                              transform=fig.transFigure, marker="o",
                              markersize=7, color=september, linestyle=""))
    fig.text(0.364, legend_y, "September", fontsize=10.5, color=muted,
             va="center")
    fig.text(0.48, legend_y,
             "Line color and labels show change in percentage points",
             fontsize=10.5, color=muted, va="center")

    fig.text(0.07, 0.092,
             "Top five increases and decreases among 307 Pokémon present in both reports. "
             "Weighted usage is descriptive, not win rate.",
             fontsize=10.5, color=muted, ha="left")
    fig.text(0.07, 0.057,
             "Smogon Champions VGC best-of-three ladder · 1630 rating cutoff · "
             "Reports: Aug 179,434 battles | Sep 38,449 battles",
             fontsize=9.5, color="#7A8997", ha="left")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=100, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved chart to {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV,
                        help=f"comparison CSV (default: {DEFAULT_CSV})")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT,
                        help=f"output PNG (default: {DEFAULT_OUTPUT})")
    args = parser.parse_args()
    make_plot(args.csv, args.output)


if __name__ == "__main__":
    main()
