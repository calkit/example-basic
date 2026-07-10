"""Analyze the relationship between ``x`` and ``y``.

We fit both a linear and a quadratic model and compare their
coefficients of determination (:math:`R^2`) to test whether the
system responds linearly or quadratically to increasing ``x``.
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def r_squared(y: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute the coefficient of determination."""
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    return float(1.0 - ss_res / ss_tot)


if __name__ == "__main__":
    df = pd.read_csv("data/raw/data.csv")
    x = df.x.to_numpy()
    y = df.y.to_numpy()

    # Fit linear and quadratic models
    linear_coeffs = np.polyfit(x, y, deg=1)
    quadratic_coeffs = np.polyfit(x, y, deg=2)
    linear_pred = np.polyval(linear_coeffs, x)
    quadratic_pred = np.polyval(quadratic_coeffs, x)
    r2_linear = r_squared(y, linear_pred)
    r2_quadratic = r_squared(y, quadratic_pred)

    # Plot the data along with both fits
    x_fit = np.linspace(x.min(), x.max(), 200)
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=12, color="0.4", alpha=0.7, label="Data")
    ax.plot(
        x_fit,
        np.polyval(linear_coeffs, x_fit),
        color="tab:orange",
        label=f"Linear fit ($R^2 = {r2_linear:.3f}$)",
    )
    ax.plot(
        x_fit,
        np.polyval(quadratic_coeffs, x_fit),
        color="tab:blue",
        label=f"Quadratic fit ($R^2 = {r2_quadratic:.3f}$)",
    )
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.legend()
    fig.tight_layout()
    os.makedirs("figures", exist_ok=True)
    fig.savefig("figures/x-vs-y.png", dpi=150)

    os.makedirs("results", exist_ok=True)
    with open("results/summary.json", "w") as f:
        json.dump(
            {
                "r_squared_linear": round(r2_linear, 3),
                "r_squared_quadratic": round(r2_quadratic, 3),
            },
            f,
            indent=2,
        )
